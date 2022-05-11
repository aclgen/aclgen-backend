from rest_framework import serializers
from app.api.models.service import Service
from app.api.fields import CurrentRepositoryDefault
from app.api.utils import update_repository_modified_on
from app.common.serializers import BaseListSerializer


# TODO: Fix M2M bulk update for "members" - ValueError: bulk_update() can only be used with concrete fields.
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
            "repository",
            "name",
            "comment",
            "type",
            "lock",
            "members",
            "icmp_type",
            "icmp_code",
            "port_start",
            "port_end",
            "protocol",
            "created_on",
            "modified_on",
            "status",
        )
        read_only_fields = (
            "created_on",
            "modified_on",
            "status",
        )
        m2m_fields = (
            "members"
        )
        list_serializer_class = ListServiceSerializer

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

