from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import KeyValueStore


class KeyValueStoreSerializer(ModelSerializer):
    """ """
    api_detail_url = serializers.SerializerMethodField()

    class Meta:
        model = KeyValueStore
        fields = ('api_detail_url', 'id', 'key', 'value')

    def get_api_detail_url(self, obj):
        return reverse('api:key_value_store-detail', kwargs={'pk': obj.pk})

    @staticmethod
    def get_select_related():
        return [None]

    @staticmethod
    def get_prefetch_related():
        return []
