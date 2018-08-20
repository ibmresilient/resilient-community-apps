# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_exchange"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_exchange]
verify_cert=[True|False]
server=example.com
username=domain\\username - to use this package, this must be an admin account with mailbox access to other accounts
email=admin@example.com
password=password
default_folder_path=Some folder path after root i.e. Top of Information Store/Inbox. Multiple folderpaths must be separated by commas
default_timezone=Some Microsoft timezone i.e. America/New_York or Etc/GMT
#"""
    return config_data