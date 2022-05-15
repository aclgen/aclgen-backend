import pytest
import json
import uuid

from django.urls import reverse
from rest_framework import status
from app.api.models.repository import Repository


def str_uuid():
    return str(uuid.uuid4())


@pytest.fixture
def repository():
    return Repository.objects.create(
        name='Dummy Repository'
    )


@pytest.fixture
def dummy_service_data():
    return {
        "id": str_uuid(),
        "name": "SSH",
        "comment": "Secure Shell",
        "port_start": 22,
        "port_end": 22,
        "protocol": "TCP",
        "type": "PORT",
        "lock": "UNLOCKED"
    }


@pytest.mark.django_db
def test_create_service(client, repository, dummy_service_data):
    url = reverse('services', kwargs={
        "repo_id": repository.id
    })
    data = dummy_service_data

    response = client.post(
        url,
        data=json.dumps(data),
        content_type="application/json"
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_update_delete_service(client, repository, dummy_service_data):
    # Create the Service

    url = reverse('services', kwargs={
        "repo_id": repository.id
    })
    data = dummy_service_data

    response = client.post(
        url,
        data=json.dumps(data),
        content_type="application/json"
    )

    assert response.status_code == status.HTTP_201_CREATED

    # Update the Service
    service = response.data["id"]

    url = reverse('service', kwargs={
        "repo_id": repository.id,
        "service_id": service
    })

    response = client.put(
        url,
        data={
            "id": service,
            "name": "SSH Updated",
            "comment": "Secure Shell",
            "port_start": 22,
            "port_end": 22,
            "protocol": "TCP",
            "type": "PORT",
            "lock": "UNLOCKED"
        },
        content_type="application/json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'SSH Updated'

    # Delete the Service
    url = reverse('service', kwargs={
        "repo_id": repository.id,
        "service_id": service
    })

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


