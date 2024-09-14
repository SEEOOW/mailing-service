from django.apps import AppConfig
# from mailing.services import start_scheduler


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    # def ready(self):
    #     start_scheduler()
