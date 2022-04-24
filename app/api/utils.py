from django.utils import timezone


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

