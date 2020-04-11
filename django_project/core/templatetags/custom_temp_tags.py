import re
import threading
from django import template
from django.utils.encoding import force_text
from django.utils.functional import lazy
from bleach.sanitizer import (
    ALLOWED_ATTRIBUTES,
    ALLOWED_PROTOCOLS,
    ALLOWED_STYLES,
    Cleaner,
    BleachSanitizerFilter
)
bleach_lock = threading.Lock()  # bleach is not thread-safe
register = template.Library()


class LazyCleaner(Cleaner):
    """Allows lazy objects."""
    def clean(self, text):
        filtered = BleachSanitizerFilter(
            source=self.walker(self.parser.parseFragment(str(text))),
            attributes=self.attributes,
            strip_disallowed_elements=self.strip,
            strip_html_comments=self.strip_comments,
            allowed_elements=self.tags,
            allowed_css_properties=self.styles,
            allowed_protocols=self.protocols,
            allowed_svg_properties=[],
        )
        for filter_class in self.filters:
            filtered = filter_class(source=filtered)
        return self.serializer.render(filtered)


lazy_cleaner_instance = LazyCleaner(
    tags=[
        'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li',
        'ol', 'strong', 'ul', 'br'
    ],
    attributes=ALLOWED_ATTRIBUTES,
    styles=ALLOWED_STYLES,
    protocols=ALLOWED_PROTOCOLS,
    strip=True,
    strip_comments=True
)


def bleach_clean(s):
    with bleach_lock:
        return lazy_cleaner_instance.clean(s)


bleach_clean_lazy = lazy(bleach_clean, str)


@register.filter
def bleach_escape(text):
    return bleach_clean_lazy(text)


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
