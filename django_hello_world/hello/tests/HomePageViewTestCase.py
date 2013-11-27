from django_hello_world.hello.models import Person
from django_hello_world.hello.views import HomePageView
from django.test import RequestFactory
import unittest


class HomePageViewTestCase(unittest.TestCase):
    def test_get(self):
        """HomePageView.get() sets 'person' in response context."""
        # Setup name.
        person = Person.objects.get(email="nastya.zavalkina@gmail.com")
        # Setup request and view.
        request = RequestFactory().get('/fake-path')
        view = HomePageView.as_view(template_name='hello/home.html')
        # Run.
        response = view(request, person=person)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'hello/home.html')
        self.assertEqual(response.context_data['person'], person)
