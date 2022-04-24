from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from app.api.models.service import Service
from app.api.serializers.service import ServiceSerializer, BulkServiceSerializer
from app.api.models.repository import Repository
from app.util.validation import validate_uuids


class ServiceViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Service.objects.all()
    serializer_class = BulkServiceSerializer

    def get_queryset(self, ids=None):
        repository = self.kwargs.get("repo_id")
        service = self.kwargs.get("service_id")

        # print(f"Repository: {repository}")
        # print(f"Service: {service}")
        # print(f"IDs: {ids}")

        if repository and ids:
            return self.queryset.filter(repository=repository, id__in=ids)

        if repository and service:
            return self.queryset.filter(repository=repository, id=service)

        if repository:
            return self.queryset.filter(repository=repository)

        return self.queryset

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(ServiceViewSet, self).get_serializer(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.get_queryset())

    def create(self, request, *args, **kwargs):
        repository = Repository.objects.get(id=kwargs["repo_id"])

        if isinstance(request.data, list):
            for item in request.data:
                item["repository"] = repository
        else:
            print(request.data)
            raise ValidationError("Invalid input")

        return super(ServiceViewSet, self).create(request, *args, **kwargs)

    def update_bulk(self, request, *args, **kwargs):
        repository = Repository.objects.get(id=kwargs["repo_id"])

        ids = validate_uuids(request.data)

        if isinstance(request.data, list):
            for item in request.data:
                item["repository"] = repository
        else:
            raise ValidationError("Invalid input")

        instances = self.get_queryset(ids=ids)
        serializer = self.get_serializer(instances, data=request.data, partial=False, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        data = serializer.data
        return Response(data)

    def perform_update(self, serializer):
        serializer.save()



