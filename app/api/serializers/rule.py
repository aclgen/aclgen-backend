from rest_framework import serializers
from app.api.models.rules import Rule


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = [
            "id",
            "name",
            "comment",
            "device",
            "repository",
            "source",
            "destination",
            "service",
            "direction",
            "action"
        ]
