import os.path
import codecs
from django.contrib.staticfiles import finders
from premailer import Premailer
SECRET_MOUNT = '/run/secrets/'


def read_secret(secret):
    with open(os.path.join(SECRET_MOUNT, secret)) as f:
        return f.read().rstrip('\r\n')


class ImprovedPremailer(Premailer):
    def _load_external(self, url):
        try:
            super()._load_external(url)
        except ValueError:
            finders.find('', all=True)
            processed = False
            for path in finders.searched_locations:
                stylefile = url
                if not os.path.isabs(stylefile):
                    stylefile = os.path.abspath(
                        os.path.join(path or '', stylefile)
                    )
                if os.path.exists(stylefile):
                    with codecs.open(stylefile, encoding='utf-8') as f:
                        css_body = f.read()
                    processed = True

            if not processed:
                raise ValueError(stylefile)
            return css_body
