from rest_framework import serializers
from app.api.models.device import Device
from app.api.fields import CurrentRepositoryDefault


class DeviceSerializer(serializers.ModelSerializer):
    repository = serializers.HiddenField(default=CurrentRepositoryDefault())

    class Meta:
        model = Device
        fields = (
            "id",
            "name",
            "type",
            "status",
            "repository",
            "created_on",
            "modified_on",
        )

