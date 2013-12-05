from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from django_hello_world.hello.middleware.http_request import *

from with_asserts.mixin import AssertHTMLMixin


class RequestTestCase(TestCase, AssertHTMLMixin):

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

    def test_middleware_class_is_in_middleware_classes(self):
        middleware_classes = getattr(settings, 'MIDDLEWARE_CLASSES')
        self.assertIn(
            'django_hello_world.hello.middleware.http_request.StoreRequestInDatabase',
            middleware_classes)

    def setUp(self):
        Request.objects.all().delete()
        Request.objects.create(full_path='/test1/', priority=2)
        Request.objects.create(full_path='/test2/', priority=1)

    def test_view_with_priorities(self):

        response = self.client.get(reverse('request'))
        with self.assertHTML(response, 'ul#request_list li') as (first, second, third):
            self.assertIn('[2] /test1/', first.text)
            self.assertIn('[1] /request/', second.text)
            self.assertIn('[1] /test2/', third.text)
