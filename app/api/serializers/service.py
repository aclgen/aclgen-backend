from rest_framework import serializers
from app.api.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "port_start",
            "port_end",
            "protocol",
            "repository",
            "created_on",
            "modified_on",
        ]

