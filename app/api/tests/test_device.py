import pytest
import json
import uuid

from django.urls import reverse
from rest_framework import status
from app.api.models.repository import Repository
from app.api.models.device import Device


def str_uuid():
    return str(uuid.uuid4())


@pytest.fixture
def repository():
    return Repository.objects.create(
        name='Dummy Repository'
    )


@pytest.fixture
def repository_and_device_pair():
    repository = Repository.objects.create(
        name='Dummy Repository',
    )

    device = Device.objects.create(
        id=uuid.uuid4(),
        name='Test Device',
        comment='a dummy device',
        type='FIREWALL',
        repository=repository
    )

    return repository, device


@pytest.fixture
def dummy_device_data():
    return {
        "id": str_uuid(),
        "name": "Test Device",
        "comment": "a dummy device",
        "type": "FIREWALL"
    }


@pytest.mark.django_db
class TestDeviceCreate:
    def test_create_device(self, client, repository, dummy_device_data):
        url = reverse('devices', kwargs={
            "repo_id": repository.id
        })
        data = dummy_device_data

        response = client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
        )

        assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
class TestDeviceUpdate:
    def test_update_device(self, client, repository_and_device_pair):
        repository, device = repository_and_device_pair

        url = reverse('device', kwargs={
            "repo_id": repository.id,
            "dev_id": device.id
        })

        response = client.put(
            url,
            data={
                'id': device.id,
                'name': 'Updated Dummy Device',
                'comment': 'a comment',
                'type': 'FIREWALL',
            },
            content_type="application/json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Updated Dummy Device'
        assert response.data['type'] == 'FIREWALL'


@pytest.mark.django_db
class TestDeviceDelete:
    def test_delete_device(self, client, repository_and_device_pair):
        repository, device = repository_and_device_pair

        url = reverse('device', kwargs={
            "repo_id": repository.id,
            "dev_id": device.id
        })

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT

