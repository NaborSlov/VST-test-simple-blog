from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

USER = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = USER
        fields = ['id', 'username', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')

        if attrs.get('password') != confirm_password:
            raise ValidationError({'confirm_password': 'пароли должны быть одинаковые'})

        return attrs

    def create(self, validated_data):
        instance = USER.objects.create_user(**validated_data)

        request = self.context["request"]
        login(request, instance)

        return instance


class AuthenticationSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = USER
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Авторизация пользователя
        """
        user = authenticate(username=validated_data.get('username'),
                            password=validated_data.get('password'))
        if not user:
            raise ValidationError({"username": "Неправильный логин или пароль"})

        request = self.context["request"]
        login(request, user)

        return user
