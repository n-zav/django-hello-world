from django.http import HttpRequest
from django.test import TestCase
from mock import patch, Mock
from mock import MagicMock
from django_hello_world.hello.middleware.http_request import *


class RequestTestCase(TestCase):

    # mock models.Request constructor
    @patch('django_hello_world.hello.middleware.HttpRequest.Request')
    def test_process_request(self, mock_request_class):

        # mock models.Request.save method
        save_mock = Mock(return_value=None)
        mock_request_class.return_value.save = save_mock

        # create new django.http.HttpRequest object to pass
        # into the StoreRequestInDatabase.process_request()
        test_full_path = 'test_full_path'
        mock_http_request = HttpRequest()
        # replace get_full_path() method of newly created object with mock
        mock_http_request.get_full_path \
            = MagicMock(return_value=test_full_path)

        # instantiate object under test and call method which we want to test
        object_under_test = StoreRequestInDatabase()
        object_under_test.process_request(mock_http_request)

        # verify that all methods were called correctly
        # (expected number of times and/or with correct parameters)
        self.assertEqual(mock_http_request.get_full_path.call_count, 1)
        mock_request_class.assert_called_once_with(full_path=test_full_path)
        self.assertEqual(save_mock.call_count, 1)
