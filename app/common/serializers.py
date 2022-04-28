from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import ObjectDoesNotExist


class BaseListSerializer(serializers.ListSerializer):
    def update(self, instances, validated_data):
        return super(BaseListSerializer, self).update(instances, validated_data)

    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise ValidationError("The data does not match requires type (must be a list)")

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

