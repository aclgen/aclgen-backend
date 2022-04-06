import uuid

from django.db import models
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimaryMixin


class Repository(UUIDPrimaryMixin, BaseModel):
    name = models.TextField(max_length=64)

    class Meta:
        verbose_name = "Repository"
