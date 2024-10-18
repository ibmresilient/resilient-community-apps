# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_teams"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""[fn_teams]
#
# Use in function 'MS Teams: Post Message' with the input field: team_channel
# <team_channel> = <channel webhook url>
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
# selftest = <selftest channel webhook url>
# selftest_workflows = <selftest channel webhook url and Teams Workflows>
"""

# not v3.0
# [fn_teams_approval_process]
# # if using the Approval Request process, enable the poller to check for approval request updates
# # in seconds
# #poller_interval=60
# # Comma separated list of case-insensitive approval words
# approval_words=accept, accepted, approve, approved, ok
# # Comma separated list of case-insensitive rejection words
# rejection_words=reject, rejected, deny, denied, no
