from django.db import models
from app.rules_old.models.base import BaseRuleModel

import uuid


class Rule(BaseRuleModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4(),
        serialize=False,
    )
    source = models.TextField(max_length=255)
    destination = models.TextField(max_length=255)
    service = models.TextField(max_length=255)