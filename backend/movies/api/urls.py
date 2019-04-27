from django.urls import path,include

from .views import (
  MovieListView,
  MovieDetailView
)

urlpatterns =[
  path('',MovieListView.as_view()),
  path('<id>',MovieDetailView.as_view(),name='movie-detail'),
]