import uuid
from rest_framework.exceptions import ValidationError


def validate_uuids(data, field="id", unique=True, version=4):
    if isinstance(data, list):
        uuids = [uuid.UUID(x[field], version=version) for x in data]

        if unique and len(uuids) != len(set(uuids)):
            raise ValidationError(f"Found multiple updates for a single {field} [uuid4]")

        return uuids

    return [data]


