from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import SongForm
from .models import Song
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def createsong(request):
    if request.method == 'GET':
        return render(request, 'songs/createsong.html', {'form': SongForm()})
    else:
        try:
            form = SongForm(request.POST)
            newsong = form.save(commit=False)
            newsong.user = request.user
            newsong.save()
            return redirect('currentplaylistsongs')
        except ValueError:
            return render(request, 'songs/createsong.html', {'form':SongForm(), 'error': 'Bad Data Passed In.  Try Again!!!'})  

@login_required
def currentsongs(request):
    songs = Song.objects.filter(user=request.user).order_by('created')
    return render(request, 'songs/currentsongs.html', {'songs': songs})

@login_required
def currentplaylistsongs(request):
    songs = Song.objects.filter(user=request.user, currentplaylist=True).order_by('created')
    return render(request, 'songs/currentplaylistsongs.html', {'songs': songs})

@login_required
def viewsong(request, song_pk):
    song = get_object_or_404(Song, pk=song_pk)
    if request.method == 'GET':
        form = SongForm(instance=song) # very cool it will automatically forward the info
        return render(request, 'songs/viewsong.html', {'song': song, 'form': form})
    else:
        try:
            form = SongForm(request.POST, instance=song)
            form.save()
            return redirect('currentplaylistsongs')
        except ValueError:
            form = SongForm(request.POST)     
            return render(request, 'songs/viewtodo.html', {'song':song(), 'form': form,  'error': 'Bad Data Passed In.  Try Again!!!'})

@login_required
def deletesong(request, song_pk):
    song = get_object_or_404(Song, pk=song_pk, user=request.user)
    if request.method == 'POST':
        song.delete()
        return redirect('currentplaylistsongs')


      
