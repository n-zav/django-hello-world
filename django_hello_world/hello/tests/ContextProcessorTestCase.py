import unittest

from django.template import RequestContext
from django.test.client import RequestFactory
from django.conf import settings

from ..context_processors import access_to_settings


class ContextProcessorTestCase(unittest.TestCase):

    def test_access_to_settings(self):
        """
        Tests that settings are in the context
        """
        request = RequestFactory().get('/')
        context = RequestContext(request, {}, [access_to_settings])
        self.assertIn('SETTINGS', context)
        self.assertEquals(context['SETTINGS'], settings)
