from rest_framework import serializers
from app.rules.models.ruleset import RuleSet


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

