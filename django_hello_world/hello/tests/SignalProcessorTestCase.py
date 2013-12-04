from django.test import TestCase
from ..models import Person, Change


class AuthEditTestCase(TestCase):
    def setUp(self):
        Change.objects.all().delete()

    def test_signal_processor(self):
        # test that table changes is empty from the outset
        self.assertEqual(Change.objects.all().count(), 0)
        # check created
        person = Person.objects.create(
            first_name="Jane",
            last_name="Doe",
            date_of_birth="2001-01-01",
            biography="Jane Doe's biograpthy",
            email="jane.doe@example.com",
            skype="jane.doe",
            jabber="jane.doe@jabber.ru",
            other_contacts="Contact Jane"
        )
        self.assertEqual(Change.objects.all().count(), 1)

        # check updated
        person.first_name = "Martishka"
        person.save()
        changes = Change.objects.filter(change_type='updated').filter(model_name='Person')
        self.assertEqual(changes.count(), 1)

        # check deleted
        person.delete()
        changes = Change.objects.filter(change_type='deleted').filter(model_name='Person')
        self.assertEqual(changes.count(), 1)
