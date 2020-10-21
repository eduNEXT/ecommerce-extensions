"""
App configuration for eco_tenant.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EcoTenantConfig(AppConfig):
    """
    Django eduNEXT e-commerce tenant configuration.
    """
    name = 'eco_tenant'
    label = 'edunext'
    verbose_name = 'eduNEXT tenant'
