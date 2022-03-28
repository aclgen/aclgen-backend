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


class ObjectDetailViewSet(APIView):
    def get_object(self, object_id):
        try:
            return Object.objects.get(id=object_id)
        except Object.DoesNotExist:
            return None

    def get(self, request, object_id, *args, **kwargs):
        instance = self.get_object(object_id)

        if not instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        serializer = ObjectSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, object_id, *args, **kwargs):
        instance = self.get_object(object_id)

        if not instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'defs': request.data.get('defs'),
        }

        serializer = ObjectSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, object_id, *args, **kwargs):
        instance = self.get_object(object_id)

        if not instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({}, status=status.HTTP_200_OK)

