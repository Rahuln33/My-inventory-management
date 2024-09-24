from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):
    def test_create_item(self):
        url = reverse('create_item')
        data = {'name': 'Test Item', 'description': 'Test Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        item = Item.objects.create(name='Test Item', description='Test Description')
        url = reverse('item_detail', args=[item.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
