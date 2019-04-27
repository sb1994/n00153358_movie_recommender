from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Rating(models.Model):
  movie = models.ForeignKey(Movie, related_name='ratings',on_delete=models.CASCADE)
  user = models.ForeignKey(User,related_name='ratings',on_delete=models.CASCADE)
  rating = models.TextField()
  def __self__(self):
    return self.rating