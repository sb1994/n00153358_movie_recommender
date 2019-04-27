from rest_framework import serializers
from django.contrib.auth.models import User
from comments.models import Comment
from movies.models import Movie
from accounts.api.serializers import UserSerializer

class CommentListSerializer(serializers.ModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='movie-detail',
        lookup_field='id'
    )
    # user = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail',
    #     lookup_field='id'
    # )
    user= UserSerializer()
    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
            'movie',
            'created',
            'user'
        )

class CommentCreateSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(allow_blank=False)
    movie_id = serializers.IntegerField(
        required=True,
        # help_text=_('Required. Id of the thread this post is created in')
    )
    # user_id = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail',
    #     lookup_field='user_id'
    # )
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail',
        lookup_field='id'
    )
    class Meta:
        model = Comment
        fields = (
            'id',
            'comment',
            'movie_id',
            'created',
            'user',
        )
        read_only_fields=('id', 'movie_id', 'created', 'user')

    def create(self, validated_data):
        comment = validated_data['comment']
        movie_id = validated_data['movie_id']

        # print(validated_data)
        # # Get movie object
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Thread does not exist, please enter correct thread id')

        # # Get the requesting user
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        else:
            raise serializers.ValidationError('Must be authenticated to create post')

        # Create the post
        comment = Comment(
            comment=comment,
            movie=movie,
            user=user
        )
        # print(comment)
        # Update the thread last_activity to post creation time
        comment.save()
        return comment