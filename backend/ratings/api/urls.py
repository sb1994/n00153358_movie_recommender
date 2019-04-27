from django.urls import path,include

from .views import (
  RatingListAPIView,
  RecommendationView
)

urlpatterns =[
  path('',RatingListAPIView.as_view()),
  path('recommendation',RecommendationView.as_view()),
  
]