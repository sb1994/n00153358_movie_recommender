from rest_framework import serializers
from accounts.api.serializers import UserSerializer
from comments.api.serializers import CommentListSerializer

from ..models import (
  Movie
)

class MovieSerializer(serializers.ModelSerializer):
  # comments = serializers.RelatedField(many=True) ##gets comment id
  # comments = serializers.StringRelatedField(many= True) ##gives (Comment Related Object) As response
  # comments = serializers.PrimaryKeyRelatedField(many= True,read_only=True) ##gets comment id
  # comments = serializers.SerializerMethodField(source = 'comment', many=True) ##gets comment id
  # comments = serializers.SerializerMethodField()
  comments = CommentListSerializer(many=True)

  class Meta:
    model=Movie
    # fields = ('backdrop_path','title','budget','tmdb_id','orginal_title','overview','poster_path','popularity','status','release_date','runtime','tagline','video','vote_count','vote_average','')
    fields = ('id','backdrop_path','title','budget','tmdb_id','orginal_title','overview','poster_path','popularity','status','release_date','runtime','tagline','video','vote_count','vote_average','comments')
    # depth=1










# class MovieCommentSerializer(serializers.ModelSerializer):
#   user = UserSerializer(queryset=User.objects.all(),required=False, allow_null=True, default=None)
#   # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False, allow_null=True, default=None)
#   comment = serializers.CharField(
#     max_length=255,
#     help_text=(
#       'Required. 3-32 characters.'
#     ),
#   )
#   comment = serializers.CharField(
#     max_length=255,
#     help_text=(
#       'Required. 3-32 characters.'
#     ),
#   )
#   movie_id = serializers.CharField(
#     max_length=255,
#     help_text=(
#       'Required. 3-32 characters.'
#     ),
#   )
#   # movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(),required=False, allow_null=True, default=None )
#   class Meta:
#     model=Comment
#     fields = ('id','comment','movie_id','created','user_id')  
#     # extra_kwargs = {'user_id': {'default': serializers.CurrentUserDefault()}}
  



  # def create(self,validated_data):
  #   user_id = validated_data.pop('user_id')
  #   # user = validated_data.pop('user')
  #   movie_id = validated_data.pop('movie_id')
  #   comment = validated_data.pop('comment')

  #   comment_object = Comment.objects.create(comment = comment, movie_id = movie_id,user_id =user_id,)
  #   # comment_object.user = validated_data.pop('user')
  #   # user = self.request.user
  #   # print(user)

  #   return comment_object