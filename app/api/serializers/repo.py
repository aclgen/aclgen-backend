from rest_framework import serializers
from app.api.models.repository import Repository
from app.api.serializers.service import ServiceSerializer
from app.api.serializers.object import ObjectSerializer
from app.api.serializers.device import FullDeviceSerializer
from app.api.serializers.folder import DeviceFolderSerializer


class FullRepositorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    devices = FullDeviceSerializer(many=True, read_only=True)
    objects = ObjectSerializer(many=True, read_only=True, source="objectlist")
    folders = DeviceFolderSerializer(many=True, read_only=True)

    class Meta:
        model = Repository
        fields = (
            "id",
            "name",
            "created_on",
            "modified_on",
            "services",
            "objects",
            "devices",
            "folders",
        )


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = [
            "id",
            "name",
            "created_on",
            "modified_on",
        ]

