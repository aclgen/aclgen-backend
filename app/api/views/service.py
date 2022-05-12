from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
from app.api.models.service import Service
from app.api.serializers.service import ServiceSerializer
from app.api.models.repository import Repository
from app.util.validation import validate_uuids
from app.api.enums import ServiceType


class ServiceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self, ids=None):
        repository = self.kwargs.get("repo_id")
        service = self.kwargs.get("service_id")

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

    def get_serializer_class(self):
        return self.serializer_class

    def get_object(self):
        return get_object_or_404(self.get_queryset())

    def update(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            repository = Repository.objects.get(id=kwargs["repo_id"])
            ids = validate_uuids(request.data)

            for item in request.data:
                item["repository"] = repository

            instances = self.get_queryset(ids=ids)
            serializer = self.get_serializer(instances, data=request.data, partial=False, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            data = serializer.data
            # Workaround for updating ManyToMany fields in bulk
            #self.perform_update_m2m_members(data=request.data)

            return Response(data)
        else:
            return super(ServiceViewSet, self).update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def perform_update_m2m_members(self, data):
        errors = []

        for item in data:
            service_type = item.get("type")

            if service_type == ServiceType.COLLECTION:
                try:
                    members = item.get("members")
                    if members is not None:
                        instance = Service.objects.get(id=item["id"])
                        instance.members.clear()
                        for member in members:
                            instance.members.add(member)

                    errors.append({})
                except IntegrityError as e:
                    errors.append({"members": f"Invalid or non-existing member provided for Service with ID {item['id']}"})

        if any(errors):
            raise ValidationError(errors)
