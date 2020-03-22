from django.apps import AppConfig


class AuditLogAppConfig(AppConfig):
    name = None
    models_to_register = None

    def ready(self):
        from auditlog.registry import auditlog
        from django.apps import apps

        for row in self.models_to_register:
            obj = apps.get_model(self.name, row[0])
            exclude = [x for x in obj._meta.fields_map]
            exclude += row[1]
            auditlog.register(obj, exclude_fields=exclude)


class Config(AuditLogAppConfig):
    name = 'core'
    models_to_register = [
        ('KeyValueStore', []),
    ]
