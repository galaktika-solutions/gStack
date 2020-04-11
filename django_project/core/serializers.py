from rest_framework.serializers import ModelSerializer

from .models import KeyValueStore


class KeyValueStoreSerializer(ModelSerializer):
    """ """
    class Meta:
        model = KeyValueStore
        fields = ('id', 'key', 'value')
