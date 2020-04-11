from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from .serializers import UserSerializer
from core.mixins import ModelInfoMixin


class UserViewset(
    ModelInfoMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    """ Contains informations regarding the users. """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
