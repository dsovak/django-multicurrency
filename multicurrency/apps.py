from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MulticurrencyConfig(AppConfig):
    name = 'multicurrency'
    verbose_name = _('Multicurrency')