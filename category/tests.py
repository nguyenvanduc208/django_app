from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Category
from .serializers import CategorySerializer

# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_data = {'name': 'Electronics', "status": True}
        self.category = Category.objects.create(name='Clothing')

    def test_create_category(self):
        response = self.client.post("/api/categories", self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_get_categories(self):
        response = self.client.get("/api/categories")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)