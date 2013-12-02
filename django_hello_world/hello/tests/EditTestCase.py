from django.test import TestCase
from ..forms import EditForm
from ..models import Person


class EditTestCase(TestCase):

    def test_valid_form(self):
        person = Person.objects.create(first_name="Jane",
                                       last_name="Doe",
                                       date_of_birth="2001-01-01",
                                       biography="Jane Doe's bio",
                                       email="jane.doe@example.com",
                                       jabber="jane.doe@jabber.ru",
                                       skype="jane.doe",
                                       other_contacts="Contact Jane",
                                       image="")
