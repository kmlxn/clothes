from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CatalogConfig(AppConfig):
    name = "catalog"
    verbose_name = _("Clothes Catalog")

    def ready(self):
        from . import signals
