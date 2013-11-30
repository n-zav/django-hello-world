from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from mock import patch, Mock
from mock import MagicMock
from django_hello_world.hello.middleware.http_request import *


class RequestTestCase(TestCase):

    # mock models.Request constructor
    def test_process_request(self):
        # test that there is no record in db at first
        test_full_path = '/test_full_path'
        count = Request.objects.filter(full_path=test_full_path).count()
        self.assertEqual(0, count)

        # instantiate object under test and call method which we want to test
        request = RequestFactory().get(test_full_path)
        object_under_test = StoreRequestInDatabase()
        object_under_test.process_request(request)

        # test that the record exists now
        count = Request.objects.filter(full_path=test_full_path).count()
        self.assertEqual(1, count)
