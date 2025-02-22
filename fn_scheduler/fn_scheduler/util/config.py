# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_scheduler"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_scheduler]
# timezone. ex: UTC, America/New_York
timezone=UTC
# number of rules which can run in parallel
thread_max=20
# directory for the sqlite persistent db
datastore_dir=
# db url if using a postgreSQL DB. Use this with AppHost
# db_url=postgresql://username:password@host:port/database (or) db_url=postgresql+pypostgresql://username:password@host:port/database
# set to True to disable note creation when a scheduled rule is triggered. Default is False.
disable_notes=False
"""
    return config_data