from rest_framework import serializers
from app.api.models.repository import Repository


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = [
            "id",
            "name",
            "created_on",
            "modified_on",
        ]

