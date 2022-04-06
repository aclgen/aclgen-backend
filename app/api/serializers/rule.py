from rest_framework import serializers
from app.api.models.rules import Rule, RuleSet


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = [
            "id",
            "name",
            "comment",
            "ruleset",
            "repository",
            "source",
            "destination",
            "service",
            "direction",
            "action"
        ]
