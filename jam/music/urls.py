from django.urls import path, include
from .views import SongsAPIView

urlpatterns = [
    path('songs/', SongsAPIView.as_view()),
    path('songs/<str:pk>/', SongsAPIView.as_view()),
]