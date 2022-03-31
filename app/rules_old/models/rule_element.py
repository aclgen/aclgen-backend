from app.rules_old.models.base import BaseRuleModel
from ruleset import RuleSet
from django.db import models


class RuleElement(BaseRuleModel):
    ruleset = models.ForeignKey(RuleSet, on_delete=models.CASCADE, related_name="ruleset")
    order = models.IntegerField()

    class Meta:
        verbose_name = "RuleElement"
        ordering = ("-order",)
