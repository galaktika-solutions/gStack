from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.views.decorators.csrf import ensure_csrf_cookie

from .views import DjangoChannelsTestView, React


api_patterns = [
    path("", include("core.urls_api")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explorer/', include('explorer.urls')),
    path('api/', include((api_patterns, 'api'), namespace='api')),
    path('rest-auth/', include('rest_auth.urls')),
    path('django-channels/test/', DjangoChannelsTestView.as_view()),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("", ensure_csrf_cookie(React.as_view()), name="react"),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
