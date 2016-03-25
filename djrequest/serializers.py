# Serializers define the API representation.]
import models
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        
class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('url', 'title')
        
class SongSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = User
        fields = ('url', 'title', 'soundcloud_link', 'youtube_link',
                  'spotify_link', 'playmusic_link', 'verified', 'requests',
                  'genre')
        
class SessionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)
    genre = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = User
        fields = ('url', 'user', 'title', 'genre', 'link', 'suspend', 'sub_only', 
                  'verified_only', 'ended')
        
class SongRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'user', 'song', 'complete', 'note', 'points')
        
class SongRequestDetailedSerializer(serializers.HyperlinkedModelSerializer):
    song = SongSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'user', 'song', 'complete', 'note', 'points')
        
class UserPrefsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)
    banned_users = serializers.StringRelatedField(many=True)
    subbed_users = serializers.StringRelatedField(many=True)
    following_users = serializers.StringRelatedField(many=True)
    mod_users = serializers.StringRelatedField(many=True)
    banned_songs_by_word = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = User
        fields = ('url', 'user', 'default_link', 'logo',
                  'banned_users', 'subbed_users', 'following_users', 'mod_users',
                  'banned_songs_by_word', 'dark', 'color', 'can_verify')