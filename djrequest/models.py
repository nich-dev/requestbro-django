from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
colors = (
          ('blue', 'Blue (Default)'), ('red', 'Red'), ('pink', 'Pink'),
          ('purple', 'Purple'), ('deep-purple', 'Deep Purple'),
          ('indigo', 'Indigo'), ('light-blue', 'Light Blue'),
          ('cyan', 'Cyan'), ('teal', 'Teal'), ('green', 'Green'),
          ('light-green', 'Light Green'), ('lime', 'Lime'),
          ('orange', 'Orange'), ('deep-orange', 'Deep Orange'),
          ('brown', 'Brown'), ('grey', 'Greyscale'), ('blue-grey', 'Blue-Grey'),          
          )


class Genre(models.Model):
    title = models.CharField(max_length=20)
    date_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s' % (self.title)
    
    class Meta:
        ordering = ['title']

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=30)
    soundcloud_link = models.CharField(max_length=150, blank=True, null=True)
    youtube_link = models.CharField(max_length=150, blank=True, null=True)
    spotify_link = models.CharField(max_length=150, blank=True, null=True)
    playmusic_link = models.CharField(max_length=150, blank=True, null=True)
    verified = models.BooleanField(default=False)
    requests = models.IntegerField(default=0)
    genre = models.ForeignKey(Genre)
    date_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s by %s' % (self.title, self.artist)
    
    class Meta:
        ordering = ['title']
    
class Session(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    genre = models.ForeignKey(Genre)
    link = models.CharField(max_length=255)
    suspend = models.BooleanField(default=False)
    sub_only = models.BooleanField(default=False)
    verified_only = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)
    date_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s by %s' % (self.title, self.user)
    
    class Meta:
        ordering = ['user']
    
class SongRequest(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    complete = models.BooleanField(default=False)
    note = models.CharField(max_length=100, blank=True, null=True)
    points = models.IntegerField(default=0)
    date_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s requests %s' % (self.title, self.song)
    
    class Meta:
        ordering = ['user']
    
class UserPrefs(models.Model):
    user = models.ForeignKey(User)
    default_link = models.CharField("Default link that will show up in your sessions.",max_length=255, blank=True, null=True)
    logo = models.TextField(blank=True,null=True)
    banned_users = models.ManyToManyField(User, related_name="banners", blank=True)
    subbed_users = models.ManyToManyField(User, related_name="subs", blank=True)
    banned_songs = models.ManyToManyField(Song, blank=True)
    following_users = models.ManyToManyField(User, blank=True, related_name="followers")
    mod_users = models.ManyToManyField(User, blank=True, related_name="moderators")
    banned_songs_by_word = models.TextField(blank=True,null=True)
    dark = models.BooleanField(default=False)
    color = models.CharField(max_length=15, default="blue", choices=colors)
    can_verify = models.BooleanField(default=False) #admin things
    date_edited = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return '%s profile %s' % (self.user, self.date_edited)
    
    class Meta:
        ordering = ['user']