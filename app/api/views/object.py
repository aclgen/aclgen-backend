from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.object import Object
from app.api.models.repository import Repository
from app.api.serializers.object import ObjectSerializer
from app.util.validation import validate_uuids


class ObjectViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self, ids=None):
        repository = self.kwargs.get("repo_id")
        object_id = self.kwargs.get("object_id")

        if repository and ids:
            print(self.queryset.filter(repository=repository, id__in=ids))
            return self.queryset.filter(repository=repository, id__in=ids)

        if repository and object_id:
            return self.queryset.filter(repository=repository, id=object_id)

        if repository:
            return self.queryset.filter(repository=repository)

        return self.queryset

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True

        return super(ObjectViewSet, self).get_serializer(*args, **kwargs)

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
            return Response(data)
        else:
            return super(ObjectViewSet, self).update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()
