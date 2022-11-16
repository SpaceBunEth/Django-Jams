from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Songs
from .serializers import SongsSerializer

from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class SongsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Songs.objects.get(pk=pk)
        except Songs.DoesNotExists:
            raise Http404
    # Read
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongsSerializer(data)
        else:
            data = Songs.objects.all()
            serializer = SongsSerializer(data, many=True)
        return Response(serializer.data)
    # Create
    def post(self, request, format=None):
        print('MADE A POST REQUEST')
        data = request.data
        serializer = SongsSerializer(data=data)

        #Check data is valid
        serializer.is_valid(raise_exception=True)

        #Save the Song sent over
        serializer.save()

        response.data = {
            'message': 'Song CREATED SUCCESSFULLY',
            'data': serializer.data,
        }
        return Response

        