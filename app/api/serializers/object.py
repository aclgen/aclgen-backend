from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from django.db import IntegrityError
from app.api.models.object import Object
from app.api.fields import CurrentRepositoryDefault
from app.api.utils import update_repository_modified_on
from app.common.serializers import BaseListSerializer


class ListObjectSerializer(BaseListSerializer):
    def update(self, instances, validated_data):
        instance_hash = {index: instance for index, instance in enumerate(instances)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]

        writable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields
            if x != "id"
        ]

        if "modified_on" in self.child.Meta.fields:
            writable_fields += ["modified_on"]
            modified_on = timezone.now()
            for instance in result:
                instance.modified_on = modified_on

        try:
            self.child.Meta.model.objects.bulk_update(result, writable_fields)
        except IntegrityError as e:
            raise ValidationError(e)

        update_repository_modified_on(result)

        return result


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
        )
        read_only_fields = (
            "created_on",
            "modified_on",
            "status"
        )
        list_serializer_class = ListObjectSerializer

