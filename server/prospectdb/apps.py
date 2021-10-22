from django.apps import AppConfig


class ProspectdbConfig(AppConfig):
    name = 'prospectdb'

    def ready(self):
        from . import signals
