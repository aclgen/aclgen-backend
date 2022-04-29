from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from app.util.models import BaseModel
from app.common.mixins import UUIDPrimarySelfMixin, UUIDPrimaryMixin
from app.api.models.repository import Repository


class Folder(UUIDPrimaryMixin, BaseModel):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name="folders")

    name = models.TextField(max_length=64, blank=False)

    class Meta:
        verbose_name = "Folder"


class FolderItem(UUIDPrimaryMixin):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=False, null=False,
                               related_name="folder_items")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField(auto_created=False, primary_key=False, serialize=False)
    content_object = GenericForeignKey('content_type', 'object_id')


