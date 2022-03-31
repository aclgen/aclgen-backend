import uuid

from django.db import models
from app.rules_old.models.base import BaseRuleModel


class RuleSet(BaseRuleModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4(),
        serialize=False,
    )

    class Meta:
        verbose_name = "Ruleset"

    def __str__(self):
        return f"{self.name}"

