from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    note = models.TextField(max_length=100, blank=True) # blank is equal to null
    lyriclink = models.URLField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    currentplaylist = models.BooleanField(default=False)
    acousticonly = models.BooleanField(default=False)
    electriconly = models.BooleanField(default=False)
    backlog = models.BooleanField(default=False)
    user =  models.ForeignKey(User, on_delete=models.CASCADE) # foreign key/relationship 

    # display the songs better in admin

    def __str__(self):
        return self.title    
