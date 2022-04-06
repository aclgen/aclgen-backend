from rest_framework import serializers
from app.api.models.device import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "id",
            "name",
            "type",
            "repository",
            "created_on",
            "modified_on",
        ]

