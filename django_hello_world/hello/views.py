import json
from time import sleep

from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .forms import EditForm
from .models import Person, Request


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
        sleep(10)
        form = EditForm(request.POST, request.FILES, instance=person)
        is_ajax_request = form.data['is_ajax_request']

        if form.is_valid():  # All validation rules pass
            form.save()
            html = render_to_string('hello/edit_form.html', {
                'person': person,
                'form': form}, context_instance=RequestContext(request))
            response = json.dumps({
                'success': True,
                'message': 'Data was successfully updated.',
                'html': html
            })
        else:
            html = render_to_string('hello/edit_form.html', {
                'person': person,
                'form': form}, context_instance=RequestContext(request))
            response = json.dumps({
                'success': False,
                'message': 'An error occurred while updating data',
                'html': html
            })
        if is_ajax_request:
            return HttpResponse(response,
                                content_type="application/javascript")
        else:
            if form.is_valid():
                return HttpResponseRedirect(reverse('home'))
    else:
        form = EditForm(instance=person)  # An unbound form

    return render_to_response('hello/edit.html', {
        'person': person,
        'form': form}, context_instance=RequestContext(request))
