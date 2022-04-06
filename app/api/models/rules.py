from django.db import models
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimaryMixin
from app.api.mixins import RepositoryLinkMixin
from app.api.models.object import Object
from app.api.models.service import Service
from app.api.models.device import Device
from app.api.enums import RuleDirection, RuleAction


class Rule(UUIDPrimaryMixin, RepositoryLinkMixin, BaseModel):
    name = models.TextField(max_length=64, blank=False)
    comment = models.TextField(max_length=255, blank=True)

    # Device
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="device_rules")

    # Objects (foreign keys)
    source = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="source_objects")
    destination = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="dest_objects")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")

    # Direction & Action (enums)
    direction = models.CharField(max_length=64, choices=RuleDirection.choices(), default=RuleDirection.INBOUND)
    action = models.CharField(max_length=64, choices=RuleAction.choices(), default=RuleAction.ACCEPT)

    class Meta:
        verbose_name = "Rule"

    def __str__(self):
        return f"{self.id}: {self.name}"

