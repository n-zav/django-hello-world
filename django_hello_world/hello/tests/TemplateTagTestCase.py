from django.test import TestCase
from ..models import Person
from ..templatetags.object_admin_edit_link_tag import admin_edit_link


class TemplateTagTestCase(TestCase):

    person = Person.objects.create(pk=2,
                                   first_name='Jane',
                                   last_name='Doe',
                                   date_of_birth='2001-01-01',
                                   biography='Jane Doe',
                                   email='jane.oe@example.com',
                                   jabber='jane.doe.jabber.ru',
                                   skype='jane.doe',
                                   other_contacts='Contact Jane')

    def test_edit_admin_link(self):
        self.assertEqual(admin_edit_link(self.person), '/admin/hello/person/2/')
