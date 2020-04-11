from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from .models import KeyValueStore
from .serializers import KeyValueStoreSerializer


class KeyValueStoreViewset(ModelViewSet):
    """ Contains Technical informations. """
    serializer_class = KeyValueStoreSerializer
    queryset = KeyValueStore.objects.all()
    filter_fields = ('key', )


class DjangoChannelsTestView(View):
    def get(self, request):
        async_to_sync(get_channel_layer().group_send)(
            'everybody', {
                'type': 'message',
                'topic': 'test',
                'data': ugettext('Hello everybody.')
            }
        )
        return HttpResponse(_('Message was sent to everybody.'))


class React(TemplateView):
    template_name = 'basic.html'
