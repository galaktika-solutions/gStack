import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.core.mail import mail_admins
from django.http import HttpResponse


class DemoIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'demo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if os.environ.get('ENV', 'PROD') != 'DEV':
            build_js = os.listdir('static/demo/dist')
        else:
            build_js = os.listdir('django_project/demo/static/demo/dist')
        build_js = [f for f in build_js if f.endswith('.js')][0]
        context['build_js'] = build_js
        return context


class TestEmailView(LoginRequiredMixin, View):
    def post(self, request):
        mail_admins('test email', 'Hi, Admin! This worked...')
        return HttpResponse('OK')


class IntentionallyBrokenView(View):
    def get(self, request):
        raise Exception('This view is intentionally broken.')
