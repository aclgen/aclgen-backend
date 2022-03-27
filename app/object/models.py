from django.db import models
from app.util.models import BaseModel


class Object(BaseModel):
    name = models.TextField(max_length=32)
    description = models.TextField(max_length=255)
    defs = models.JSONField(encoder=None)

    def __str__(self):
        return self.name
