from rest_framework.generics import ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from blog.models import Blog, Comment
from blog.permissions import IsOwner
from blog.serializers import CommentSerializer, CommentDeleteUpdateSerializer, BlogListCreateSerializer, BlogSerializer


class ListCreateBlogView(ListCreateAPIView):
    serializer_class = BlogListCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.exclude(delete=True)


class UpdateDestroyBlogView(UpdateAPIView, DestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Blog.objects.exclude(delete=True)

    def perform_destroy(self, instance):
        instance.delete = True
        instance.save()
        return instance


class RetrieveBlogView(RetrieveAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.exclude(delete=True)


class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class UpdateRemoveCommentView(UpdateAPIView, DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    permission_classes = [IsOwner]
