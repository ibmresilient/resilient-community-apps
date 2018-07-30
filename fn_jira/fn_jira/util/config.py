# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_jira"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[jira]
url=https://<jira url>
user=<jira user>
password=<jira user password>
# use verifyFlag to disable untrusted certificate verification
verifyFlag=True
"""
    return config_data