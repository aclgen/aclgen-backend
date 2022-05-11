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
            "repository",
            "name",
            "comment",
            "type",
            "lock",
            # COLLECTION
            "members",
            # IPV4
            "range_start",
            "range_end",
            # IPV6
            "ipv6_range_start",
            "ipv6_range_end",
            "created_on",
            "modified_on",
            "status",
        )
        read_only_fields = (
            "created_on",
            "modified_on",
            "status"
        )
        list_serializer_class = ListObjectSerializer

    def is_value_actually_empty(self, value):
        if isinstance(value, int):
            return False

        if value is None or value == "" or not value:
            return True

        return False

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        for field in self.Meta.fields:
            try:
                if self.is_value_actually_empty(rep[field]):
                    rep.pop(field)
            except KeyError:
                pass

        return rep
