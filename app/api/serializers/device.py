from rest_framework import serializers
from app.api.models.device import Device
from app.api.serializers.rule import RuleSerializer
from app.api.fields import CurrentRepositoryDefault
from app.api.utils import update_repository_modified_on_target


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
    rules = RuleSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        Update the modified_on time for the parent Repository
        """
        update_repository_modified_on_target(validated_data["repository"])
        return super(DeviceSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """
        Update the modified_on time for the parent Repository
        """
        update_repository_modified_on_target(validated_data["repository"])
        return super(DeviceSerializer, self).update(instance, validated_data)

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
        read_only_fields = (
            "created_on",
            "modified_on",
            "status",
        )

