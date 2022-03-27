from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, editable=False)
    updated = models.DateTimeField(auto_now=True, blank=True, editable=False)

    class Meta:
        abstract = True

