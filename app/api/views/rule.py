from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.rules import Rule
from app.api.serializers.rule import RuleSerializer


class RuleViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def _get_value(self, key):
        return self.kwargs.get(key)

    def get_object(self):
        device_id = self._get_value("dev_id")
        rule_id = self._get_value("rule_id")

        return get_object_or_404(self.queryset, id=rule_id, device=device_id)

    def create(self, request, *args, **kwargs):
        device_id = self._get_value("dev_id")
        repo_id = self._get_value("repo_id")

        data = request.data | {
            "repository": repo_id,
            "device": device_id
        }

        serializer = RuleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        device_id = self._get_value("dev_id")

        instances = self.queryset.filter(device=device_id)
        serialized = RuleSerializer(instances, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = RuleSerializer(instance)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"response": "Rule successfully deleted"}, status=status.HTTP_200_OK)
