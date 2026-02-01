from django.apps import AppConfig

class VisualizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visualizer'

    def ready(self):
        from django.contrib.auth.models import User

        if not User.objects.filter(username="demo").exists():
            User.objects.create_user(
                username="demo",
                password="demo123"
            )
