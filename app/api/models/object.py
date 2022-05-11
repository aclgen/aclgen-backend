import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.mixins import StatusFieldMixin
from app.api.models.repository import Repository
from app.api.enums import LockStatus, ObjectType
from app.api.utils import raise_validation_error_detail, validate_empty_fields


class CollectionTypeObject(models.Model):
    members = models.ManyToManyField("Object", blank=True)

    class Meta:
        abstract = True


class IPV4TypeObject(models.Model):
    range_start = models.TextField(max_length=64, blank=True, null=True)
    range_end = models.TextField(max_length=64, blank=True, null=True)

    class Meta:
        abstract = True


class IPV6TypeObject(models.Model):
    ipv6_range_start = models.TextField(max_length=128, blank=True, null=True)
    ipv6_range_end = models.TextField(max_length=128, blank=True, null=True)

    class Meta:
        abstract = True


class Object(
    UUIDPrimarySelfMixin,
    BaseModel,
    StatusFieldMixin,
    CollectionTypeObject,
    IPV4TypeObject,
    IPV6TypeObject
):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="objectlist")

    name = models.TextField(max_length=128, blank=False, null=False)
    comment = models.TextField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=65, choices=ObjectType.choices(), blank=False, null=False)
    lock = models.CharField(max_length=64, choices=LockStatus.choices(), default=LockStatus.UNLOCKED,
                            blank=False, null=False)

    class Meta:
        verbose_name = "Object"
        unique_together = (('id', 'repository'),)

    def __str__(self):
        return f"{self.id}@{self.name}"

    def _validate_type_ipv4(self):
        if self.range_start is None:
            raise_validation_error_detail("range_start must be given a value")

        if self.range_end is None:
            raise_validation_error_detail("range_end must be given a value")

        required_empty_fields = ["ipv6_range_start", "ipv6_range_end", "members"]
        validate_empty_fields(context=self, required_empty_fields=required_empty_fields)

    def _validate_type_ipv6(self):
        if self.ipv6_range_start is None:
            raise_validation_error_detail("ipv6_range_start must be given a value")

        if self.ipv6_range_end is None:
            raise_validation_error_detail("ipv6_range_end must be given a value")

        required_empty_fields = ["range_start", "range_end", "members"]
        validate_empty_fields(context=self, required_empty_fields=required_empty_fields)

    def _validate_type_collection(self):
        if self.members is None:
            raise_validation_error_detail("the collection must contain members")

        required_empty_fields = ["range_start", "range_end", "ipv6_range_start", "ipv6_range_end"]
        validate_empty_fields(context=self, required_empty_fields=required_empty_fields)

    def save(self, *args, **kwargs):
        print("Object.model save() called")
        if self.type == ObjectType.IPV4:
            print("check ipv4")
            self._validate_type_ipv4()

        if self.type == ObjectType.IPV6:
            print("check ipv6")
            self._validate_type_ipv6()

        if self.type == ObjectType.COLLECTION:
            print("check collection")
            self._validate_type_collection()

        return super().save(*args, **kwargs)


@receiver(post_save, sender=Repository)
def create_standard_objects(sender, instance, created, **kwargs):
    if created:
        Object.objects.create(
            id=uuid.uuid4(),
            name="ANY (IPV4)",
            comment="Any IPV4 address",
            range_start="0.0.0.1",
            range_end="255.255.255.254",
            repository=instance,
            type="IPV4",
            lock="IMMUTABLE"
        )
