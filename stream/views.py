from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Stream, Category

def home_page(request, template='home.html'):
    streams = Stream.objects.filter(active=True)
    featured = Stream.objects.filter(active=True, featured=True).count() > 0
    if featured:
        streams = streams.filter(featured=True)
    return render(request, template, {
        "streams": streams,
        "trending": Stream.objects.filter(active=True).order_by('?'),
        "featured_enabled": Stream.objects.filter(active=True, featured=True).count() > 0,
        "categories": Category.objects.all(),
    })


def stream_info(request, stream_id, template='stream.html'):
    stream = get_object_or_404(Stream, pk=stream_id)

    return render(request, template, {
        "stream": stream,
        "stream_url": "{}/{}.m3u8".format(stream.hls_root_url, stream.slug)
    })


def coub(request, template='coub.html'):

    return render(request, template, {
        "stream": None,
        "stream_url": settings.COUB_STREAM_URL
    })


def cc(request, stream_id, template='cc.html'):
    stream = get_object_or_404(Stream, pk=stream_id)

    return render(request, template, {
        "stream": stream,
        "stream_url": "{}/{}.m3u8".format(stream.hls_root_url, stream.slug)
    })


def category_info(request, category_id, template='category.html'):
    category = get_object_or_404(Category, pk=category_id)
    streams = Stream.objects.filter(category=category, active=True)
    return render(request, template, {
        "category":category,
        "streams":streams,
    })


def search_stream(request, search_query, template='pages/search.html'):
    search = search_query.strip().replace(" ", "|")
    streams = Stream.objects.filter(name__iregex=".*%s.*" % search, active=True)
    return render(request, template, {
        "streams": streams,
        "search_request": search_query,
    })


def multistream(request, template='multistream.html'):
    streams = map(lambda o: "{}/{}.m3u8".format(settings.HLS_ROOT_URL, o.slug),
                  Stream.objects.filter(active=True))
    return render(request, template, {
        "streams": streams,
    })
