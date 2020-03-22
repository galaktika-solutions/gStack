import logging
import sys
import datetime
from mimetypes import guess_type
from django.core.mail.backends.smtp import EmailBackend
import django
django.setup()

from email_backend.backend import CustomEmailMessage
from email_backend.models import SentEmails
LOG = logging.getLogger('django.mailsender')


class DetailedEmailBackend(EmailBackend):
    def send_messages(self, email_messages):
        """
        Sends one or more EmailMessage objects and returns a list with success or
        failure flags.
        """
        if not email_messages:
            return []
        with self._lock:
            new_conn_created = self.open()
            if not self.connection:
                return [False] * len(email_messages)
            success_list = []
            for message in email_messages:
                sent = self._send(message)
                if sent:
                    success_list.append(True)
                else:
                    success_list.append(False)
            if new_conn_created:
                self.close()
        return success_list


if __name__ == '__main__':
    # select unsent messages
    object_list = list(
        SentEmails.objects
        .filter(sent_at__isnull=True)
        .prefetch_related('sentemailsattachment_set')
    )
    if not object_list:
        LOG.info('No new messages')
        sys.exit(0)

    LOG.info(f'Messages to send: {[m.id for m in object_list]}')
    email_messages = []
    for msg in object_list:
        m = CustomEmailMessage(
            subject=msg.subject,
            body=msg.body,
            from_email=msg.from_address,
            content_subtype=msg.content_subtype,
            to=[x for x in msg.to_address.split(', ') if x],
            bcc=[x for x in msg.bcc_address.split(', ') if x],
            cc=[x for x in msg.cc_address.split(', ') if x]
        )
        for attachment in msg.sentemailsattachment_set.all():
            m.attach(
                f'{attachment.name}',
                open(attachment.attachment.path, 'rb').read(),
                guess_type(attachment.attachment.name)[0]
            )

        m.restrict_recipients()
        email_messages.append(m)

    backend = DetailedEmailBackend()
    success_list = backend.send_messages(email_messages)
    for m, s in list(zip(object_list, success_list)):
        if s:
            m.sent_at = datetime.datetime.now()
            m.save()
            LOG.info('Mail sent: %s' % m.id)
        else:
            LOG.warning('Mail error: %s' % m.id)
