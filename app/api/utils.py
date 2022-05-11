from django.utils import timezone
from rest_framework.exceptions import ValidationError


def update_repository_modified_on(instances):
    """
    Updates the modified_on value for Repository when child items are created/updated.
    """
    if isinstance(instances, list):
        repository = instances[0].repository
        repository.modified_on = timezone.now()
        repository.save()


def update_device_modified_on(instances):
    """
    Updates the modified_on value for Device when child items are created/updated.
    """
    if isinstance(instances, list):
        device = instances[0].device
        device.modified_on = timezone.now()
        device.save()


def update_repository_modified_on_target(repository):
    if repository:
        repository.modified_on = timezone.now()
        repository.save()


def update_device_modified_on_target(device):
    if device:
        device.modified_on = timezone.now()
        device.save()


def validate_empty_fields(context, required_empty_fields=[]):
    for field in context.__dict__:
        if field in required_empty_fields and context.__dict__[field] is not None:
            raise ValidationError({
                "detail": f"{field} cannot have a value as it is a service type of {context.type}"
            })


def raise_validation_error_detail(error):
    raise ValidationError({"detail": error})
