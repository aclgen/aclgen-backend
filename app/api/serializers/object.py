from rest_framework import serializers
from app.api.models.object import Object
from app.api.fields import CurrentRepositoryDefault
from app.api.utils import update_repository_modified_on
from app.common.serializers import BaseListSerializer


class ListObjectSerializer(BaseListSerializer):
    def update(self, instances, validated_data):
        return super(ListObjectSerializer, self).update(instances, validated_data)

    def update_parent_modified_on(self, result):
        update_repository_modified_on(result)


class ObjectSerializer(serializers.ModelSerializer):
    repository = serializers.HiddenField(default=CurrentRepositoryDefault())

    class Meta:
        model = Object
        fields = (
            "id",
            "name",
            "comment",
            "status",
            "repository",
            "range_start",
            "range_end",
            "created_on",
            "modified_on",
            "lock",
        )
        read_only_fields = (
            "created_on",
            "modified_on",
            "status"
        )
        list_serializer_class = ListObjectSerializer

