from rest_framework import serializers

from blog.models import Blog, Comment
from core.serializers import RetrieveUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        current_user = validated_data.pop("current_user")
        instance = Comment.objects.create(**validated_data, user=current_user)
        return instance


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description']


class BlogListCreateSerializer(serializers.ModelSerializer):
    current_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = Blog
        exclude = ['delete']
        extra_kwargs = {"author_name": {"read_only": True}}

    def create(self, validated_data):
        current_user = validated_data.pop("current_user")
        instance = Blog.objects.create(**validated_data, user=current_user, author_name=current_user.username)
        return instance


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = RetrieveUserSerializer()

    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True},
                        "delete": {"read_only": True}}
