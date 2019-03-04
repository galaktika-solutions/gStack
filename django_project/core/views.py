import os

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
# from django.http import HttpResponse
# from django.views import View
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
#
# # Project imports
from .models import KeyValueStore
from .serializers import KeyValueStoreSerializer
# from .mixins import NoJsonPaginationMixin


class KeyValueStoreViewset(ModelViewSet):
    """General application settings"""

    serializer_class = KeyValueStoreSerializer
    queryset = KeyValueStore.objects.all()
    filter_fields = ('key', )
    permission_classes = (DjangoModelPermissions,)


class PublishTranslations(View):
    def get(self, request):
        try:
            import uwsgi
            uwsgi.reload()
        except ImportError:
            pass  # Probably django was started in DEV mode
        return HttpResponseRedirect(reverse('rosetta-old-home-redirect'))


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if os.environ.get('ENV', 'PROD') != 'DEV':
            build_js = os.listdir('static/demo/dist')
        else:
            build_js = os.listdir('django_project/demo/static/demo/dist')
        build_js = [f for f in build_js if f.endswith('.js')][0]
        context['build_js'] = build_js
        return context


# class DjangoChannelsTestView(View):
#     def get(self, request):
#         async_to_sync(get_channel_layer().group_send)(
#             'everybody', {
#                 'type': 'message',
#                 'topic': 'test',
#                 'data': 'Hello everybody.'
#             }
#         )
#         return HttpResponse('Message was sent to everybody.')
