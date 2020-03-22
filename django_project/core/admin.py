from django.contrib import admin
from django.contrib.auth.models import Group

from .models import KeyValueStore


@admin.register(KeyValueStore)
class KeyValueStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value')
    list_display_links = list_display


# we don't need the default django group
admin.site.unregister(Group)
