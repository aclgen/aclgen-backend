from django.db import models
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.mixins import RepositoryLinkMixin, StatusFieldMixin
from app.api.models.object import Object
from app.api.models.service import Service
from app.api.models.device import Device
from app.api.enums import RuleDirection, RuleAction
from app.api.models.device import DeviceFolder


class Rule(UUIDPrimarySelfMixin, RepositoryLinkMixin, BaseModel, StatusFieldMixin):
    name = models.TextField(max_length=64, blank=False)
    comment = models.TextField(max_length=255, blank=True)

    # Device
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="rules")

    # Objects (foreign keys)
    sources = models.ManyToManyField(Object, related_name="rule_sources")
    destinations = models.ManyToManyField(Object, related_name="rule_destinations")
    services_sources = models.ManyToManyField(Service, related_name="rule_services_source", blank=True, null=True)
    services_destinations = models.ManyToManyField(Service, related_name="rule_services_destination", blank=True, null=True)

    # Direction & Action (enums)
    direction = models.CharField(max_length=64, choices=RuleDirection.choices(), default=RuleDirection.INBOUND)
    action = models.CharField(max_length=64, choices=RuleAction.choices(), default=RuleAction.ACCEPT)

    # Folder
    folder = models.ForeignKey(DeviceFolder, on_delete=models.CASCADE, related_name="rule_folders",
                               blank=False, null=False)

    class Meta:
        verbose_name = "Rule"

    def __str__(self):
        return f"{self.id}: {self.name}"

