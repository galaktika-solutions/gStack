from django.contrib import admin

from .models import KeyValueStore


@admin.register(KeyValueStore)
class KeyValueStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value')
    list_display_links = list_display
