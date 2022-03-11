from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import about, create_view, list_view


class TestUrls(SimpleTestCase):
    def test_blog_about_url_is_resolved(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about)

    def test_blog_sell_url_is_resolved(self):
        url = reverse('blog-sell')
        self.assertEqual(resolve(url).func, create_view)

    def test_blog_hhome_url_is_resolved(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func, list_view)

    def test_blog_habout_url_is_resolved(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about)

    def test_blog_hsell_url_is_resolved(self):
        url = reverse('blog-sell')
        self.assertEqual(resolve(url).func, create_view)

    def test_blog_ghome_url_is_resolved(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func, list_view)

    def test_ggblog_about_url_is_resolved(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about)

    def test_ggblog_sell_url_is_resolved(self):
        url = reverse('blog-sell')
        self.assertEqual(resolve(url).func, create_view)

    def test_vvblog_hhome_url_is_resolved(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func, list_view)

    def test_vvblog_habout_url_is_resolved(self):
        url = reverse('blog-about')
        self.assertEqual(resolve(url).func, about)
