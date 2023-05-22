from django.apps import AppConfig


class OqcInfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.OQC_info"

    def ready(self):
        pass
