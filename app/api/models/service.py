import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.enums import Protocol, LockStatus
from app.api.mixins import StatusFieldMixin
from app.api.models.repository import Repository
from app.api.enums import ServiceType


class Service(UUIDPrimarySelfMixin, BaseModel, StatusFieldMixin):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="services")

    name = models.TextField(max_length=128)
    comment = models.TextField(max_length=255)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

    lock = models.CharField(max_length=64, choices=LockStatus.choices(), default=LockStatus.UNLOCKED, blank=True)

    class Meta:
        verbose_name = "Service"
        unique_together = (('id', 'repository'),)


class CollectionService(models.Model):
    service = GenericRelation(Service, related_query_name="service")
    type = ServiceType.COLLECTION

    services = models.ManyToManyField(Service, related_name="collection_services")


class ICMPService(models.Model):
    service = GenericRelation(Service, related_query_name="service")
    type = ServiceType.ICMP

    icmp_type = models.IntegerField(default=0)
    icmp_code = models.IntegerField(default=0)


class PortRangeService(models.Model):
    service = GenericRelation(Service, related_query_name="service")
    type = ServiceType.PORT

    port_start = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    port_end = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    protocol = models.CharField(max_length=64, choices=Protocol.choices(), default=Protocol.UDP)


@receiver(post_save, sender=Repository)
def create_standard_services(sender, instance, created, **kwargs):
    auto_default_creation_enabled = True

    if created and auto_default_creation_enabled:
        # Default TCP Any Service
        default_any_tcp_service = Service.objects.create(
            id=uuid.uuid4(),
            name="TCP Any",
            comment="TCP Any Service",
            repository=instance,
            lock="IMMUTABLE",
            item=PortRangeService.objects.create(
                port_start=0,
                port_end=65535,
                protocol="TCP",
            )
        )

        # Default UDP Any Service
        default_any_udp_service = Service.objects.create(
            id=uuid.uuid4(),
            name="UDP Any",
            comment="UDP Any Service",
            repository=instance,
            lock="IMMUTABLE",
            item=PortRangeService.objects.create(
                port_start=0,
                port_end=65535,
                protocol="UDP",
            )
        )

        # Default ICMP Service (test)
        default_dummy_icmp_service = Service.objects.create(
            id=uuid.uuid4(),
            name="ICMP Dummy Test",
            comment="Testing ICMP",
            repository=instance,
            lock="IMMUTABLE",
            item=ICMPService.objects.create(
                icmp_type=0,
                icmp_code=2,
            )
        )

        # Default Any Service Collection for TCP and UDP
        any_collection_uuid = uuid.uuid4()

        any_collection = Service.objects.create(
            id=any_collection_uuid,
            name="Any",
            comment="Any Service for UDP and TCP",
            repository=instance,
            lock="UNLOCKED",
            item=CollectionService.objects.create()
        )

        any_collection.item.services.add(default_any_udp_service)
        any_collection.item.services.add(default_any_tcp_service)

