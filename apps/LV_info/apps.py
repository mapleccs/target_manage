from django.apps import AppConfig


class TargetInfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.LV_info"

    def ready(self):
        pass
