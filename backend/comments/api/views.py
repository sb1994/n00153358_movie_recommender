from comments.models import Comment
from movies.models import Movie
from rest_framework import generics, views
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
# from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

from .serializers import (
    CommentListSerializer,
    CommentCreateSerializer,
    # PostDetailSerializer,
    # PostUpdateSerializer,
    # PostDeleteSerializer
)

class CommentListAPIView(generics.ListAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentListSerializer
  permission_classes = [AllowAny]
class CommentCreateAPIView(generics.CreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentCreateSerializer
  permission_classes = [AllowAny]


