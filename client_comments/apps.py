from django.apps import AppConfig


class ClientCommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_comments'

    def ready(self):
        import client_comments.signals
