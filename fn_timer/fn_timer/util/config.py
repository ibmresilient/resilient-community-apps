# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_timer"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_timer when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_timer]
# Max Timer sleep time. The input string is of format “time value” concatenated with a
# “time unit” character, where character is: 's' for seconds, 'm' for minutes, 'h' for hours
# 'd' for days.  For example: '30s' = 30 seconds; '40m' = 40 minutes;
max_timer=30d

# Add num_workers= to the resilient section to set the number of threads
"""
    return config_data
