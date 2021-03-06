import datetime
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from .pdf_converter import render_to_pdf


def hello_world_pdf(ctx, language="en", preview=True, user=None):
    translation.activate(language)
    ctx['now'] = datetime.datetime.now()
    email = None
    if not preview and not user.is_anonymous:
        email = {
            'subject': _('Hello World'),
            'to': [user.email, ]
        }

    return render_to_pdf(
        template_src='pdf/hello_world.tex',
        filename='hello_world',
        context_dict=ctx,
        email=email
    )
