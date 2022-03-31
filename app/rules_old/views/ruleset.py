from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.rules_old.models.ruleset import RuleSet
from app.rules_old.serializers.ruleset import RuleSetSerializer


class RuleSetViewSet(APIView):
    def get(self, request, *args, **kwargs):
        objects = RuleSet.objects.all()
        serializer = RuleSetSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'comment': request.data.get('comment')
        }

        serializer = RuleSetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)