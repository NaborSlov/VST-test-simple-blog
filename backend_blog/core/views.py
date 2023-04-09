from django.contrib.auth import logout
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from core.serializers import RegisterSerializer, AuthenticationSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    http_method_names = ['post']


class UserAuthenticationView(CreateAPIView):
    serializer_class = AuthenticationSerializer
    http_method_names = ['post']


class UserLogoutView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        """
        Выход из сессии
        """
        logout(request)
        return Response(status=status.HTTP_200_OK)
