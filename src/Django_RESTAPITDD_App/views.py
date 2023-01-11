from django.shortcuts import render

from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    """ENG: This class defines the create behavior of our rest API."""
    """RUS: Этот класс определяет поведение создания нашего API."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    
    def perform_create(self, serializer):
        """ENG: This method saves the POST data when creating a new data."""
        """RUS: Этот метод сохраняет POST-данные при создании новой записи."""
        serializer.save()

