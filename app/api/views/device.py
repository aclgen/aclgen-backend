from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.device import Device
from app.api.serializers.device import DeviceSerializer
from django.db.models import Q


class DeviceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_device(self):
        repo_id = self.kwargs["repo_id"]
        device_id = self.kwargs["dev_id"]
        print(f"RepoID: {repo_id}\nDeviceID: {device_id}")

        return get_object_or_404(Device.objects.all(), id=device_id, repository=repo_id)

    def list(self, request, *args, **kwargs):
        repo_id = self.kwargs.get('repo_id')
        print(f"REPO ID: {repo_id}")
        data = DeviceSerializer(self.queryset.filter(repository=repo_id), many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_device()
        serialized = DeviceSerializer(instance)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_device()
        instance.delete()
        return Response({"response": "Device successfully deleted"}, status=status.HTTP_200_OK)

