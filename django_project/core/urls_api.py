from rest_framework.routers import SimpleRouter

from .views import KeyValueStoreViewset

SharedRouter = SimpleRouter()
SharedRouter.register(
    'key_value_store',
    KeyValueStoreViewset,
    basename='key_value_store'
)

urlpatterns = SharedRouter.urls
