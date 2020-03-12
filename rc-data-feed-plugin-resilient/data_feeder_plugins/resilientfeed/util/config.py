# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[resilient_feed]
class=ResilientFeed
# provide configuration information to the target Resilient and Organization
host=localhost
#proxy_host=
api_key_id=
api_key_secret=
#email=
#password=
port=1443
org=resilient
cafile=false
# identify a sqlite db file to retain mapping between resilient instances.
db_sync_file=/path/to/file
"""
    return config_data
