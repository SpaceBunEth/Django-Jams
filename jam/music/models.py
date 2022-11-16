from django.db import models

class Playlist(models.Model):
    name = models.CharField(max_length=69)

class Album(models.Model):
    name = models.CharField(max_length=69)

class Genre(models.Model):
    label = models.CharField(max_length=69)

class Artist(models.Model):
    name = models.CharField(max_length=69)
    bio = models.CharField(max_length=255)
    img_url = models.URLField(max_length=200)

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=255)
    duration = models.TimeField()
    num_play = models.IntegerField()
    explicit = models.BooleanField()
    playlist_song = models.ManyToManyField(Playlist)
    # album_song = models.ManyToManyField(Album)
    # genre_song = models.ManyToManyField(Genre)
    # artist_song = models.ManyToManyField(Artist)


