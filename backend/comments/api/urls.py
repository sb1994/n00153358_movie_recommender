from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin

from .views import (
    CommentListAPIView,
    CommentCreateAPIView,
    # PostDetailAPIView,
    # PostUpdateAPIView,
    # PostDeleteAPIView
)

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comment-list'),
    path('create/', CommentCreateAPIView.as_view(), name='comment-create'),
    # path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    # path('<int:pk>/edit/', PostUpdateAPIView.as_view(), name='post-update'),
    # path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
]