from django.apps import AppConfig
# Ammend apps (ensures text is translated to different languages)
from django.utils.translation import gettext_lazy as _ 

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.users'
    verbose_name = _("Users")
