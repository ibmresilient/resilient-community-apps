# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_teams"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_teams]
# <channel_name> = <teams channel webhook>
# selftest = <teams channel webhook>
#
# directory_id and application_id can be found at
#    portal.azure.com > App registrations > Integration Name > Overview
#
# secret_value can be found at
#   portal.azure.com > App registrations > Integration Name > Certificates & secrets
directory_id = <Directory (tenant) ID>
application_id = <Application (client) ID>
secret_value = <Secret Value>
"""
    return config_data