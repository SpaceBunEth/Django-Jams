from rest_framework import serializers
from .models import Songs, Playlist, Album, Genre, Artist
from pprint import pprint as p

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'
        