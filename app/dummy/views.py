from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DummyTestViewSet(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"isDummy": "oh yes"}, status.HTTP_501_NOT_IMPLEMENTED)


