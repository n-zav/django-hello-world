from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django_hello_world.hello.views import *
from django.contrib.auth.views import login, logout
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', HomePageView.as_view(), name='home'),
                       url(r'^request/', RequestListView.as_view(),
                           name='request'),
                       # auth urls
                       url(r'^accounts/login/$', login, name='login'),
                       url(r'^accounts/logout/$', logout, name='logout'),
                       url(r'^accounts/profile/$', redirect_to, {'url': '/'},
                           name='accounts-profile'),
                       url(r'^accounts/$', redirect_to, {'url': '/'},
                           name='accounts'),
                       # edit urls
                       url(r'^edit/$', edit_view, name="edit-view"),
                       # admin urls
                       url(r'^admin/doc/',
                           include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)), )

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {
            'document_root': settings.MEDIA_ROOT,
            }),
        url(r'^static(?P<path>.*)$', 'django.views.static.serve',
            {
            'document_root': settings.STATIC_ROOT,
            }),
        )
