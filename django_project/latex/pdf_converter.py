import os
import tempfile
from subprocess import Popen, PIPE
from shutil import rmtree
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings
from django.core.files import File
from django.utils.html import escape
from django.core.mail import EmailMessage
TMP_DIR = settings.MEDIA_ROOT + 'latex/'


def render_to_pdf(template_src, filename, context_dict, email=None):
    context_dict['LATEX_STATIC_ROOT'] = settings.LATEX_STATIC_ROOT
    context_dict['ENV'] = settings.ENV
    context_dict['PROD'] = settings.PROD
    template = get_template(template_src)
    rendered_tpl = str(template.render(context_dict))
    if not os.path.isdir(TMP_DIR):
        os.mkdir(TMP_DIR)
    tempdir = tempfile.mkdtemp(dir=TMP_DIR)
    tex_file = os.path.join(tempdir, filename + '.tex')
    with open(tex_file, 'w') as f:
        f.write(rendered_tpl)
    f.close()

    source = '/'.join(template.origin.name.split('/')[0:-1]) + '/'
    command = ['lualatex', '-output-directory', tempdir, tex_file]
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=source)
    out, err = process.communicate()
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=source)
    out, err = process.communicate()
    pdf = os.path.join(tempdir, filename + '.pdf')
    all_ok = process.returncode == 0 and os.path.isfile(pdf)

    if email and all_ok:
        EmailMessage(
            subject=email['subject'],
            body=email.get('body', ''),
            to=email['to'],
            attachments=[(f'{filename}.pdf', File(open(pdf, 'rb')), 'application/pdf')]
        ).send()
        response = HttpResponse('The email was sent!')
    elif email is None and all_ok:
        with open(pdf, 'rb') as f:
            pdf = f.read()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="' + filename + '.pdf"'
        response.write(pdf)
    elif not settings.DEBUG:
        raise Exception('Something went wrong during the pdf generation!')
    else:
        text = escape(out).replace('\\n', '<br/>')
        response = HttpResponse(f"<pre>{text}</pre>")

    if settings.DEBUG:
        log_file = os.path.join(tempdir, filename + '.log')
        with open(log_file, 'r') as f:
            print(f.read())

    rmtree(tempdir)
    return response
