from rest_framework import serializers
from app.rules.models import RuleSet, Rule


class RuleSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleSet
        fields = [
            "id",
            "name",
            "comment",
            "created_on",
            "modified_on"
        ]


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = [
            "id",
            "ruleset",
            "name",
            "comment",
            "created_on",
            "modified_on",
            "source",
            "destination",
            "service",
            "direction",
            "action"
        ]

