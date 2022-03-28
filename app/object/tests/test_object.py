from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Object


class ObjectCreationTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.object_url = reverse('object')

    def test_object_creation_endpoint_with_valid_data(self):
        # Data
        data = {
            'name': 'Test Object',
            'description': 'Test Object that represents an IP address',
            'defs': ["127.0.0.1/32"],
        }

        # Perform the request
        response = self.client.post(self.object_url, data)

        # Handle request response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Object.objects.count(), 1)



