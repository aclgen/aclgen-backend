from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from app.api.models.device import Device
from app.api.serializers.device import DeviceSerializer


class DeviceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        repository = self.kwargs.get("repo_id")
        device = self.kwargs.get("dev_id")

        if repository and device:
            return self.queryset.filter(repository=repository, id=device)

        if repository and not device:
            return self.queryset.filter(repository=repository)

        return self.queryset

    def get_object(self):
        return get_object_or_404(self.get_queryset())




