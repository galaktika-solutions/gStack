import datetime
import csv
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer
from core.mixins import ModelInfoMixin
from core.utils import CSVDataRow, csv_field


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

    @action(methods=['get'], detail=False)
    def csv(self, request):
        class UserCSV(CSVDataRow):
            def __init__(self, data):
                self.data = data

            @csv_field("Id")
            def slug(self):
                return self.data['id']

            @csv_field("Email")
            def status(self):
                return self.data['email']

        qs = self.get_queryset().values('id', 'email')
        today = datetime.datetime.utcnow().date()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'filename="users-{today}.csv"'
        response.write(b"\xef\xbb\xbf")
        writer = csv.writer(response)
        writer.writerow(UserCSV._header())
        for item in qs:
            writer.writerow(UserCSV(data=item)._list())
        return response
