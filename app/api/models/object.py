from django.db import models
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin
from app.api.mixins import StatusFieldMixin
from app.api.models.repository import Repository


class Object(UUIDPrimarySelfMixin, BaseModel, StatusFieldMixin):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="objectlist")
    name = models.TextField(max_length=32)
    comment = models.TextField(max_length=255)
    range_start = models.TextField(max_length=64)
    range_end = models.TextField(max_length=64)

    class Meta:
        verbose_name = "Object"

    def __str__(self):
        return f"{self.id}@{self.name}"
