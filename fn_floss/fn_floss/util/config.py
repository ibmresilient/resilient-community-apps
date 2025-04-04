# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
"""Generate a default configuration-file section for fn_floss"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_floss]
# Floss Function
# Use the following floss_options variable to specify the commandline options to be used by 
# the floss package to define the behavior for extracting strings. 
# Each commandline parameter should be separated by a comma.
# The defaults here are: -q quiet mode, -s shellcode, -n minimum string length
# See https://github.com/fireeye/flare-floss/blob/master/doc/usage.md for all possible commandline options.
floss_options=-q,-s,-n 5
"""
    return config_data
