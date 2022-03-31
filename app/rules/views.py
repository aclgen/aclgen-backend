from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.rules.models import RuleSet, Rule
from app.rules.serializers import RuleSetSerializer, RuleSerializer


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


class RuleSetDetailViewSet(APIView):
    def get_object(self, object_id):
        try:
            return RuleSet.objects.get(id=object_id)
        except RuleSet.DoesNotExist:
            return None

    def delete(self, request, ruleset_id, *args, **kwargs):
        instance = self.get_object(ruleset_id)

        if not instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({}, status=status.HTTP_200_OK)


class RuleViewSet(APIView):
    def get(self, request, *args, **kwargs):
        objects = Rule.objects.all()
        serializer = RuleSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'comment': request.data.get('comment'),
            'ruleset': request.data.get('ruleset'),
            'source': request.data.get('source'),
            'destination': request.data.get('destination'),
            'service': request.data.get('service'),
            'direction': request.data.get('direction'),
            'action': request.data.get('action'),
        }

        serializer = RuleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)