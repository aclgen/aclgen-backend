from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimaryMixin, UUIDPrimarySelfMixin
from app.api.enums import Protocol
from app.api.mixins import RepositoryLinkMixin, StatusFieldMixin
from app.api.models.repository import Repository


# TODO: Unfinished Folder model / Model not in use
# class Folder(UUIDPrimaryMixin, RepositoryLinkMixin, BaseModel):
#     name = models.TextField(max_length=64)
#     parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")
#
#     class Meta:
#         verbose_name = "Folder"
#
#     def __str__(self):
#         return f"{self.id}: {self.name}"


# TODO: Unfinished Collection model / Model not in use
class Collection(UUIDPrimaryMixin, RepositoryLinkMixin, BaseModel):
    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)
    #folder = models.ManyToManyField(Folder, related_name="collections")

    class Meta:
        verbose_name = "Collection"


class Service(UUIDPrimarySelfMixin, BaseModel, StatusFieldMixin):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="services")
    name = models.TextField(max_length=64)
    comment = models.TextField(max_length=255)
    port_start = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    port_end = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)])
    protocol = models.CharField(max_length=64, choices=Protocol.choices(), default=Protocol.UDP)

    class Meta:
        verbose_name = "Service"

    def __str__(self):
        return f"{self.name}: {self.port_start} to {self.port_end} /{self.protocol}"
