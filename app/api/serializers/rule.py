from rest_framework import serializers
from app.api.models.rules import Rule
from app.api.fields import CurrentDeviceDefault, CurrentRepositoryDefault


class RuleSerializer(serializers.ModelSerializer):
    repository = serializers.HiddenField(default=CurrentRepositoryDefault())
    device = serializers.HiddenField(default=CurrentDeviceDefault())

    class Meta:
        model = Rule
        fields = (
            "id",
            "name",
            "comment",
            "device",
            "status",
            "repository",
            "sources",
            "destinations",
            "services_sources",
            "services_destinations",
            "direction",
            "action",
            "folder",
            "created_on",
            "modified_on",
        )
        read_only_fields = (
            "created_on",
            "modified_on",
            "status",
        )
