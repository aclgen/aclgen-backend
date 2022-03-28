from django.db import models
from app.util.models import BaseModel


class Object(BaseModel):
    name = models.TextField(max_length=32)
    description = models.TextField(max_length=255)
    defs = models.JSONField(encoder=None)

    class Meta:
        verbose_name = "Object"

    def __str__(self):
        return f"{self.name}"
