from django.db import models
from app.util.models import BaseModel

import uuid


class Object(BaseModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4(),
        serialize=False,
    )
    name = models.TextField(max_length=32)
    description = models.TextField(max_length=255)
    defs = models.JSONField(encoder=None)

    class Meta:
        verbose_name = "Object"

    def __str__(self):
        return f"{self.name}"
