from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from app.service.models import Folder, Service
from app.service.serializers import FolderSerializer, ServiceSerializer


class FolderViewSet(APIView):
    def get(self, request, *args, **kwargs):
        objects = Folder.objects.all()
        serializer = FolderSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'parent_folder': request.data.get('parent_folder')
        }

        serializer = FolderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FolderDetailViewSet(APIView):
    def get_object(self, object_id):
        try:
            return Folder.objects.get(id=object_id)
        except Folder.DoesNotExist:
            return None

    def get(self, request, folder_id, *args, **kwargs):
        instance = self.get_object(folder_id)

        if not instance:
            return Response({"response": "Folder does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FolderSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, folder_id, *args, **kwargs):
        instance = self.get_object(folder_id)

        if not instance:
            return Response({"response": "Folder does not exist"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'name': request.data.get('name'),
            'parent_folder': request.data.get('parent_folder')
        }

        serializer = FolderSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, folder_id, *args, **kwargs):
        instance = self.get_object(folder_id)

        if not instance:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"response": "Folder successfully deleted"}, status=status.HTTP_200_OK)


class ServiceViewSetNew(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'comment': request.data.get('comment'),
            'port_start': request.data.get('port_start'),
            'port_end': request.data.get('port_end'),
            'protocol': request.data.get('protocol'),
        }

        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceViewSet(APIView):
    def get(self, request, *args, **kwargs):
        objects = Service.objects.all()
        serializer = ServiceSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'comment': request.data.get('comment'),
            'port_start': request.data.get('port_start'),
            'port_end': request.data.get('port_end'),
            'protocol': request.data.get('protocol'),
        }

        serializer = ServiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)