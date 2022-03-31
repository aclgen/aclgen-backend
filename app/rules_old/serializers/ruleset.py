from rest_framework import serializers
from app.rules_old.models.ruleset import RuleSet


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

