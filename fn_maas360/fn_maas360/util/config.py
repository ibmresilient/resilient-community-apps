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
maas360_auth_url=/auth-apis/auth/1.0/authenticate/

# Basic Search Fn settings
maas360_basic_search_url=/device-apis/devices/2.0/search/customer/
# Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250. Default value: 250
maas360_basic_search_page_size=25
# Optional - Match 0 (Default) indicates Partial match for Device Name, Username, Phone Number. Match 1 indicates Exact match.
#maas360_basic_search_match=0
# Optional - Sort attribute. Possible values: lastReported (Default) or installedDate
#maas360_basic_search_sort_attribute=lastReported
# Optional - Sort Order. Possible values: asc or dsc (Default)
#maas360_basic_search_sort_order=dsc

# Action Fn settings
maas360_locate_device_url=/device-apis/devices/1.0/locateDevice/
maas360_get_software_installed_url=/device-apis/devices/1.0/softwareInstalled/
maas360_lock_device_url=/device-apis/devices/1.0/lockDevice/
maas360_wipe_device_url=/device-apis/devices/1.0/wipeDevice/
# Required - Whether to notify the administrator on successful device wipe. “yes” value enables this flag
maas360_wipe_device_notify_me=Yes
# Required - Whether to notify the user on successful device wipe. “yes” value enables this flag.
maas360_wipe_device_notify_user=Yes
# Required - Comma separated list of other email addresses to notify on successful device wipe
maas360_wipe_device_notify_others=email1, email2
maas360_cancel_pending_wipe_url= /device-apis/devices/1.0/cancelPendingWipe/

# Stop App Distribution Fn settings
maas360_stop_app_distribution_url=/application-apis/applications/1.0/stopAppDistribution/

# Search Installed Apps Fn settings
maas360_search_installed_apps_url=/application-apis/installedApps/1.0/search/
# Limit number of devices returned at one time. Allowed page sizes: 25, 50, 100, 200, 250. Default value: 50
maas360_search_installed_apps_page_size=50
    """
    return config_data
