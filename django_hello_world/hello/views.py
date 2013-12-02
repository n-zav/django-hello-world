from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .forms import EditForm
from .models import Person, Request
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class HomePageView(TemplateView):

    template_name = "hello/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        person = Person.objects.get(pk=1)
        context['person'] = person
        return context


class RequestListView(ListView):

    model = Request
    template_name = "hello/request.html"
    queryset = Request.objects.order_by('-time_added')[:10]


@login_required
def edit_view(request):
    person = Person.objects.get(pk=1)
    if request.method == 'POST':  # If the form has been submitted...
        form = EditForm(request.POST, request.FILES, instance=person)
        if form.is_valid():  # All validation rules pass
            form.save()
            return HttpResponseRedirect(reverse('home'))  # Redirect after POST
    else:
        form = EditForm(instance=person)  # An unbound form

    return render_to_response('hello/edit.html', {
        'person': person,
        'form': form}, context_instance=RequestContext(request))
