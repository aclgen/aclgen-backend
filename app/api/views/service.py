from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.service import Service
from app.api.serializers.service import ServiceSerializer


class ServiceViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def _get_values(self, with_service_id=True):
        if with_service_id:
            return self.kwargs.get("repo_id"), self.kwargs.get("service_id")
        return self.kwargs.get("repo_id")

    def get_object(self):
        repo_id, service_id = self._get_values()
        return get_object_or_404(self.queryset, id=service_id, repository=repo_id)

    def create(self, request, *args, **kwargs):
        repo_id = self._get_values(with_service_id=False)

        data = request.data | {
            "repository": repo_id
        }

        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        repo_id = self._get_values(with_service_id=False)
        instances = self.queryset.filter(repository=repo_id)
        serialized = ServiceSerializer(instances, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)




