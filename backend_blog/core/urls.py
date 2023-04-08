from django.urls import path

from core.views import UserRegisterView, UserAuthenticationView, UserLogoutView

urlpatterns = [
    path('login/', UserAuthenticationView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('reg/', UserRegisterView.as_view(), name='register'),
]
