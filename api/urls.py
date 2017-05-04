from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^streams/$', views.streams, name='list_streams'),
    url(
        r'^stream/(?P<stream_id>\d+)/next',
        views.next_stream,
        name='next_stream'
    ),

    url(
        r'^stream/(?P<stream_id>\d+)/prev',
        views.prev_stream,
        name='prev_stream'
    ),
]
