from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.object import Object
from app.api.serializers.object import ObjectSerializer


class ObjectViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def _get_values(self, with_object_id=True):
        if with_object_id:
            return self.kwargs.get("repo_id"), self.kwargs.get("object_id")
        return self.kwargs.get("repo_id")

    def get_object(self):
        repo_id, object_id = self._get_values()

        return get_object_or_404(Object.objects.all(), id=object_id, repository=repo_id)

    def create(self, request, *args, **kwargs):
        repo_id = self._get_values(with_object_id=False)

        data = request.data | {
            "repository": repo_id
        }

        serializer = ObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        repo_id = self._get_values(with_object_id=False)
        instances = self.queryset.filter(repository=repo_id)
        serialized = ObjectSerializer(instances, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = ObjectSerializer(instance)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"response": "Object successfully deleted"}, status=status.HTTP_200_OK)
