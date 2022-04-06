from django.db import models
from app.api.models.repository import Repository


class RepositoryLinkMixin(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        abstract = True

