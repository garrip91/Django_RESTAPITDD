from django.test import TestCase

from .models import Bucketlist

# Добавим эти импорты:
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):
    """ENG: This class defines the test suite for the bucketlist model."""
    """RUS: Этот класс определяет набор тестов для модели Bucketlist."""
    
    def setUp(self):
        """ENG: This method defines the test client and other test variables."""
        """RUS: Этот метод определяет тестовый клиент и другие тестовые переменные."""
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)
    
    def test_model_can_create_a_bucketlist(self):
        """ENG: Test the Bucketlist model can create data."""
        """RUS: Проверяем может ли модель Bucketlist создать запись (данные)."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """ENG: This class defines the test suite for the our app (Django_RESTAPITDD_App) views."""
    """RUS: Этот класс определяет набор тестов для представлений нашего приложения (Django_RESTAPITDD_App)."""
    
    def setUp(self):
        """ENG: This method defines the test client and other test variables."""
        """RUS: Этот метод определяет тестовый клиент и другие тестовые переменные."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )
    
    def test_api_can_create_a_bucketlist(self):
        """ENG: Test the Django_RESTAPITDD_App app can create data."""
        """RUS: Проверяем может ли наше приложение (Django_RESTAPITDD_App) создать запись (данные)."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

