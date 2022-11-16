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

class Songs(models.Model):
    title = models.CharField(max_length=255)
    duration = models.TimeField()
    num_play = models.IntegerField()
    explicit = models.BooleanField()
    # playlist_song = models.ManyToManyField(Playlist)
    # album_song = models.ManyToManyField(Album)
    # genre_song = models.ManyToManyField(Genre)
    # artist_song = models.ManyToManyField(Artist)


class PlaylistSong(models.Model):
    song = models.ForeignKey('Songs', on_delete=models.PROTECT)
    playlist = models.ForeignKey('Playlist', on_delete=models.PROTECT)

class AlbumSongs(models.Model):
    album = models.ForeignKey('Album', on_delete=models.PROTECT)
    song = models.ForeignKey('Songs', on_delete=models.PROTECT)

class GenreSongs(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    song = models.ForeignKey('Songs', on_delete=models.PROTECT)

class ArtistSongs(models.Model):
    artist = models.ForeignKey('Artist',on_delete=models.PROTECT)
    song = models.ForeignKey('Songs', on_delete=models.PROTECT)


