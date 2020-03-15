from django.urls import path

from .views import HelloWorldTestPDFView

urlpatterns = [
    path(
        'hello_world/',
        HelloWorldTestPDFView.as_view(),
        name="account_approval_autocomplete"
    ),
]
