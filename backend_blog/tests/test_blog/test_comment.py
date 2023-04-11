import pytest
from django.urls import reverse

from blog.models import Comment
from tests.factories import BlogFactory, CommentFactory


@pytest.mark.django_db
def test_create_comment(auth_client, user):
    blog = BlogFactory.create(user=user)
    response = auth_client.post(reverse("create_comment"),
                                data={
                                    "blog": blog.id,
                                    "description": "test create comment"
                                })

    response_expected = {
        "id": response.data.get("id"),
        "user": {
            "id": user.id,
            "username": user.username,
        },
        "description": "test create comment",
        "blog": blog.id,
        "created": response.data.get("created")
    }

    assert response.status_code == 201
    assert response.data == response_expected


@pytest.mark.django_db
def test_delete_comment(auth_client, user):
    blog = BlogFactory.create(user=user)
    comment = CommentFactory.create(user=user, blog=blog)

    response = auth_client.delete(reverse("comment", args=[comment.id]))

    assert response.status_code == 204
    assert Comment.objects.filter(id=comment.id).exists() is False
