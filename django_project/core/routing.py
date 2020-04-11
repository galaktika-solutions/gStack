from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class Websocket(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'everybody',
            self.channel_name
        )
        self.accept()

    def message(self, event):
        self.send_json(event)


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                path('ws/', Websocket),
            ]
        )
    ),
})
