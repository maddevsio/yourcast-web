# -*- coding: utf-8 -*-
import json
from random import shuffle

def serialize_stream(stream):
    items = stream.youtube_links.split("\n")
    if stream.play_random:
        shuffle(items)
    return {
        "id": stream.pk,
        "name": stream.name,
        "slug": stream.slug,
        "keywords": stream.keywords,
        "plex_playlist_id": stream.plex_playlist_id,
        "channels": stream.channels,
        "update_frequency": stream.update_frequency,
        "video_length": stream.video_length,
        "is_news": stream.is_news,
        "play_random": stream.play_random,
        "links": [{
            "url": link
        } for link in items]
    }


