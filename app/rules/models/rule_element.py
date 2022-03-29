from base import BaseRuleModel
from django.db import models


class RuleElement(BaseRuleModel):
    order = models.IntegerField()

    class Meta:
        verbose_name = "RuleElement"
        