from rest_framework import serializers
from .models import Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = [
            "name",
            "description",
            "defs",
            "created",
            "updated"
        ]

        