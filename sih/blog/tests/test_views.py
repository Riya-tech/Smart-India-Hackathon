from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Items, ItemsCart
import json


class TestViews(TestCase):

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

    def ttest_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def ttest_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testg_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testg_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testg_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testg_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testnot_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testnot_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testll_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testtt_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testtt_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testgeee_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testeee_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testeeeeee_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def testeeeeeeee_home_GET(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def testggg_about_GET(self):
        response = self.client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')
