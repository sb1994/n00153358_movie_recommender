from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.response import Response
from ..models import (
  Movie
)
from django.contrib.auth.models import User
from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .serializers import (
  MovieSerializer,
  
)
from django.core.paginator import Paginator
from .pagination import(PostLimitOffsetPagination,PostPageNumberPagination)
class MovieListView(ListAPIView):
  permission_classes = [AllowAny]
  queryset = Movie.objects.all()
  serializer_class=MovieSerializer
  pagination_class = PostLimitOffsetPagination
class MovieDetailView(RetrieveAPIView):
  permission_classes = [AllowAny]
  lookup_field = "id"
  queryset = Movie.objects.all()
  serializer_class=MovieSerializer

