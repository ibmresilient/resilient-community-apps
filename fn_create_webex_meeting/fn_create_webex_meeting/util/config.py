# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_create_webex_meeting"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[create_webex_meeting]
# this may also be the conference id for the developer sandbox
webex_email=
webex_password=
webex_site=
webex_site_url=
webex_timezone=
# use these as an alternative to webex_site (i.e. developer sandbox)
#webex_site_id=
#webex_partner_id=
"""
    return config_data
