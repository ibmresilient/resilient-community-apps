# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_maas360"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_maas360]
# Authentication settings
# -----------------------
maas360_host_url=
maas360_billing_id=
maas360_platform_id=
maas360_app_id=
maas360_app_version=
maas360_app_access_key=
maas360_username=
maas360_password=
maas360_auth_url=/auth-apis/auth/1.0/authenticate/

# Basic Search settings
# ---------------------
# Required
# Basic search url
maas360_basic_search_url=/device-apis/devices/2.0/search/customer/
# Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250 (Default)
maas360_basic_search_page_size=25

# Optional
# Match 0 (Default) indicates Partial match for Device Name, Username, Phone Number. Match 1 indicates Exact match.
maas360_basic_search_match=0
# Sort attribute. Possible values: lastReported (Default)  or installedDate
maas360_basic_search_sort_attribute=lastReported
# Sort Order. Possible values: asc  or dsc (Default)
maas360_basic_search_sort_order=dsc
    """
    return config_data
