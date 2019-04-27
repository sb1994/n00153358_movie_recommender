from rest_framework import serializers
from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from comments.api.serializers import CommentListSerializer

from movies.models import Movie
from ..models import Rating

class RatingListSerializer(serializers.ModelSerializer):
  movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(),required=False, allow_null=True, default=None)
  user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False, allow_null=True, default=None)
  rating = serializers.CharField(max_length=255,help_text=('Required. 3-32 characters.'))
  class Meta:
    model = Rating
    fields = (
      'id',
      'rating',
      'movie_id',
      'user_id'
    )

# class CommentCreateSerializer(serializers.ModelSerializer):
#   comment = serializers.CharField(allow_blank=False)
#   movie_id = serializers.IntegerField(
#       required=True,
#       # help_text=_('Required. Id of the thread this post is created in')
#   )
#   # user_id = serializers.HyperlinkedRelatedField(
#   #     read_only=True,
#   #     view_name='user-detail',
#   #     lookup_field='user_id'
#   # )
#   user = serializers.HyperlinkedRelatedField(
#     read_only=True,
#     view_name='user-detail',
#     lookup_field='id'
#   )
#   class Meta:
#     model = Comment
#     fields = (
#         'id',
#         'comment',
#         'movie_id',
#         'created',
#         'user',
#     )
#     read_only_fields=('id', 'movie_id', 'created', 'user')

#   def create(self, validated_data):
#     comment = validated_data['comment']
#     movie_id = validated_data['movie_id']

#     # print(validated_data)
#     # # Get movie object
#     try:
#         movie = Movie.objects.get(id=movie_id)
#     except Movie.DoesNotExist:
#         raise serializers.ValidationError('Thread does not exist, please enter correct thread id')

#     # # Get the requesting user
#     user = None
#     request = self.context.get("request")
#     if request and hasattr(request, "user"):
#         user = request.user
#     else:
#         raise serializers.ValidationError('Must be authenticated to create post')

#     # Create the post
#     comment = Comment(
#         comment=comment,
#         movie=movie,
#         user=user
#     )
#     # print(comment)
#     # Update the thread last_activity to post creation time
#     comment.save()
#     return comment






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