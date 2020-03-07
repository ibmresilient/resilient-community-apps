# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[resilient_feed]
class=ResilientFeed
host=localhost
#proxy_host=
api_key_id=
api_key_secret=
#email=
#password=
port=1443
org=resilient
cafile=false
# optionally use sqlite db to retain mapping between resilient instances
# if not used, a datatable in the resulting incident is maintained
#db_sync_file=/path/to/file
"""
    return config_data
