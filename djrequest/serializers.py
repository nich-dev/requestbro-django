# Serializers define the API representation.]
import models
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSimpleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username',)
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Song
        fields = ('url', 'title', 'soundcloud_link', 'youtube_link',
                  'spotify_link', 'playmusic_link', 'verified', 'requests',
                  'genre')


class SongRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SongRequest
        fields = ('url', 'user', 'song', 'complete', 'note', 'points')


class SongRequestDetailedSerializer(serializers.HyperlinkedModelSerializer):
    song = SongSerializer(many=True, read_only=True)

    class Meta:
        model = models.SongRequest
        fields = ('url', 'user', 'song', 'complete', 'note', 'points')


class UserPrefsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)
    banned_users = serializers.StringRelatedField(many=True)
    following_users = serializers.StringRelatedField(many=True)
    mod_users = serializers.StringRelatedField(many=True)
    banned_songs_by_word = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.UserPrefs
        fields = ('url', 'user', 'default_link', 'logo',
                  'banned_users', 'banned_songs', 'following_users',
                  'mod_users', 'banned_songs_by_word', 'dark',
                  'color', 'can_verify')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    prefs = UserPrefsSerializer(source='userprefs_set', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'is_staff', 'prefs')
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }


class SessionSimpleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = models.Session
        fields = ('url', 'user', 'title', 'genre', 'link', 'suspend', 'sub_only',
                  'verified_only', 'ended', 'allow_soundcloud', 'allow_youtube',
                  'allow_spotify', 'allow_playmusic')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    requests = SongRequestDetailedSerializer(many=True, read_only=True, source='songrequest_set')

    class Meta:
        model = models.Session
        fields = ('url', 'user', 'title', 'genre', 'link', 'suspend', 'sub_only',
                  'verified_only', 'ended', 'allow_soundcloud', 'allow_youtube',
                  'allow_spotify', 'allow_playmusic')