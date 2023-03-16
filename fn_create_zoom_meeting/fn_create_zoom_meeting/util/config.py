# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for create_zoom_meeting"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""[fn_create_zoom_meeting]
zoom_api_url=https://api.zoom.us/v2
zoom_api_key=<zoom api key>
zoom_marketplace_account_email=<zoom marketplace account email>
zoom_api_secret=<zoom api secret>
zoom_api_timezone=<timezone, i.e America/New_York>
zoom_account_id=<account id>
zoom_client_id=<server_to_server_client_id>
zoom_client_secret=<server_to_server_client_secret>
"""