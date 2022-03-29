from base import BaseRuleModel
from django.db import models


class Ruleset(BaseRuleModel):
    elements = models.JSONField()

    class Meta:
        verbose_name = "Ruleset"

    def __str__(self):
        return f"{self.name}"

