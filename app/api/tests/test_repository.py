import pytest
import json

from django.urls import reverse
from rest_framework import status
from app.api.models.repository import Repository
from app.api.serializers.repo import RepositorySerializer


@pytest.fixture
def dummy_repository_data():
    return {
        'name': 'Test Repository'
    }


@pytest.mark.django_db
class TestRepositoryCreate:
    def test_create_repository(self, client, dummy_repository_data):
        url = reverse('repositories')
        data = dummy_repository_data

        response = client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
class TestRepositoryList:
    def test_list_repositories(self, client):
        url = reverse('repositories')
        response = client.get(url)

        repositories = Repository.objects.all()
        expected_data = RepositorySerializer(repositories, many=True).data

        assert response.status_code == 200
        assert response.data == expected_data



