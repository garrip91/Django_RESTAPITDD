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

    def test_api_can_get_a_bucketlist(self):
        """ENG: Test the Django_RESTAPITDD_App app can get a given data."""
        """RUS: Проверяем может ли наше приложение (Django_RESTAPITDD_App) получить запись (данные)."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': bucketlist.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)
    
    def test_api_can_update_bucketlist(self):
        """ENG: Test the Django_RESTAPITDD_App app can update a given data."""
        """RUS: Проверяем может ли наше приложение (Django_RESTAPITDD_App) обновить запись (данные)."""
        #change_bucketlist = {'name': 'Something new'}
        #### Я ДОБАВИЛ: ####
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something new'}
        ####################
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_api_can_delete_bucketlist(self):
        """ENG: Test the Django_RESTAPITDD_App app can delete a given data."""
        """RUS: Проверяем может ли наше приложение (Django_RESTAPITDD_App) удалить запись (данные)."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
