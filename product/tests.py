from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ProductTests(APITestCase):
    end_point = "/api/products/"
    
    def test_get_product(self, product_factory):
        response = self.client.get(self.end_point)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Lay ra thanh cong")