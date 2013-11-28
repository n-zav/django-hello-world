from django_hello_world.hello.models import Request
from django.http import HttpRequest


class StoreRequestInDatabase(object):
    def process_request(self, request):
        b = Request(full_path=HttpRequest.get_full_path(request))
        b.save()
        return None
