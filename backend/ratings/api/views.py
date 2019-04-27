from ..models import Rating
from movies.models import Movie
from ..lib.utils import recommendations
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
    RatingListSerializer,
    # RatingCreateSerializer,
    # PostDetailSerializer,
    # PostUpdateSerializer,
    # PostDeleteSerializer
)

class RatingListAPIView(generics.ListAPIView):
  queryset = Rating.objects.all()
  serializer_class = RatingListSerializer
  permission_classes = [AllowAny]

class RecommendationView(views.APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    current_user_id = request.user.id
    movie_recommendations=recommendations(current_user_id)
    return Response({"movie_recommendations": movie_recommendations, "content": "Hello World!"})
# class RatingCreateAPIView(generics.CreateAPIView):
#   queryset = Rating.objects.all()
#   serializer_class = RatingCreateSerializer
#   permission_classes = [IsAuthenticated]