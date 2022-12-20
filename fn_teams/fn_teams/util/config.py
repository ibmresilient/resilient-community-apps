# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_teams"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_teams]
#
# <channel_name> = <channel webhook url> 
# (<channel_name> and the <teams_channel> input for the MS Teams: Post Message function must be the same.
#
# selftest = <selftest channel webhook url>
#
# directory_id and application_id can be found at
#    portal.azure.com > App registrations > Integration Name > Overview
#
# secret_value can be found at
#   portal.azure.com > App registrations > Integration Name > Certificates & secrets
#
# refresh_token can be generated using the OAuth utils tool.
#   Only required for MS Teams: Read Message function.

directory_id = <Directory (tenant) ID>
application_id = <Application (client) ID>
secret_value = <Secret Value>
# refresh_token = <Refresh token> 

"""
    return config_data