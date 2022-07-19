# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_webex"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_webex when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_webex]
# this may also be the conference id for the developer sandbox
webex_site_url = <URL>
webex_bearerid = <BearerID>
webex_timezone = GMT 00:00"""

    return config_data
