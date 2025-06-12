from django.apps import AppConfig

class UsersConfig(AppConfig):  # name of the config class doesn't matter much
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # ✅ this MUST match your app folder name exactly
