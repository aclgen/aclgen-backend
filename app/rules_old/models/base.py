from app.util.models import BaseModel
from django.db import models


class BaseRuleModel(BaseModel):
    """Abstract model for rules_old"""

    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)

    class Meta:
        abstract = True
