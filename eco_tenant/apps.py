"""
App configuration for eco_tenant.
"""
from __future__ import unicode_literals

from django.apps import AppConfig
from django.core.signals import request_started


class EcoTenantConfig(AppConfig):
    """
    Django eduNEXT e-commerce tenant configuration.
    """
    name = 'eco_tenant'
    label = 'edunext'
    verbose_name = 'eduNEXT tenant'

    def ready(self):
        """
        Method to perform actions after apps registry is ended
        """
        from eco_tenant.receivers import update_tenant_settings
        request_started.connect(update_tenant_settings)
