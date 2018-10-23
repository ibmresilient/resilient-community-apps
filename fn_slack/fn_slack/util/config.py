# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_slack"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_slack]
# Slack app OAuth Access Token
api_token=xoxp-xxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxx-xxxxxxxxxxx

# Username represents the default submission author.
# Used together with 'as_user=False'.
# You can also update the username on the Workflow.
username=Resilient"""

    return config_data
