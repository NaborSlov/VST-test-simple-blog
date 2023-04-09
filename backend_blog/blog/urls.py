from django.urls import path

from blog.views import CreateCommentView, ListCreateBlogView, UpdateRemoveCommentView, RetrieveBlogView, \
    UpdateDestroyBlogView

urlpatterns = [
    path('blogs/', ListCreateBlogView.as_view(), name='list_blogs'),
    path('blogs/<int:pk>/', RetrieveBlogView.as_view(), name='blog_retrieve'),
    path('blogs/update/<int:pk>/', UpdateDestroyBlogView.as_view(), name='update_delete'),
    path('comment/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/', UpdateRemoveCommentView.as_view(), name='comment'),
]
