import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.mixins import StatusFieldMixin
from app.api.models.repository import Repository
from app.api.enums import LockStatus


class ObjectGroup(UUIDPrimarySelfMixin, BaseModel, StatusFieldMixin):
    name = models.TextField(max_length=32)
    comment = models.TextField(max_length=255)

    lock = models.CharField(max_length=64, choices=LockStatus.choices(), default=LockStatus.UNLOCKED)


class Object(UUIDPrimarySelfMixin, BaseModel, StatusFieldMixin):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="objectlist")
    name = models.TextField(max_length=32)
    comment = models.TextField(max_length=255)
    range_start = models.TextField(max_length=64)
    range_end = models.TextField(max_length=64)

    lock = models.CharField(max_length=64, choices=LockStatus.choices(), default=LockStatus.UNLOCKED)

    group = models.ManyToManyField(ObjectGroup, related_name="groupobjects", blank=True, null=True)

    class Meta:
        verbose_name = "Object"

    def __str__(self):
        return f"{self.id}@{self.name}"


@receiver(post_save, sender=Repository)
def create_standard_objects(sender, instance, created, **kwargs):
    if created:
        Object.objects.create(
            id=uuid.uuid4(),
            name="ANY",
            comment="Any IP address",
            range_start="0.0.0.1",
            range_end="255.255.255.254",
            repository=instance,
            lock="IMMUTABLE"
        )
