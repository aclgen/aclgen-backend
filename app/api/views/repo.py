from rest_framework import status, viewsets, mixins
from rest_framework.generics import get_object_or_404
from app.api.models.repository import Repository
from app.api.serializers.repo import RepositorySerializer


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
    lookup_field = "id"

    def get_repo(self):
        repository_id = self.kwargs["repository_id"]
        return get_object_or_404(Repository.objects.all(), id=repository_id)



