import factory
from django.contrib.auth import get_user_model

from blog.models import Blog, Comment

User = get_user_model()


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = "test title blog"
    description = "test description"
    theme = "superPassword21"


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    description = "test description comment"
