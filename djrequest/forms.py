from django.forms import ModelForm
from models import UserPrefs, SongRequest, Song, Session

class UserPrefForm(ModelForm):
    class Meta:
        model = UserPrefs
        fields = ['default_link', 'banned_users', 'banned_songs',
                  'banned_songs_by_word','following_users',
                  'mod_users', 'dark', 'color', ]

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'soundcloud_link', 
                  'youtube_link','spotify_link', 
                  'playmusic_link', 'genre', ]
        
class SongRequestForm(ModelForm):
    class Meta:
        model = SongRequest
        fields = ['song', 'note', ]
        
class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'genre', 'link', 
                  'verified_only',]