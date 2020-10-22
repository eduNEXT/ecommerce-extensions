"""
App configuration for tenant.
"""
from __future__ import unicode_literals

from django.apps import AppConfig


class TenantConfig(AppConfig):
    """
    Django eduNEXT e-commerce tenant configuration.
    """
    name = 'ecommerce_extensions.tenant'
    label = 'edunext'
    verbose_name = 'eduNEXT tenants'
