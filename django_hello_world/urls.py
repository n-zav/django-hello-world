from django.conf.urls.defaults import patterns, include, url
from django_hello_world.hello.views import HomePageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       #  Examples:
                       url(r'^$', HomePageView.as_view(), name='home'),

                       # Uncomment the admin/doc line below to enable
                       # admin documentation:
                       url(r'^admin/doc/',
                           include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)), )
