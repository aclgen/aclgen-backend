from rest_framework import serializers
from app.api.models.device import Device
from app.api.models.rules import Rule
from app.api.serializers.rule import RuleSerializer
from app.api.fields import CurrentRepositoryDefault


class ReadDeviceSerializer(serializers.ModelSerializer):
    rules = RuleSerializer(many=True, read_only=True)

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
            "rules",
        )


class DeviceSerializer(serializers.ModelSerializer):
    repository = serializers.HiddenField(default=CurrentRepositoryDefault())
    # TODO Not working?
    rules = RuleSerializer(many=True, read_only=True, source="devices_rules")

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
            "rules",
        )

