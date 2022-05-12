import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.enums import Protocol, LockStatus
from app.api.mixins import StatusFieldMixin
from app.api.models.repository import Repository
from app.api.enums import ServiceType
from app.api.utils import validate_empty_fields
from rest_framework.exceptions import ValidationError


class CollectionTypeService(models.Model):
    members = models.ManyToManyField("Service", blank=True)

    class Meta:
        abstract = True


class ICMPTypeService(models.Model):
    icmp_type = models.PositiveSmallIntegerField(blank=True, null=True)
    icmp_code = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class PortTypeService(models.Model):
    port_start = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)], blank=True, null=True)
    port_end = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)], blank=True, null=True)
    protocol = models.CharField(max_length=64, choices=Protocol.choices(), blank=True, null=True)

    class Meta:
        abstract = True


class Service(
    UUIDPrimarySelfMixin,
    BaseModel,
    StatusFieldMixin,
    CollectionTypeService,
    ICMPTypeService,
    PortTypeService
):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="services")

    name = models.TextField(max_length=128, blank=False, null=False)
    comment = models.TextField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=65, choices=ServiceType.choices(), blank=False, null=False)
    lock = models.CharField(max_length=64, choices=LockStatus.choices(), default=LockStatus.UNLOCKED,
                            blank=False, null=False)

    class Meta:
        verbose_name = "Service"
        unique_together = (('id', 'repository'),)

    def _validate_empty_fields(self, required_empty_fields=[]):
        validate_empty_fields(context=self, required_empty_fields=required_empty_fields)

    def _validate_type_port(self):
        if self.port_start is None:
            raise ValidationError({"detail": "port_start must be given a value"})

        if self.port_end is None:
            raise ValidationError({"detail": "port_end must be given a value"})

        if self.protocol is None:
            raise ValidationError({"detail": "protocol must be specified"})

        required_empty_fields = ["icmp_type", "icmp_code", "members"]
        self._validate_empty_fields(required_empty_fields=required_empty_fields)

    def _validate_type_icmp(self):
        if self.icmp_type is None:
            raise ValidationError({"detail": "icmp_type must be given a value"})

        if self.icmp_code is None:
            raise ValidationError({"detail": "icmp_code must be given a value"})

        required_empty_fields = ["port_start", "port_end", "protocol", "members"]
        self._validate_empty_fields(required_empty_fields=required_empty_fields)

    def _validate_type_collection(self):
        if self.members is None:
            raise ValidationError({"detail": "the collection must contain members"})

        required_empty_fields = ["port_start", "port_end", "protocol", "icmp_type", "icmp_code"]
        self._validate_empty_fields(required_empty_fields=required_empty_fields)

    def save(self, *args, **kwargs):
        print("Service save()")
        if self.type == ServiceType.PORT:
            self._validate_type_port()

        if self.type == ServiceType.COLLECTION:
            self._validate_type_collection()

        if self.type == ServiceType.ICMP:
            self._validate_type_icmp()

        return super().save(*args, **kwargs)


@receiver(post_save, sender=Repository)
def create_standard_services(sender, instance, created, **kwargs):
    auto_default_creation_enabled = True

    if created and auto_default_creation_enabled:
        print("Instance: ", instance)

        print("Debug: Creating default Service")
        # Default TCP Any Service
        default_tcp_any_service = Service.objects.create(
            id=uuid.uuid4(),
            name="TCP Any",
            comment="TCP Any Service",
            type="PORT",
            repository=instance,
            lock="IMMUTABLE",
            port_start=0,
            port_end=65535,
            protocol="TCP"
        )

        # Default UDP Any Service
        default_udp_any_service = Service.objects.create(
            id=uuid.uuid4(),
            name="UDP Any",
            comment="UDP Any Service",
            type="PORT",
            repository=instance,
            lock="IMMUTABLE",
            port_start=0,
            port_end=65535,
            protocol="TCP"
        )

        # Default UDP/TCP Any Service Collection
        default_any_collection = Service.objects.create(
            id=uuid.uuid4(),
            name="TCP/UDP Any",
            comment="TCP&UDP Service Group",
            type="COLLECTION",
            repository=instance,
            lock="UNLOCKED"
        )

        # Dummy ICMP Test
        default_dummy_icmp = Service.objects.create(
            id=uuid.uuid4(),
            name="Dummy ICMP",
            comment="Dummy ICMP service",
            type="ICMP",
            repository=instance,
            lock="UNLOCKED",
            icmp_type=0,
            icmp_code=2
        )

        default_any_collection.members.add(default_udp_any_service)
        default_any_collection.members.add(default_tcp_any_service)
