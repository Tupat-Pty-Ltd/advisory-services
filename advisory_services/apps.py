from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """
    """
    name = 'advisory_services'
    verbose_name = "Advisory Services"

    def ready(self):
        pass
