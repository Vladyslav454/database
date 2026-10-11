from django.test import TestCase
from .models import Category

class TestCategoryModel(TestCase):  # Змінено назву класу
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/articles/category/innovations')