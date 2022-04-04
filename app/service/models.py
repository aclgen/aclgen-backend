import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from app.util.models import BaseModel
from app.service.enums import Protocol


class Folder(BaseModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        serialize=False,
    )
    name = models.TextField(max_length=64)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"

    def __str__(self):
        return f"{self.id}: {self.name}"


class Collection(BaseModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        serialize=False,
    )
    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)
    folder = models.ManyToManyField(Folder, related_name="folders")

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        return f"{self.name}"


class Service(BaseModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        serialize=False,
    )
    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)
    port_start = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    port_end = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    protocol = models.CharField(max_length=64, choices=Protocol.choices(), default=Protocol.UDP)
    collection = models.ManyToManyField(Collection, related_name="collections")  # TODO: test this

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.name}: {self.port}/{self.protocol}"

