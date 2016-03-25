from django.contrib import admin
import models

# Register your models here.
class UserPrefAdmin(admin.ModelAdmin):
    model = models.UserPrefs
    
    list_display = ('user', 'date_created','date_edited')
    search_fields = ('user', 'date_created','date_edited')
    ordering = ('user',)
    
class SongAdmin(admin.ModelAdmin):
    model = models.Song
    
    list_display = ('title', 'artist','date_created','date_edited')
    search_fields = ('title', 'artist', 'date_created','date_edited')
    ordering = ('title','artist')
    
class SessionAdmin(admin.ModelAdmin):
    model = models.Session
    
    list_display = ('title', 'user','date_created','date_edited')
    search_fields = ('title', 'user', 'date_created','date_edited')
    ordering = ('date_created','user')
    
class SongRequestAdmin(admin.ModelAdmin):
    model = models.SongRequest
    
    list_display = ('user','date_created','date_edited')
    search_fields = ('user', 'date_created','date_edited')
    ordering = ('date_created','user')
    
admin.site.register(models.UserPrefs, UserPrefAdmin)
admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Session, SessionAdmin)
admin.site.register(models.SongRequest, SongRequestAdmin)