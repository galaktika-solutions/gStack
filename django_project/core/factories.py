import factory
from factory.fuzzy import FuzzyText

from .models import KeyValueStore


class KeyValueStoreFactory(factory.django.DjangoModelFactory):
    key = FuzzyText(length=20)

    class Meta:
        model = KeyValueStore
        django_get_or_create = ('key', )
