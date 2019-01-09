from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.core.mail import mail_admins
from django.http import HttpResponse


class DemoIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'demo/index.html'


class TestEmailView(LoginRequiredMixin, View):
    def post(self, request):
        mail_admins('test email', 'Hi, Admin! This worked...')
        return HttpResponse('OK')


class IntentionallyBrokenView(View):
    def get(self, request):
        raise Exception('This view is intentionally broken.')
