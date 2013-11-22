"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_hello_world.hello.models import Person


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class HttpTest(TestCase):
    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello!')


class PersonTestCase(TestCase):
    Person.objects.create(first_name="Jane", last_name="Doe",
                          date_of_birth="01.01.2001", biography="Here is Jane Doe's bio",
                          email="jane.doe@gmail.com", jabber="jane.doe@jabber.ru",
                          skype="jane.doe", other_contacts="contact jane")
    Person.objects.create(first_name="John", last_name="Doe",
                          date_of_birth="02.02.2002", biography="Here is John Doe's bio",
                          email="john.doe@gmail.com", jabber="john.doe@jabber.ru",
                          skype="john.doe", other_contacts="contact john")

    def test_person_creation(self):
        """Jane and John are correctly identified"""
        jane = Person.objects.get(first_name="jane")
        john = Person.objects.get(first_name="john")
        self.assertEqual(jane.date_of_birth(), "01.01.2001")
        self.assertEqual(jane.skype(), "jane.doe")
        self.assertEqual(john.email(), "john.doe@gmail.com")
        self.assertEqual(john.biography(), "Here is John Doe's bio")