from core.apps import AuditLogAppConfig

models_to_register = [
    ('Permission', []),
    ('Group', []),
    ('GroupPermission', []),
    ('User', []),
    ('UserPermission', []),
    ('Membership', []),
]


class Config(AuditLogAppConfig):
    name = 'myuser'
    models_to_register = models_to_register
