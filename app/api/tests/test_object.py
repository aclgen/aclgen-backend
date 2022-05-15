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
def dummy_object_data():
    return {
        "id": str_uuid(),
        "name": "Local Network",
        "comment": "a local network",
        "range_start": "192.168.1.1",
        "range_end": "192.168.254",
        "type": "IPV4",
        "lock": "UNLOCKED"
    }


@pytest.mark.django_db
def test_create_update_delete_service(client, repository, dummy_object_data):
    # Create the Object

    url = reverse('objects', kwargs={
        "repo_id": repository.id
    })
    data = dummy_object_data

    response = client.post(
        url,
        data=json.dumps(data),
        content_type="application/json"
    )

    assert response.status_code == status.HTTP_201_CREATED

    # Update the Object
    object_id = response.data["id"]

    url = reverse('object', kwargs={
        "repo_id": repository.id,
        "object_id": object_id,
    })

    response = client.put(
        url,
        data={
            "id": object_id,
            "name": "Local Network 2",
            "comment": "a local network i think",
            "range_start": "10.0.1.1",
            "range_end": "10.0.1.254",
            "type": "IPV4",
            "lock": "UNLOCKED"
        },
        content_type="application/json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Local Network 2'
    assert response.data['range_start'] == '10.0.1.1'

    # Delete the Object
    url = reverse('object', kwargs={
        "repo_id": repository.id,
        "object_id": object_id,
    })

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
