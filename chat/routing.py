from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('api/chat/', consumers.ChatConsumer.as_asgi()),
]