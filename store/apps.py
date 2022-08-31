from django.apps import AppConfig
from django.db.models.signals import post_save


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        from . import signals
        # post_save.connect(signals.post_listener, dispatch_uid="uid")
