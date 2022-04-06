from django.db import models
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimaryMixin
from app.api.mixins import RepositoryLinkMixin
from app.api.enums import DeviceType


class Device(UUIDPrimaryMixin, RepositoryLinkMixin, BaseModel):
    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)
    type = models.CharField(max_length=64, choices=DeviceType.choices(), default=DeviceType.FIREWALL)
    # TODO: Add other Device Specific fields?

    class Meta:
        verbose_name = "Device"

    def __str__(self):
        return f"{self.id}: {self.name} in {self.repository.name}"
