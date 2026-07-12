import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StockManagmentSystem.settings")
django.setup()

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model
import core.models as models
from datetime import date

class ItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = models.category.objects.create(name="Test Category")
        self.Item = models.Item.objects.create(name="Test item", quantity=100, category=self.category)

    def test_get_item_list(self):
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(p['name'] == "Test item" for p in response.data))

    def test_get_item_detail(self):
        url = reverse('item-detail', args=[self.Item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test item")

    def test_create_item(self):
        url = reverse('item-list')
        data = {
            "name": "New item",
            "quantity": 50,
            "category": self.category.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New item")

    def test_update_item(self):
        url = reverse('item-detail', args=[self.Item.id])
        data = {
            "name": "Updated item",
            "quantity": 80,
            "category": self.category.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated item")

    def test_delete_item(self):
        url = reverse('item-detail', args=[self.Item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.Item.objects.filter(id=self.Item.id).exists())

class CategoryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = models.category.objects.create(name="Test Category")

    def test_get_category_list(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(c['name'] == "Test Category" for c in response.data))

    def test_get_category_detail(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Category")

    def test_create_category(self):
        url = reverse('category-list')
        data = {"name": "New Category"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Category")

    def test_update_category(self):
        url = reverse('category-detail', args=[self.category.id])
        data = {"name": "Updated Category"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Category")

    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.category.objects.filter(id=self.category.id).exists())

class SectionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='sectionuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.section = models.section.objects.create(name="Test Section")

    def test_get_section_list(self):
        url = reverse('section-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(s['name'] == "Test Section" for s in response.data))

    def test_get_section_detail(self):
        url = reverse('section-detail', args=[self.section.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Section")

    def test_create_section(self):
        url = reverse('section-list')
        data = {"name": "New Section"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Section")

    def test_update_section(self):
        url = reverse('section-detail', args=[self.section.id])
        data = {"name": "Updated Section"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Section")

    def test_delete_section(self):
        url = reverse('section-detail', args=[self.section.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.section.objects.filter(id=self.section.id).exists())

class StockInAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = models.category.objects.create(name="StockInCat")
        self.item = models.Item.objects.create(name="StockInItem", quantity=10, category=self.category)
        self.stockin = models.StockIn.objects.create(
            item=self.item,
            quantity=5,
            date_of_entry='2025-06-01',  # Use a valid date format
            category=self.category,
            reciever="Receiver Name",
            remarks="Test remarks"
        )

    def test_get_stockin_list(self):
        url = reverse('stock-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(s['remarks'] == "Test remarks" for s in response.data))

    def test_get_stockin_detail(self):
        url = reverse('stock-detail', args=[self.stockin.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['remarks'], "Test remarks")

    
    

    def test_delete_stockin(self):
        url = reverse('stock-detail', args=[self.stockin.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.StockIn.objects.filter(id=self.stockin.id).exists())

class StockOutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='stockoutuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = models.category.objects.create(name="StockOutCat")
        self.section = models.section.objects.create(name="StockOutSection")
        self.item = models.Item.objects.create(name="StockOutItem", quantity=10, category=self.category)
        self.stockout = models.StockOut.objects.create(
            item=self.item,
            quantity=3,
            date_of_issue='2025-06-01',
            category=self.category,
            section=self.section,
            emp_name="Emp Name",
            remarks="StockOut remarks"
        )

    def test_get_stockout_list(self):
        url = reverse('stockout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(s['remarks'] == "StockOut remarks" for s in response.data))

    def test_get_stockout_detail(self):
        url = reverse('stockout-detail', args=[self.stockout.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['remarks'], "StockOut remarks")

    

    def test_delete_stockout(self):
        url = reverse('stockout-detail', args=[self.stockout.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(models.StockOut.objects.filter(id=self.stockout.id).exists())