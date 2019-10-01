# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_scheduler"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_scheduler]
# timezone. ex: utc, America/New_York
timezone=utc
# number of rules which can run in parallel
thread_max=20
# directory for the sqlite persistent db
datastore_dir=
"""
    return config_data