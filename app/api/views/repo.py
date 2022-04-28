from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.repository import Repository
from app.api.serializers.repo import RepositorySerializer, FullRepositorySerializer


class RepositoryViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

    def get_queryset(self):
        repository = self.kwargs.get("id")

        if repository:
            return self.queryset.filter(id=repository)

        return self.queryset

    def get_object(self):
        return get_object_or_404(self.get_queryset())

    def retrieve_full(self, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        serialized = FullRepositorySerializer(instance)

        return Response(serialized.data, status=status.HTTP_200_OK)



