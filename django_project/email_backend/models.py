from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime


def media_file_path(instance, filename):
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    now = now.strftime('%s')
    name = filename.split('/')
    file_type = name[len(name) - 1]
    return f'email_attachment/{year}/{now}.{file_type}'


class SentEmails(models.Model):
    '''
    | Every email what we sent out from the system, goes throught this model.
    | There is a service called mailsender which sends out the emails in the end.
    '''
    subject = models.CharField(_('Email subject'), max_length=1000)
    body = models.TextField(_('Email body'), blank=True)
    from_address = models.TextField()
    to_address = models.TextField()
    cc_address = models.TextField(blank=True)
    bcc_address = models.TextField(blank=True)
    content_subtype = models.CharField(max_length=10, default='html')
    sent_at = models.DateTimeField(null=True, blank=True, db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = _("Sent Emails")

    def __str__(self):
        return f'#{self.id} - {self.subject}'


class SentEmailsAttachment(models.Model):
    ''' One email can have multiple attachments, hew we store it. '''
    sent_email = models.ForeignKey(SentEmails, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=media_file_path, max_length=1000)
    name = models.CharField(_('Name'), max_length=200)
