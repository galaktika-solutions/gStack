from django.conf import settings


def extra_context(request):
    return dict(
        servername=settings.BASE_URL,
        PROD=settings.PROD,
        VERSION=settings.VERSION
    )
