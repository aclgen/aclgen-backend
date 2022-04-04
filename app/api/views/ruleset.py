from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.rules import RuleSet
from app.api.serializers.ruleset import RuleSetSerializer


class RuleSetViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = RuleSet.objects.all()
    serializer_class = RuleSetSerializer

    def get_values(self, with_ruleset_id=True):
        if with_ruleset_id:
            return self.kwargs["repo_id"], self.kwargs["dev_id"], self.kwargs["ruleset_id"]
        return self.kwargs["repo_id"], self.kwargs["dev_id"]

    def get_ruleset(self):
        repo_id, dev_id, ruleset_id = self.get_values()

        print(f"RepoID: {repo_id}\nDeviceID: {dev_id}\nRuleSetID: {ruleset_id}")

        return get_object_or_404(self.queryset, id=ruleset_id, repository=repo_id, device=dev_id)

    def list(self, request, *args, **kwargs):
        repo_id, dev_id = self.get_values(with_ruleset_id=False)
        instances = self.queryset.filter(repository=repo_id, device=dev_id)
        serialized = RuleSetSerializer(instances, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_ruleset()
        serialized = RuleSetSerializer(instance)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        repo_id, dev_id = self.get_values(with_ruleset_id=False)
        data = request.data | {
            "repository": repo_id,
            "device": dev_id
        }

        serializer = RuleSetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_ruleset()
        instance.delete()
        return Response({"response": "RuleSet successfully deleted"}, status=status.HTTP_200_OK)

