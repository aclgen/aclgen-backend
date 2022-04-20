from rest_framework.exceptions import ValidationError
import uuid


def validate_ids(data, field="id", unique=True):
    if isinstance(data, list):
        ids = [int(x[field]) for x in data]

        if unique and len(ids) != len(set(ids)):
            raise ValidationError(f"Found multiple updates for a single {field}")

        return ids

    return [data]


def _validate_uuid(test_value, version=4):
    try:
        return uuid.UUID(test_value, version=version).__str__()
    except ValueError:
        raise ValidationError("Invalid UUID inputs")


def validate_uuids(data, field="id", unique=True):
    if isinstance(data, list):
        uuids = [_validate_uuid(x[field]) for x in data]

        if unique and len(uuids) != len(set(uuids)):
            print(uuids)
            print(set(uuids))
            print(data)
            print(f"len: {len(uuids)} vs len-set {len(set(uuids))}")
            raise ValidationError(f"Found multiple updates for a single {field} [uuid4]")

        return uuids

    return [data]


