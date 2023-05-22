from django.apps import AppConfig


class IqcInfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.IQC_info"

    def ready(self):
        pass
