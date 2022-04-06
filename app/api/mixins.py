from django.db import models
from app.api.models.repository import Repository


class RepositoryLinkMixin(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        abstract = True


class StatusFieldMixin(models.Model):
    """Status field to support frontend feature.
    Field isn't saved to the database as it is static and will never change value"""
    status = "source"

    class Meta:
        abstract = True
