from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action

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
    queryset = (
        get_user_model().objects.all()
        .select_related(*serializer_class.get_select_related())
        .prefetch_related(*serializer_class.get_prefetch_related())
    )

    @action(methods=['get'], detail=False)
    def profile(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, context={'request': request})
        return Response(serializer.data)
