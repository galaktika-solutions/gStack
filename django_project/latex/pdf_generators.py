import datetime
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from .pdf_converter import render_to_pdf


def hello_world(ctx, language, preview, user=None):
    translation.activate(language)
    ctx['now'] = datetime.datetime.now()
    subject = _('Hello World')
    file_name = 'hello_world'

    email = None
    if preview is False and user is not None:
        email = {
            'subject': subject,
            'to': [user.email, ]
        }

    return render_to_pdf('hello_world.tex', file_name, ctx, email)
