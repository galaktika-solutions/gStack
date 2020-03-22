from django.contrib import admin
from django.contrib.auth.models import Group
from auditlog.models import LogEntry
from auditlog.admin import LogEntryAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
import json

from .models import KeyValueStore


@admin.register(KeyValueStore)
class KeyValueStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value')
    list_display_links = list_display


class LogEntryAdminV2(LogEntryAdmin):
    def msg_short(self, obj):
        if obj.action == 2 or obj.action == 0:
            return ''  # delete and create
        return super().msg_short(obj)

    def resource_url(self, obj):
        return mark_safe(super().resource_url(obj))

    def user_url(self, obj):
        return mark_safe(super().user_url(obj))

    def msg(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        msg = '''
            <table>
                <tr style="border-bottom: black 1px solid;">
                    <th style="min-width: 20px; font-weight: 700"><b>#</b></th>
                    <th style="min-width: 100px;font-weight: 700">Field</th>
                    <th style="min-width: 100px;font-weight: 700">From</th>
                    <th style="min-width: 100px;font-weight: 700">To</th>
                </tr>
        '''
        for i, field in enumerate(sorted(changes), 1):
            value = [i, field] + changes[field]
            msg += format_html(
                '''
                    <tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                    </tr>
                ''',
                *value
            )

        msg += '</table>'
        return mark_safe(msg)

    list_select_related = ['content_type', 'actor']
    search_fields = ['actor__first_name', 'actor__last_name', 'actor__email']
    list_per_page = 20
    fieldsets = None


# we don't need the default django group
admin.site.unregister(Group)
admin.site.unregister(LogEntry)  # unregister the default admin version of auditlog
admin.site.register(LogEntry, LogEntryAdminV2)
