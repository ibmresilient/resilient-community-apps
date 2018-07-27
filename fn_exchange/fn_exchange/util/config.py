# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_exchange"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_exchange]
cert_verify=[True|False]
server=example.com
username=domain\\username
password=password
default_folder_path=Some folder path after root i.e. Top of Information Store/Inbox
default_timeozne=Some Microsoft timezone i.e. America/New_York
#"""
    return config_data