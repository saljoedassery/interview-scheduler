import sys

from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler'

    def ready(self):
        super().ready()
        if 'runserver' not in sys.argv:
            return True
        from scheduler.initialize import create_users
        create_users()
