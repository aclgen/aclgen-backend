import uuid

from django.db import models


class UUIDPrimaryMixin(models.Model):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4,
        serialize=False,
    )

    class Meta:
        abstract = True


class UUIDPrimarySelfMixin(models.Model):
    id = models.UUIDField(
        auto_created=False,
        primary_key=True,
        default=uuid.uuid4,
        serialize=False,
    )

    class Meta:
        abstract = True
