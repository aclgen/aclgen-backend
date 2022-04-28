from rest_framework import serializers
from app.api.models.service import Service
from app.api.fields import CurrentRepositoryDefault
from app.api.utils import update_repository_modified_on
from app.common.serializers import BaseListSerializer


class ListServiceSerializer(BaseListSerializer):
    def update(self, instances, validated_data):
        return super(ListServiceSerializer, self).update(instances, validated_data)

    def update_parent_modified_on(self, result):
        update_repository_modified_on(result)


class ServiceSerializer(serializers.ModelSerializer):
    repository = serializers.HiddenField(default=CurrentRepositoryDefault())

    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "port_start",
            "port_end",
            "protocol",
            "repository",
            "created_on",
            "modified_on",
            "status",
        )
        read_only_fields = (
            "created_on",
            "modified_on",
            "status",
        )
        list_serializer_class = ListServiceSerializer


