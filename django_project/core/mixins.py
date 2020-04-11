from rest_framework.response import Response
from rest_framework.decorators import action


class ModelInfoMixin(object):
    @action(methods=['get'], detail=False)
    def model_info(self, request):
        def format_choice(choices):
            response = []
            for row in choices:
                response.append({'id': row[0], 'text': row[1]})
            return response

        data = {}
        fields_tmp = list(self.queryset.model._meta.fields)
        fields_tmp += self.queryset.model._meta.many_to_many
        for field in fields_tmp:
            data[str(field.name)] = {}
            if field.choices:
                data[str(field.name)]['choices'] = format_choice(field.choices)
            data[str(field.name)]['help_text'] = field.help_text
            data[str(field.name)]['verbose_name'] = field.verbose_name
        return Response(data)

    @action(methods=['GET'], detail=False)
    def schema(self, request):
        meta = self.metadata_class()
        data = meta.get_serializer_info(self.get_serializer())
        return Response(data)
