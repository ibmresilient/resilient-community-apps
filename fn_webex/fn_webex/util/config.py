# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_webex"""


def config_section_data():

    config_data = u"""[fn_webex]
# Creditals and other options required for fn_webex

webex_site_url = https://webexapis.com
webex_timezone = UTC +00:00
client_id = <Issued when creating the integration>
client_secret = <Issued when creating the integration>
refresh_token = <Generated using the OAuth Utilities Tool>
scope = <A space-separated list of scopes being requested by your integration (see below)>
"""
    return config_data
