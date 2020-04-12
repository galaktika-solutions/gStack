from rest_framework.routers import SimpleRouter

from .views import UserViewset

SharedRouter = SimpleRouter()
SharedRouter.register(
    'user',
    UserViewset,
    basename='user'
)

urlpatterns = SharedRouter.urls
