from django.views import View

from .pdf_generators import hello_world_pdf


class HelloWorldTestPDFView(View):
    def get(self, request):
        if request.GET.get('email'):
            return hello_world_pdf(
                ctx={},
                language=request.GET.get('language', 'en'),
                preview=False,
                user=request.user
            )
        return hello_world_pdf(
            ctx={},
            language=request.GET.get('language', 'en'),
            preview=True,
            user=request.user
        )
