"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django_hello_world.hello.models import Person
from django_hello_world.hello.views import HomePageView
import unittest
from django.test import RequestFactory


class HomePageViewTestCase(unittest.TestCase):
    def test_get(self):
        """HomePageView.get() sets 'person' in response context."""
        # Setup name.
        person = Person.objects.create(first_name="Nastya",
                                       last_name="Zavalkina",
                                       date_of_birth="1990-08-06",
                                       biography="Here I am",
                                       email="nastya.zavalkina@gmail.com",
                                       jabber="nastya.zavalkina@jabber.ru",
                                       skype="nastya.zavalkina",
                                       other_contacts="twitter: @mirronenko")
        # Setup request and view.
        request = RequestFactory().get('/fake-path')
        view = HomePageView.as_view(template_name='hello/home.html')
        # Run.
        response = view(request, person=person)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'hello/home.html')
        self.assertEqual(response.context_data['person'], person)
