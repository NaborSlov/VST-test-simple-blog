import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from tests import factories


@pytest.fixture
def user(db):
    User = get_user_model()

    user = User.objects.create_user(
        username="testname",
        password="testSuper1Password"
    )
    return user


@pytest.fixture
def other_user(db):
    User = get_user_model()

    user = User.objects.create_user(
        username="other_user",
        password="other_Password"
    )
    return user


@pytest.fixture
def auth_client(user):
    client = APIClient()
    client.login(username="testname", password="testSuper1Password")
    return client
