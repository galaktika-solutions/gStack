from django.urls import path, include
from django.contrib import admin
from django.apps import apps
from rest_framework.routers import DefaultRouter
from django.views.i18n import JavaScriptCatalog

from .views import KeyValueStoreViewset, PublishTranslations


router = DefaultRouter()
router.register('key-value-store', KeyValueStoreViewset)

urlpatterns = [
    path('', include('demo.urls', namespace='demo')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('explorer/', include('explorer.urls')),
    path('api/', include(router.urls)),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('django-channels/test/', DjangoChannelsTestView.as_view()),
    path('rosetta/', include('rosetta.urls')),
    path(
        'publish-translations/',
        PublishTranslations.as_view(),
        name='publish_translations'
    ),
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        'jsi18n/',
        JavaScriptCatalog.as_view(),
        name='javascript-catalog'
    ),
]

if apps.is_installed('debug_toolbar'):
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
