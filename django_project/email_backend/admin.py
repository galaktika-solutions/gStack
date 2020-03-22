from django.contrib import admin
from django.utils.safestring import mark_safe

from email_backend import models


@admin.register(models.SentEmails)
class SentEmailsAdmin(admin.ModelAdmin):
    def display_body(self, obj):
        return mark_safe(str(obj.body))

    list_display = ('id', 'subject', 'from_address', 'create_time', 'sent_at')
    list_display_links = list_display
    search_fields = ['id', 'subject', 'from_address']
    readonly_fields = ('display_body', )


@admin.register(models.SentEmailsAttachment)
class SentEmailsAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sent_email', 'attachment')
    list_display_links = list_display
    search_fields = ['id', 'sent_email_id', ]
    raw_id_fields = ('sent_email', )
    autocomplete_lookup_fields = {'fk': list(raw_id_fields)}
