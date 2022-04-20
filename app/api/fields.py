from rest_framework import serializers
from app.api.models.repository import Repository
from app.api.models.device import Device
from django.db.models import ObjectDoesNotExist
from django.core.exceptions import ValidationError


class ModelObjectIdField(serializers.Field):
    def to_representation(self, value):
        return value.id

    def to_internal_value(self, data):
        return data


class CurrentRepositoryDefault(object):
    requires_context = True

    def __call__(self, serializer_field):
        try:
            self.repository = Repository.objects.get(
                id=serializer_field.context["request"].parser_context["kwargs"]["repo_id"]
            )
        except ObjectDoesNotExist:
            raise ValidationError("Repository does not exist")

        return self.repository


class CurrentDeviceDefault(object):
    requires_context = True

    def __call__(self, serializer_field):
        try:
            self.device = Device.objects.get(
                id=serializer_field.context["request"].parser_context["kwargs"]["dev_id"]
            )
        except ObjectDoesNotExist:
            raise ValidationError("Device does not exist")

        return self.device

