from django.views.generic.base import TemplateView

from django_hello_world.hello.models import Person


class HomePageView(TemplateView):

    template_name = "hello/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        person = Person.objects.get(email="nastya.zavalkina@gmail.com")
        context['person'] = person
        return context

#@render_to('hello/home.html')
#def home(request):
#    users = User.objects.all()
#    return {'users': users}
