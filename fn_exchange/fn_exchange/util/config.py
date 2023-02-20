# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_exchange"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_exchange]
verify_cert=True
server=example.com

# To use this package, this must be an admin account with mailbox access to other accounts
username=domain\\username

# This is the default account to send emails and create meetings if one was not specified. Specifying an account that is not this one will require impersonation access.
email=admin@example.com 
password=password

# folder path after root i.e. Top of Information Store/Inbox. Multiple folder paths must be separated by commas.
default_folder_path=Top of Information Store/Inbox

# Set a different Timezone if required. Default Timezone is set to Etc/GMT
#timezone=Etc/GMT

#https_proxy=https://your.proxy.com
#http_proxy=http://your.proxy.com
"""
    return config_data