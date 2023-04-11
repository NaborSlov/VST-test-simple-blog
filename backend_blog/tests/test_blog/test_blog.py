import pytest
from django.urls import reverse

from blog.models import Blog
from blog.serializers import BlogListCreateSerializer, CommentSerializer
from tests.factories import BlogFactory, CommentFactory

test = {"id": 1,
        "user": {"id": 1,
                 "username": "testname"},
        "title": "test title blog",
        "description": "test description",
        "theme": "test theme",
        "created": "2023-04-11T19:45:25.170058+05:00",
        "author_name": "testname"}


@pytest.mark.django_db
def test_create(auth_client, user):
    response = auth_client.post(reverse("list_blogs"),
                                data={"title": "test title blog",
                                      "description": "test description",
                                      "theme": "test theme"})

    expected_response = {"id": response.data.get('id'),
                         "user": {
                             "id": user.id,
                             "username": user.username,
                         },
                         "title": "test title blog",
                         "description": "test description",
                         "theme": "test theme",
                         "created": response.data.get("created"),
                         "author_name": user.username}

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_get_list_blogs(auth_client, user):
    blogs = BlogFactory.create_batch(10, user=user, author_name=user.username)
    response = auth_client.get(reverse("list_blogs"))

    expected_response = {'count': 10,
                         'next': None,
                         'previous': None,
                         'results': BlogListCreateSerializer(instance=blogs, many=True).data}

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_get_list_delete_blogs(auth_client, user):
    blogs_is_active = BlogFactory.create_batch(7, user=user, author_name=user.username)
    blogs_not_active = BlogFactory.create_batch(3, user=user, author_name=user.username, delete=True)
    response = auth_client.get(reverse("list_blogs"))

    expected_response = {'count': 7,
                         'next': None,
                         'previous': None,
                         'results': BlogListCreateSerializer(instance=blogs_is_active, many=True).data}

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_get_one_blog_and_comments(auth_client, user):
    blog = BlogFactory.create(user=user)
    comments = CommentFactory.create_batch(5, user=user, blog=blog)
    response = auth_client.get(reverse("blog_retrieve", args=[blog.id]))

    expected_response = {"id": blog.id,
                         "comments": CommentSerializer(comments, many=True),
                         "user": {
                             "id": user.id,
                             "username": user.username,
                         },
                         "title": blog.title,
                         "description": blog.description,
                         "theme": blog.theme,
                         "created": blog.created,
                         "delete": False,
                         "author_name": user.username,
                         }

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_delete_blog(auth_client, user):
    blog = BlogFactory.create(user=user, delete=True)
    response = auth_client.get(reverse("blog_retrieve", args=[blog.id]))

    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_blog_by_id(auth_client, user):
    blog = BlogFactory.create(user=user)

    response = auth_client.delete(reverse("update_delete", args=[blog.id]))
    changed_blog = Blog.objects.get(id=blog.id)

    assert response.status_code == 204
    assert changed_blog.delete is True


@pytest.mark.django_db
def test_update_blog(auth_client, user):
    blog = BlogFactory.create(user=user)

    response = auth_client.patch(reverse("update_delete", args=[blog.id]),
                                 data={
                                     "title": "updated blog title",
                                     "description": "updated blog description",
                                     "theme": "updated blog theme"
                                 })

    expected_response = {"id": blog.id,
                         "comments": [],
                         "user": {
                             "id": user.id,
                             "username": user.username,
                         },
                         "title": "updated blog title",
                         "description": "updated blog description",
                         "theme": "updated blog theme",
                         "created": response.data.get("created"),
                         "delete": False,
                         "author_name": "",
                         }

    assert response.status_code == 200
    assert response.data == expected_response
