from django.apps import AppConfig


class TechsupportInfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.TechSupport_info"

    def ready(self):
        pass
