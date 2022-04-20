from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from django.utils import timezone
from app.api.models.service import Service
from app.api.fields import CurrentRepositoryDefault, ModelObjectIdField


class ServiceSerializer(serializers.ModelSerializer):
    repository = serializers.HiddenField(default=CurrentRepositoryDefault())

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


class BulkServiceCreateUpdateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        # Update repository last modified value here

        return result

    def update(self, instances, validated_data):
        instance_hash = {index: instance for index, instance in enumerate(instances)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]

        print(result)

        writable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields + ("repository",)
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

        return result


def update_repository_modified_on(instances):
    if isinstance(instances, list):
        repository = instances[0].repository
        repository.modified_on = timezone.now()
        repository.save()


class BulkServiceSerializer(serializers.ModelSerializer):
    repository = ModelObjectIdField()

    def create(self, validated_data):
        instance = Service(**validated_data)

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.port_start = validated_data["port_start"]
        instance.port_end = validated_data["port_end"]
        instance.protocol = validated_data["protocol"]

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

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
        list_serializer_class = BulkServiceCreateUpdateSerializer


