from rest_framework import serializers
from app.api.models.object import Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = [
            "id",
            "name",
            "comment",
            "status",
            "repository",
            "range_start",
            "range_end",
            "created_on",
            "modified_on",
        ]
