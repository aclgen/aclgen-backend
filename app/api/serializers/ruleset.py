from rest_framework import serializers
from app.api.models.rules import RuleSet


class RuleSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleSet
        fields = [
            "id",
            "name",
            "comment",
            "device",
            "repository",
            "created_on",
            "modified_on",
        ]

