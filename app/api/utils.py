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


def raise_validation_error_detail(error):
    raise ValidationError({"detail": error})


def validate_empty_fields(context, required_empty_fields=[]):
    #print(f"{context.id} START -----")
    #print(context.__dict__)
    #print(f"{context.id} END ----")

    # TODO: Different approach could be in the save() method in the models, to just set all fields that need to be empty to None

    for field in context.__dict__:
        if field in required_empty_fields and context.__dict__[field] is not None:
            print(f"ERROR: {context.id}: {field} had value {context.__dict__[field]} ???")
            raise_validation_error_detail(f"{field} cannot have a value as it is a service type of {context.type}")

    if "members" in required_empty_fields:
        if context.members.count() > 0:
            context.members.clear()
            # TODO: Could also just not raise ValidationError and just clear the members...
            raise_validation_error_detail(f"service of type {context.type} cannot have"
                                          f" members (found {context.members.count()} members)")

