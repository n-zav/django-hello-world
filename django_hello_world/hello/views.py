from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Person, Request


class HomePageView(TemplateView):

    template_name = "hello/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        person = Person.objects.get(email="nastya.zavalkina@gmail.com")
        context['person'] = person
        return context


class RequestListView(ListView):

    model = Request
    template_name = "hello/request.html"

    def get_queryset(self):
        r = Request.objects.all()
        count = r.count()
        result = Request.objects.order_by('-time_added')[:10]
        return result

    def get_context_data(self, **kwargs):
        context = super(RequestListView, self).get_context_data(**kwargs)
        return context
