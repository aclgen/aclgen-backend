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


class CollectionTypeService(models.Model):
    members = models.ManyToManyField("Service", blank=True, null=True)

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
    type = models.CharField(max_length=65, choices=ServiceType.choices(), blank=False)
    lock = models.CharField(max_length=64, choices=LockStatus.choices(), default=LockStatus.UNLOCKED,
                            blank=False, null=False)


@receiver(post_save, sender=Repository)
def create_standard_services(sender, instance, created, **kwargs):
    auto_default_creation_enabled = True

    if created and auto_default_creation_enabled:
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

    # TODO: Override save method to do error checking for to avoid fields other than its related type have data



