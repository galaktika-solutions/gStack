from django.urls import path, include
from django.contrib import admin
from django.conf import settings
# from rest_framework.routers import SimpleRouter
from django.views.i18n import JavaScriptCatalog

# from .views import KeyValueStoreViewset, DjangoChannelsTestView
# from .routers import ContainerRouter

# core viewsets
# SharedRouter = SimpleRouter()
# SharedRouter.register(
#     r'key_value_store',
#     KeyValueStoreViewset,
#     base_name='key_value_store'
# )

# Register every other application SharedRouter in here
# Example:
# from pydoc import locate
# router.register_router(locate('other.urls.SharedRouter'))
# router = ContainerRouter()
# router.register_router(SharedRouter)
#
# api_patterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', include('demo.urls', namespace='demo')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # path('explorer/', include('explorer.urls')),
    # path('api/', include((api_patterns, 'api'), namespace='api')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('django-channels/test/', DjangoChannelsTestView.as_view()),
    # path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        'jsi18n/',
        JavaScriptCatalog.as_view(packages=[()]),
        name='javascript-catalog'
    ),
]

if hasattr(settings, 'DEBUG_TOOLBAR_CONFIG'):
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
