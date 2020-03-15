import re
from django import template
from django.utils.encoding import force_text
from core.mixins import bleach_clean_lazy
register = template.Library()


@register.filter
def tex_escape(text):
    ''' The message escaped to appear correctly in LaTeX '''
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless',
        '>': r'\textgreater',
    }

    keys = sorted(conv.keys(), key=lambda item: - len(item))
    regex = re.compile('|'.join(re.escape(str(key)) for key in keys))
    return regex.sub(lambda match: conv[match.group()], force_text(text))


@register.filter
def bleach_escape(text):
    return bleach_clean_lazy(text)
