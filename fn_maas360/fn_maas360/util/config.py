# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_maas360"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_maas360]
# Authentication settings
maas360_host_url=
maas360_billing_id=
maas360_platform_id=
maas360_app_id=
maas360_app_version=
maas360_app_access_key=
maas360_username=
maas360_password=

# Optional - If you are seeing read timeout=30 error you can override the timeout value
#maas360_request_timeout=60

# Basic Search Fn settings
# Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250. Default value: 250
maas360_basic_search_page_size=25
# Optional - Match 0 (Default) indicates Partial match for Device Name, Username, Phone Number. Match 1 indicates Exact match.
#maas360_basic_search_match=0
# Optional - Sort attribute. Possible values: lastReported (Default) or installedDate
#maas360_basic_search_sort_attribute=lastReported
# Optional - Sort Order. Possible values: asc or dsc (Default)
#maas360_basic_search_sort_order=dsc

# Wipe device settings
# Required - Whether to notify the administrator on successful device wipe. “yes” value enables this flag
maas360_wipe_device_notify_me=Yes
# Required - Whether to notify the user on successful device wipe. “yes” value enables this flag.
maas360_wipe_device_notify_user=No
# Required - Comma separated list of other email addresses to notify on successful device wipe
maas360_wipe_device_notify_others=email1, email2
    """
    return config_data
