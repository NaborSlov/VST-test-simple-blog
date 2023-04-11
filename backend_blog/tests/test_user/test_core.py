import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create(client):
    response = client.post(reverse("register"),
                           data={"username": "newtestuser",
                                 "password": "super1Password",
                                 "confirm_password": "super1Password"})

    expected_response = {"id": response.data.get("id"),
                         "username": "newtestuser"}

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_login(client, user):
    response = client.post(reverse("login"),
                           data=json.dumps({"username": "testname",
                                            "password": "testSuper1Password"}),
                           content_type="application/json")

    assert response.status_code == 201


@pytest.mark.django_db
def test_logout(auth_client):
    response = auth_client.delete(reverse("logout"))
    assert response.status_code == 200

