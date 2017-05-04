# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from . import signals as stream_signals
from django.utils.encoding import python_2_unicode_compatible


class AbstractDateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Stream(AbstractDateTimeModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='streams')
    plex_playlist_id = models.CharField(max_length=255, blank=True)
    hls_root_url = models.CharField(max_length=255, blank=True)
    play_random = models.BooleanField(default=False)
    youtube_links = models.TextField(blank=True)
    category = models.ForeignKey('stream.Category')
    keywords = models.CharField(max_length=255, blank=True)
    channels = models.CharField(max_length=512, blank=True)
    update_frequency = models.PositiveSmallIntegerField(blank=True)
    video_length = models.PositiveSmallIntegerField(blank=True)
    is_news = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CategoryBackground(AbstractDateTimeModel):
    background = models.ImageField(upload_to='backgrounds')

    def __str__(self):
        return self.background.url


@python_2_unicode_compatible
class Category(AbstractDateTimeModel):
    # icon = models.ImageField(upload_to='icons')
    icon = models.TextField()
    backgrounds = models.ManyToManyField(CategoryBackground)
    title = models.CharField(max_length=255)
    mask = models.TextField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


post_save.connect(stream_signals.stream_post_save, sender=Stream)
