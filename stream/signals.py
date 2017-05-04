import json
import requests
from django.conf import settings
from .utils import serialize_stream


def stream_post_save(sender, instance, created, **kwargs):
    url = "{}/stream/update".format(settings.STREAMER_API_URL)
    if created:
        url = "{}/stream/add".format(settings.STREAMER_API_URL)
    try:
        r = requests.post(url, data={
            'data': json.dumps(serialize_stream(instance))
        })
    except requests.ConnectionError:
        pass
