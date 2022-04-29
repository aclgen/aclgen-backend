from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from app.api.models.device import DeviceFolder
from app.api.serializers.folder import DeviceFolderSerializer


class DeviceFolderViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = DeviceFolder.objects.all()
    serializer_class = DeviceFolderSerializer

    def get_query(self):
        repository = self.kwargs.get("repo_id")
        device = self.kwargs.get("dev_id")
        folder = self.kwargs.get("folder_id")

        if repository and device and folder:
            return self.queryset.filter(repository=repository, device=device, id=folder)

        if repository and device:
            return self.queryset.filter(repository=repository, device=device)

        return self.queryset

    def get_object(self):
        return get_object_or_404(self.get_queryset())
