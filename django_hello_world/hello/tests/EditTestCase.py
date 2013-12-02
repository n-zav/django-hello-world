from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ..models import Person
from unittest_data_provider import data_provider


class NonAuthEditTestCase(TestCase):
    def test_edit_page_redirect(self):
        response = self.client.get(reverse('edit-view'))
        self.assertEqual(response.status_code, 302)

    def test_edit_page_redirects_to_home_page(self):
        response = self.client.get(reverse('edit-view'), follow=True)
        last_redirect = response.redirect_chain[-1][0]
        self.assertIn("/accounts/login/?next=/edit/", last_redirect)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Log in here</title>', response.content)


class AuthEditTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.get(pk=1)
        self.user = User.objects.create_user('Jane', 'jane.doe@gmail.com',
                                             'test')
        self.client.login(username='Jane', password='test')
        self.response = self.client.get(reverse('edit-view'))

    page_elements = lambda: (
        ('<form',),
        ('Cancel',)
    )

    @data_provider(page_elements)
    def test_edit_page(self, page_element):
        # test that the user can login.
        self.assertEqual(self.response.status_code, 200)
        # test that page elements exist on /edit/ page.
        self.assertIn(page_element, self.response.content)

    form_fields = lambda: (
        ('first_name',),
        ('last_name',),
        ('biography',),
        ('email',),
        ('jabber',),
        ('skype',),
        ('other_contacts',),
    )

    @data_provider(form_fields)
    def test_edit_form(self, form_field):
        self.assertIn(getattr(self.person, form_field), self.response.content)


class EditContactTestCasePost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Jane', 'jane.doe@gmail.com',
                                             'test')
        self.client.login(username='Jane', password='test')
        self.proper_data = {"first_name": "Nastya",
                            "last_name": "Zavalkina",
                            "date_of_birth": "1990-08-06",
                            "biography": "Here I am",
                            "email": "nastya.zavalkina@gmail.com",
                            "jabber": "nastya.zavalkina@jabber.ru",
                            "skype": "nastya.zavalkina",
                            "other_contacts": "twitter: @mirrronenko"}

    def test_form_submit_no_data(self):
        response = self.client.post(reverse('edit-view'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form']['first_name'].errors,
                         [u'This field is required.'])

    def test_form_submit_with_data(self):
        new_name = "Martishka"
        self.proper_data['first_name'] = new_name
        self.client.post(reverse('edit-view'), self.proper_data)
        person = Person.objects.get(pk=1)
        self.assertEqual(person.first_name, new_name)

    def test_form_submit_redirect(self):
        response = self.client.post(reverse('edit-view'), self.proper_data,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
