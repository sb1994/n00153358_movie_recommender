from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Comment(models.Model):
  movie = models.ForeignKey(Movie, related_name='comments',on_delete=models.CASCADE)
  user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
  comment = models.TextField()
  created = models.DateTimeField(auto_now_add=True, blank=True)
  def __self__(self):
    return self.comment