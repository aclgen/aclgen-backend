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

    def get_queryset(self):
        repository = self.kwargs.get("repo_id")
        service = self.kwargs.get("service_id")

        if repository and service:
            return self.queryset.filter(repository=repository, id=service)

        if repository and not service:
            return self.queryset.filter(repository=repository)

        return self.queryset

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(ServiceViewSet, self).get_serializer(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.get_queryset())





