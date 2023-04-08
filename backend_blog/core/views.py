from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import RegisterSerializer, AuthenticationSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserAuthenticationView(CreateAPIView):
    serializer_class = AuthenticationSerializer


class UserLogoutView(APIView):
    http_method_names = ['delete']

    def delete(self, request, *args, **kwargs):
        """
        Выход из сессии
        """
        logout(request)
        return Response(status=status.HTTP_200_OK)
