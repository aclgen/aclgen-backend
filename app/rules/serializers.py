from rest_framework import serializers
from app.rules.models import RuleSet, Rule


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


class RuleSetSerializer(serializers.ModelSerializer):
    rules = serializers.StringRelatedField(many=True)

    class Meta:
        model = RuleSet
        fields = [
            "id",
            "name",
            "comment",
            "created_on",
            "modified_on",
            "rules"
        ]

