# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_atd"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mcafee_atd]
atd_url=https://127.0.0.1:8888
atd_username=
atd_password=
# Amount of time in minutes before the function quits and throws an error
timeout=30

# Interval in seconds to wait to check if the file has finished being analyzed
polling_interval=60

# Analyzer profile ID. The profile ID number can be found in the UI Policy/Analyzer Profile page.
vm_profile_list=

# parameter with values either 'run_now' or 'add_to_q', defaults to 'add_to_q'
filePriority=add_to_q

trust_cert=[True|False]
"""
    return config_data
