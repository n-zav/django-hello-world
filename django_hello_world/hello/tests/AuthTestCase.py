from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from unittest_data_provider import data_provider


class AuthTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'test')

    guests_links = lambda: (
        ('Home', reverse('home'), True),
        ('Requests', reverse('request'), True),
        ('Login', reverse('login'), True),
        ('Logout', reverse('logout'), False),
        ('Edit', reverse('edit-view'), False),
        ('Edit in Admin', '/admin/hello/person/1/', False)
    )

    @data_provider(guests_links)
    def test_guest_links_are_present(self, link_title, link, link_present):
        response = self.client.get('/')
        if link_present:
            self.assertIn(link_title, response.content)
            self.assertIn(link, response.content)
        else:
            self.assertNotIn(link, response.content)

    account_pages = lambda: (
        ('/accounts',),
        ('/accounts/profile',),
    )

    @data_provider(account_pages)
    def test_redirect_account_pages(self, page):
        self.client.login(username='test', password='test')
        response = self.client.get(page, follow="True")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Contact Details</title>', response.content)

    user_links = lambda: (
        ('Home', reverse('home'), True),
        ('Requests', reverse('request'), True),
        ('Logout', reverse('logout'), True),
        ('Login', reverse('login'), False),
        ('Edit', reverse('edit-view'), True),
        ('Edit in Admin', '/admin/hello/person/1/', True)
    )

    @data_provider(user_links)
    def test_user_links_are_present(self, link_title, link, link_present):
        self.client.login(username='test', password='test')
        response = self.client.get('/')
        if link_present:
            self.assertIn(link_title, response.content)
            self.assertIn(link, response.content)
        else:
            self.assertNotIn(link, response.content)
