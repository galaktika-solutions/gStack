from django.apps import AppConfig


class Config(AppConfig):
    name = 'myuser'
    models_to_register = [('User', [])]
