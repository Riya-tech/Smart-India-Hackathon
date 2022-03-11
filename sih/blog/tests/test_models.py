from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Items, ItemsCart

class TestModels(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    