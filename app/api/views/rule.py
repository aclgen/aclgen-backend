from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from app.api.models.rules import Rule
from app.api.serializers.rule import RuleSerializer


class RuleViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def get_queryset(self):
        repository = self.kwargs.get("repo_id")
        device = self.kwargs.get("dev_id")
        rule = self.kwargs.get("rule_id")

        if repository and device and rule:
            return self.queryset.filter(repository=repository, device=device, id=rule)

        if repository and device:
            return self.queryset.filter(repository=repository, device=device)

        return self.queryset

    def get_object(self):
        return get_object_or_404(self.get_queryset())


