import os.path
import codecs
from collections import OrderedDict
from django.contrib.staticfiles import finders
from rest_framework.relations import PrimaryKeyRelatedField
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


class DictPKRelatedField(PrimaryKeyRelatedField):
    """
    This custom REST Frameworks field represents the FK relationship with
    the given method_name(function), but otherwise work like the
    PrimaryKeyRelatedField.

    Example:
    --- serializer FIELD ---
    account = DictPKRelatedField(
        queryset=Account.objects.all(), method_name='account_to_rep')

    --- serializer METHOD ---
    def account_to_rep(self, obj):
        return {'id': obj.id, 'name': obj.name}
    """
    def __init__(self, method_name, model_field=None, **kwargs):
        self.method_name = method_name
        super(DictPKRelatedField, self).__init__(**kwargs)
        if model_field:
            self.label = kwargs.get('label', model_field.verbose_name)
            self.help_text = kwargs.get('help_text', model_field.help_text)
            self.required = kwargs.get(
                'required',
                model_field.null is False and kwargs.get('read_only') is False
            )
            self.allow_null = kwargs.get('allow_null', model_field.null)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return getattr(self.parent, self.method_name)(value)


def csv_field(header_name):
    def decorator(fnc):
        fnc._header_name = header_name
        return fnc
    return decorator


class CSVDataRow(object):
    @classmethod
    def _fields(cls):
        fields = [f for f in cls.__dict__.values()]
        fields = [f for f in fields if hasattr(f, '_header_name')]
        return fields

    @classmethod
    def _header(cls):
        return [f._header_name for f in cls._fields()]

    def __getattribute__(self, field):
        attr = object.__getattribute__(self, field)
        if hasattr(attr, '_header_name'):
            return attr()
        return attr

    def _json(self):
        return OrderedDict([(f._header_name, f(self)) for f in self._fields()])

    def _list(self):
        return [f(self) for f in self._fields()]
