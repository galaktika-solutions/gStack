from rest_framework.routers import SimpleRouter

from .views import UserViewset

SharedRouter = SimpleRouter()
SharedRouter.register(
    'user',
    UserViewset,
    base_name='user'
)

urlpatterns = SharedRouter.urls
