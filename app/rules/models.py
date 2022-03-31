import uuid

from django.db import models
from app.util.models import BaseModel
from app.rules.enums import Direction, Action
from app.object.models import Object


class BaseRuleModel(BaseModel):
    """Abstract rule model for rule and ruleset objects. Inherits BaseModel."""
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        serialize=False,
    )
    name = models.TextField(max_length=64, blank=False)
    comment = models.TextField(max_length=255, blank=True)

    class Meta:
        abstract = True


class RuleSet(BaseRuleModel):
    class Meta:
        verbose_name = "Ruleset"

    def __str__(self):
        return f"{self.id}: {self.name}"


class Rule(BaseRuleModel):
    ruleset = models.ForeignKey(RuleSet, on_delete=models.CASCADE, related_name="ruleset")
    #source = models.TextField(max_length=255)  # TODO: add ForeignKey --> Object (Source)
    source = models.ForeignKey(Object, on_delete=models.SET(Object.get_deleted_object_dummy), related_name="source")
    #destination = models.TextField(max_length=255)  # TODO: add ForeignKey --> Object (Dest)
    destination = models.ForeignKey(Object, on_delete=models.SET(Object.get_deleted_object_dummy), related_name="destination")
    service = models.TextField(max_length=255)  # TODO: add ForeignKey --> Service
    direction = models.CharField(max_length=64, choices=Direction.choices(), default=Direction.INBOUND)
    action = models.TextField(max_length=64, choices=Action.choices(), default=Action.ACCEPT)

    class Meta:
        verbose_name = "Rule"

    def __str__(self):
        return f"{self.id}: {self.name}"

