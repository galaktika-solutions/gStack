from core.apps import AuditLogAppConfig


class Config(AuditLogAppConfig):
    name = 'myuser'
    models_to_register = [
        ('Permission', []),
        ('Group', []),
        ('GroupPermission', []),
        ('User', []),
        ('UserPermission', []),
        ('Membership', []),
    ]
