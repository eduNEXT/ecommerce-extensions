# -*- coding: utf-8 -*-
"""
This file contains django context_processors needed by edunext.
"""
import logging

from eco_tenant.models import SiteOptions

LOG = logging.getLogger(__name__)


def theme_options(request):
    """
    This context processor lets us add extra context to the themeable templates
    in a way that is unobtrusive and easy to migrate between releases
    """
    try:
        options = request.site.siteoptions.options_blob
    except SiteOptions.DoesNotExist:  # pylint: disable=no-member
        LOG.warning("The site %s has no associated SiteOptions register.", request.site.domain)
        options = {}

    try:
        site_theme_name = request.site_theme.theme_dir_name
    except AttributeError:
        site_theme_name = None

    return {
        "theme_dir_name": site_theme_name,
        "site_configuration": request.site.siteconfiguration,
        "options": options,
    }
