from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    path('test-email/', views.TestEmailView.as_view(), name='test-email'),
    path('broken/', views.IntentionallyBrokenView.as_view(), name='broken')
]
