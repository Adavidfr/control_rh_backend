# rh/apps.py
from django.apps import AppConfig


class RhConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rh'
    verbose_name = 'Control de Recursos Humanos'
