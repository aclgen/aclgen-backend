from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Object
from .serializers import ObjectSerializer


class ObjectViewSet(APIView):
    def get(self, request, *args, **kwargs):
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'defs': request.data.get('defs'),
        }

        serializer = ObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
