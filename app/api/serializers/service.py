from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
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
            "status",
            "repository",
            "created_on",
            "modified_on",
        ]


class BulkServiceCreateUpdateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result

    def update(self, instances, validated_data):
        instance_hash = {index: instance for index, instance in enumerate(instances)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]

        writeable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields + ("repository",)
        ]

        if "modified_on" in self.child.Meta.fields:
            writeable_fields += ["modified_on"]
            modified_on = timezone.now()
            for instance in result:
                instance.modified_on = modified_on

        try:
            self.child.Meta.model.objects.bulk_update(result, writeable_fields)
        except IntegrityError as e:
            raise ValidationError(e)

        return result


class BulkServiceSerializer(serializers.ModelSerializer):
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
        read_only_fields = [
            "created_on",
            "modified_on",
        ]
        list_serializer_class = BulkServiceCreateUpdateListSerializer

