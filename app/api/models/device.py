from django.db import models
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.mixins import StatusFieldMixin
from app.api.enums import DeviceType
from app.api.models.repository import Repository


class Device(UUIDPrimarySelfMixin, BaseModel, StatusFieldMixin):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="devices")
    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)
    type = models.CharField(max_length=64, choices=DeviceType.choices(), default=DeviceType.FIREWALL)

    class Meta:
        verbose_name = "Device"

    def __str__(self):
        return f"{self.id}: {self.name} in {self.repository.name}"
