from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework.validators import UniqueValidator
# from django.contrib.humanize.templatetags.humanize import naturaltime
from ..models import UserProfile


class UserSerializer(serializers.ModelSerializer):
  bio = serializers.CharField(source='profile.bio')
  avatar = serializers.CharField(source='profile.avatar')
  status = serializers.URLField(source='profile.status')
  name = serializers.CharField(source='profile.name')
  class Meta:
    model = User
    fields = [
      'username',
      'name',
      'bio',
      'avatar',
      'status',
      'is_staff',
      'date_joined'
    ]

class UserDetailSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='profile.bio')
    avatar = serializers.URLField(source='profile.avatar')
    status = serializers.URLField(source='profile.status')
    name = serializers.CharField(source='profile.name')
    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'bio',
            'avatar',
            'status',
            'is_staff',
        ]
        lookup_field = 'id'
class UserCreateSerializer(serializers.ModelSerializer):
  username = serializers.CharField(
    min_length=3,
    max_length=50,
    help_text=_(
        'Required. 4-32 characters. Letters, numbers, underscores or hyphens only.'
    ),
    validators=[UniqueValidator(
        queryset=User.objects.all(),
        message='is already been taken by another user'
    )],
    required=True
  )
  password = serializers.CharField(
      min_length=3,
      max_length=32,
      write_only=True,
      help_text=_(
          'Required. 3-32 characters.'
      ),
      required=True
  )
  email = serializers.EmailField(
      required=True,
      validators=[UniqueValidator(
          queryset=User.objects.all(),
          message='is already been taken by another user'
      )]
  )
  bio = serializers.CharField(source='profile.bio', allow_blank=True, default='')
  name = serializers.CharField(
      source='profile.name',
      allow_blank=True,
      default='',
      max_length=32
  )
  avatar = serializers.URLField(source='profile.avatar', allow_blank=True, default='')
  status = serializers.CharField(
    source='profile.status',
    allow_blank=True,
    max_length=16,
    min_length=0,
    default=''
  )
  fav_quote = serializers.CharField(
    source='profile.fav_quote',
    allow_blank=True,
    max_length=100,
    min_length=0,
    default=''
  )
  class Meta:
    model = User
    fields = (
        'username',
        'name',
        'email',
        'password',
        'bio',
        'avatar',
        'status',
        'fav_quote'
    )

  def create(self, validated_data):
    profile_data = validated_data.pop('profile', None)
    username = validated_data['username']
    email = validated_data['email']
    password = validated_data['password']
    user = User(
      username = username,
      email = email
    )
    user.set_password(password)
    user.save()

    avatar = profile_data.get('avatar') or None
    if not avatar:
      avatar = 'https://dummyimage.com/600x400/000/fff'
    profile = UserProfile(
      user = user,
      bio = profile_data.get('bio', ''),
      avatar = avatar,
      name = profile_data.get('name', ''),
      status = profile_data.get('status', 'Member'),
      fav_quote = profile_data.get('fav_quote', '')
    )
    profile.save()
    return user
class UserTokenSerializer(serializers.Serializer):
  username = serializers.CharField(label=_("Username"))
  password = serializers.CharField(
      label=_("Password"),
      style={'input_type': 'password'},
      trim_whitespace=False
  )

  def validate(self, attrs):
    username = attrs.get('username')
    password = attrs.get('password')

    if username and password:
      user = authenticate(request=self.context.get('request'), username=username, password=password)

      # The authenticate call simply returns None for is_active=False
      # users. (Assuming the default ModelBackend authentication
      # backend.)
      if not user:
        msg = _('Unable to log in with provided credentials.')
        raise serializers.ValidationError(msg, code='authorization')
    else:
      msg = _('All credencials must be included')
      raise serializers.ValidationError(msg, code='authorization')

    attrs['user'] = user
    return attrs

class UserLoginSerializer(serializers.ModelSerializer):
  username = serializers.CharField(
    max_length=32,
    help_text=_(
        'Required. 32 characters or fewer. Letters, numbers, underscores or hyphens only.'
    ),
    required=True
  )
  token = serializers.CharField(allow_blank=True, read_only=True)
  name = serializers.CharField(source='profile.name', read_only=True)
  class Meta:
    model = User
    fields = [
      'username',
      'name',
      'password',
      'token',
    ]
    extra_kwargs = {"password": {"write_only": True} }
