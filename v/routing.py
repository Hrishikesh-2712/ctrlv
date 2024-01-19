from django.urls import re_path
from .consumers import WSConsumer

ws_urlPatterns = [
    re_path(r'ws/$', WSConsumer.as_asgi()),
    re_path(r'ws/(?P<group>\w+)/$', WSConsumer.as_asgi())
    ]


