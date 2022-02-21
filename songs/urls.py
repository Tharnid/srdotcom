from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('create/', views.createsong, name='createsong'),
    path('currentplaylist/', views.currentplaylistsongs, name='currentplaylistsongs'),
    path('currentsongs/', views.currentsongs, name='currentsongs'),
    path('song/<int:song_pk>', views.viewsong, name='viewsong'),
     path('song/<int:song_pk>/delete', views.deletesong, name='deletesong'),   
    #path('acousticsongs', views.acousticsongs, name='acousticsongs'),
    #path('electricsongs', views.electricsongs, name='electricsongs'),
    #path('backlog', views.backloggedsongs, name='backloggedsongs'),
    #path('songs/<slug:slug>', views.viewsong, name='viewsong'), # posts/my-first-song  
]