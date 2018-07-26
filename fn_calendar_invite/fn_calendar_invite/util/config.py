# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_calendar_invite"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_calendar_invite]
email_username=jimmy@example.com
email_password=l33t
email_nickname=ResilientSpammer
email_host=mail.example.com
email_port=25
"""
    return config_data