from ..models import Request


class StoreRequestInDatabase(object):
    def process_request(self, request):
        b = Request(full_path=request.get_full_path())
        b.save()
        return None
