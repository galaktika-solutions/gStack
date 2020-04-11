from django.conf import settings
from django.utils.encoding import force_text
from rest_framework.pagination import PageNumberPagination, _positive_int
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.metadata import SimpleMetadata
from rest_framework import serializers
from explorer.exporters import CSVExporter
from six import BytesIO


def extra_context(request):
    """ Add some exra info to the context_processor. """
    return dict(
        servername=settings.BASE_URL,
        PROD=settings.PROD,
        VERSION=settings.VERSION
    )


class CSVExporterBOM(CSVExporter):
    """ Add BOM character to the CSV export so it can show utf-8 characters. """
    def _get_output(self, res, **kwargs):
        csv_data = super(CSVExporterBOM, self)._get_output(res, **kwargs)
        csv_data_io = BytesIO()
        csv_data_io.write(b'\xef\xbb\xbf')
        csv_data_io.write(csv_data.getvalue().encode('utf-8'))
        return csv_data_io


class BrowsableAPIRendererWithoutForm(BrowsableAPIRenderer):
    """ Disable the FORM on the BrowsableAPIRenderer. """
    def show_form_for_method(self, view, method, request, obj):
        return False


class HTMLOnlyPagination(PageNumberPagination):
    """ Disable the pagination everywhere except for text/html. """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size_2(request)

        if request.accepted_media_type == 'text/html' or page_size:
            return super().paginate_queryset(queryset, request, view)

        return None

    def get_page_size_2(self, request):
        try:
            return _positive_int(
                request.query_params[self.page_size_query_param],
                strict=True,
                cutoff=self.max_page_size
            )
        except (KeyError, ValueError):
            return None


class ImprovedMetadata(SimpleMetadata):
    """
    | We want to see the choices all the time even when the field is read_only.
    | We use the same code as the original except the read_only check.
    """
    def get_field_info(self, field):
        field_info = super().get_field_info(field)
        if (
            not isinstance(
                field,
                (serializers.RelatedField, serializers.ManyRelatedField)
            )
            and hasattr(field, 'choices')
        ):
            field_info['choices'] = [
                {
                    'value': choice_value,
                    'display_name': force_text(choice_name, strings_only=True)
                }
                for choice_value, choice_name in field.choices.items()
            ]
        return field_info
