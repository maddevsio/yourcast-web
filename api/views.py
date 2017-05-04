# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.core import serializers
from stream.models import Stream, Category
from stream.utils import serialize_stream


def streams(request):
    return JsonResponse([
        serialize_stream(stream) for stream in Stream.objects.filter(active=True)
    ], safe=False)


def next_stream(request, stream_id):
    is_end = False
    stream = Stream.objects.get(pk=stream_id)
    next_stream = Stream.objects.filter(
        pk__gt=stream_id,
        category=stream.category
    ).first()
    if not next_stream:
        category = Category.objects.filter(
            pk__gt=stream.category_id
        ).first()
        next_stream = Stream.objects.filter(
            category=category
        ).first()

    if not next_stream:
        is_end = True
        next_stream = stream

    return JsonResponse({
        "next_stream": next_stream.pk,
        "img": next_stream.img.url,
        "title": next_stream.name,
        "is_end": is_end,
    })


def prev_stream(request, stream_id):
    is_end = False
    stream = Stream.objects.get(pk=stream_id)
    next_stream = Stream.objects.filter(
        pk__lt=stream_id,
        category=stream.category
    ).last()
    if not next_stream:
        category = Category.objects.filter(
            pk__lt=stream.category_id
        ).first()
        next_stream = Stream.objects.filter(
            category=category
        ).last()

    if not next_stream:
        is_end = True
        next_stream = stream

    return JsonResponse({
        "prev_stream": next_stream.pk,
        "img": next_stream.img.url,
        "title": next_stream.name,
        "is_end": is_end,
    })
