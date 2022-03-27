import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DummyTestViewSet(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"isDummy": "oh yes"}, status.HTTP_501_NOT_IMPLEMENTED)

    def post(self, request, *args, **kwargs):
        dummyvalue = request.data.get('dummy')

        return Response({"lol": dummyvalue}, status.HTTP_501_NOT_IMPLEMENTED)




