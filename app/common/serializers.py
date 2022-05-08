from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist
from django.utils import timezone
from django.db import IntegrityError


class BaseListSerializer(serializers.ListSerializer):
    def to_internal_value(self, data):
        print(data)

        if not isinstance(data, list):
            raise ValidationError("The data does not match required type (must be a list)")

        result = []
        errors = []

        for item in data:
            try:
                self.child.instance = self.instance.get(id=item['id']) if self.instance else None
                self.child.initial_data = item
                validated = self.child.run_validation(item)
            except ObjectDoesNotExist:
                errors.append(f"Item {item['id']} does not exist")
            except ValidationError as e:
                errors.append(e.detail)
            else:
                result.append(validated)
                errors.append({})

        if any(errors):
            raise ValidationError(errors)

        return result

    def update_parent_modified_on(self, result=None):
        pass

    def update(self, instances, validated_data):
        if instances.count() <= 0:
            """
            Handles how we respond to all UUIDs being invalid
            """
            raise ValidationError({"detail": "No items matching your query"})

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

        self.update_parent_modified_on(result)

        return result

