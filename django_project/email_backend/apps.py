from core.apps import AuditLogAppConfig


class Config(AuditLogAppConfig):
    name = 'email_backend'
    models_to_register = [
        ('SentEmails', ['create_time', ]),
        ('SentEmailsAttachment', []),
    ]
