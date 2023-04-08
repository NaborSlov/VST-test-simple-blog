from django.urls import path

from blog.views import CreateCommentView, ListCreateBlogView, UpdateRemoveCommentView, RetrieveUpdateDestroyBlogView

urlpatterns = [
    path('blogs/', ListCreateBlogView.as_view(), name='list_blogs'),
    path('blogs/<int:pk>/', RetrieveUpdateDestroyBlogView.as_view(), name='blog'),
    path('comment/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/', UpdateRemoveCommentView.as_view(), name='comment'),
]
