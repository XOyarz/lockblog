from django.test import TestCase
from blog.views import *
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

# First test: root URL resolves to post_list view
    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')

        self.assertEqual(found.func, post_list)

# Second test: the post_list view returns the html found in post_list.html
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        expected_html = render_to_string('blog/post_list.html')

        self.assertEqual(response.content.decode(), expected_html)

# Third test can replace the previous two
    def test_home_page_works(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')


    def test_user_can_log_in_and_out(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'registration/login.html')
