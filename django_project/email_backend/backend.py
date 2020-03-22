import os
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import EmailMessage
from django.contrib.auth import get_user_model
from django.conf import settings

from .models import SentEmails, SentEmailsAttachment


class CustomEmailMessage(EmailMessage):
    content_subtype = 'html'

    def __init__(self, **kwargs):
        content_subtype = kwargs.pop('content_subtype', 'html')
        super().__init__(**kwargs)
        self.content_subtype = content_subtype
        self.active_emails = set(
            get_user_model().objects
            .filter(is_active=True)
            .values_list('email', flat=True)
        )

    def filter_email_adresses(self, emails):
        return set(emails) & self.active_emails

    def restrict_recipients(self):
        if os.environ.get('REWRITE_RECIPIENTS'):
            self.to = [os.environ.get('REWRITE_RECIPIENTS')]
            self.cc = []
            self.bcc = []
        else:
            self.to = self.filter_email_adresses(self.to)
            self.cc = self.filter_email_adresses(self.cc)
            self.bcc = self.filter_email_adresses(self.bcc)


class CustomEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        objects = []
        for m in email_messages:

            # modify the subject if it's not the live system
            subject = m.subject
            if not settings.PROD:
                subject = '%s %s' % (settings.EMAIL_SUBJECT_PREFIX, m.subject)

            #
            obj = SentEmails.objects.create(
                subject=subject,
                body=m.body,
                to_address=', '.join(m.to),
                cc_address=', '.join(m.cc),
                bcc_address=', '.join(m.bcc),
                from_address=m.from_email,
                content_subtype=m.content_subtype
            )
            for attachment in m.attachments:
                # attachment is a tuple (filename, file, type)
                SentEmailsAttachment.objects.create(
                    sent_email=obj,
                    attachment=attachment[1],
                    name=attachment[0]
                )
            objects.append(obj)
        return len(email_messages)
