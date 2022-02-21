from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)

admin.site.register(Song, SongAdmin)
