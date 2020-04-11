from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.reverse import reverse


class UserSerializer(ModelSerializer):
    """ """
    api_detail_url = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('api_detail_url', 'id', 'email', )

    def get_api_detail_url(self, obj):
        return reverse('api:user-detail', kwargs={'pk': obj.pk})

    @staticmethod
    def get_select_related():
        return [None]

    @staticmethod
    def get_prefetch_related():
        return []
