# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from stream import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^stream/(?P<stream_id>\d+)/$', views.stream_info, name='stream_info'),
    url(r'^coub/$', views.coub, name='coub'),
    url(r'^ccy/(?P<stream_id>\d+)/$', views.cc, name='cc'),
    url(r'^multistream', views.multistream, name='multistream'),
    url(
        r'^category/(?P<category_id>\d+)/$',
        views.category_info,
        name='category_info'
    ),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^search/(?P<search_query>[\d\w\s]+)$', views.search_stream, name='search'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('devtv_webui.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include('api.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
