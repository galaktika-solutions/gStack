import threading
from django.conf import settings
from django.utils.functional import lazy
from bleach.sanitizer import (
    ALLOWED_ATTRIBUTES,
    ALLOWED_PROTOCOLS,
    ALLOWED_STYLES,
    ALLOWED_TAGS,
    Cleaner,
    BleachSanitizerFilter
)
bleach_lock = threading.Lock()  # bleach is not thread-safe


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
original_lazy_cleaner_instance = LazyCleaner(
    tags=ALLOWED_TAGS,
    attributes=ALLOWED_ATTRIBUTES,
    styles=ALLOWED_STYLES,
    protocols=ALLOWED_PROTOCOLS,
    strip=True,
    strip_comments=True
)


def bleach_clean(s):
    with bleach_lock:
        return lazy_cleaner_instance.clean(s)


def original_bleach_clean(s):
    with bleach_lock:
        return original_lazy_cleaner_instance.clean(s)


bleach_clean_lazy = lazy(bleach_clean, str)
original_bleach_clean_lazy = lazy(original_bleach_clean, str)


class NoJsonPaginationMixin(object):
    def list(self, request, *args, **kwargs):
        size = request.GET.get(settings.REST_FRAMEWORK['PAGINATE_BY_PARAM'])
        if request.accepted_media_type != 'text/html' and size is None:
            self.paginate_queryset = lambda x: None
        return super(NoJsonPaginationMixin, self).list(
            request, *args, **kwargs)
