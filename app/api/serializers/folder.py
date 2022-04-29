from rest_framework import serializers
from app.api.models.device import DeviceFolder
from app.api.fields import CurrentDeviceDefault


class DeviceFolderRulesSerializer(serializers.ModelSerializer):
    rules = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source="rule_folders")

    class Meta:
        model = DeviceFolder
        fields = (
            "id",
            "name",
            "rules",
        )


class DeviceFolderSerializer(serializers.ModelSerializer):
    device = serializers.HiddenField(default=CurrentDeviceDefault())

    class Meta:
        model = DeviceFolder
        fields = (
            "id",
            "name",
            "device"
        )
        read_only_fields = (
            "id",
            "device"
        )

