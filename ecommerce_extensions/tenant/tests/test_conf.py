# -*- coding: utf-8 -*-
"""This module contains the test for conf.py file."""
from django.contrib.sites.models import Site
from django.test import TestCase
from django.test.utils import override_settings
from mock import MagicMock, patch

from ecommerce_extensions.tenant.conf import settings as SiteSettings
from ecommerce_extensions.tenant.models import TenantOptions


def _make_site(blob_str=None, site_id=1):
    """
    Returns a site object. If blob_str is passed, a TenantOptions object
    related to the site is created or updated with the blob, otherwise,
    existent TenantOptions object for the site is deleted
    """
    site = Site.objects.get(id=site_id)

    if blob_str is not None:
        obj, _ = TenantOptions.objects.get_or_create(
            site=site
        )
        obj.options_blob = blob_str
        obj.save()
    else:
        TenantOptions.objects.filter(site=site).delete()

    return site


class EdunextConfTests(TestCase):
    """
    Test for Edunext site aware configurations
    """

    @override_settings(OSCAR_DEFAULT_CURRENCY="CAD")
    @patch("ecommerce_extensions.tenant.conf.get_current_request")
    def test_conf_without_TenantOptions(self, get_current_request_mock):
        """
        This method tests the desired behavior when the current site has
        no an associated TenantOptions register.

        Expected behavior:
            - SiteSetting returns default value.
        """
        request_mock = MagicMock()
        request_mock.site = _make_site()
        get_current_request_mock.return_value = request_mock

        self.assertEqual(SiteSettings.OSCAR_DEFAULT_CURRENCY, "CAD")

    @override_settings(OSCAR_DEFAULT_CURRENCY="COP")
    @patch("ecommerce_extensions.tenant.conf.get_current_request")
    def test_conf_with_tenantoptions_no_overide(self, get_current_request_mock):
        """
        This method tests the desired behavior when the current site has
        an associated TenantOptions register but the options has not been overridden.

        Expected behavior:
            - SiteSetting returns default value.
        """
        request_mock = MagicMock()
        site_options = {
            "ANY_OTHER_SETTING": "any_value"
        }
        request_mock.site = _make_site(site_options)
        get_current_request_mock.return_value = request_mock

        self.assertEqual(SiteSettings.OSCAR_DEFAULT_CURRENCY, "COP")

    @override_settings(OSCAR_DEFAULT_CURRENCY="USD")
    @patch("ecommerce_extensions.tenant.conf.get_current_request")
    def test_conf_with_tenantoptions_overide(self, get_current_request_mock):
        """
        This method tests the desired behavior when the current site has
        an associated TenantOptions register and the option has been overridden.

        Expected behavior:
            - SiteSetting returns default value.
        """
        request_mock = MagicMock()
        site_options = {
            "OSCAR_DEFAULT_CURRENCY": "BRL"
        }
        request_mock.site = _make_site(site_options)
        get_current_request_mock.return_value = request_mock

        self.assertEqual(SiteSettings.OSCAR_DEFAULT_CURRENCY, "BRL")
