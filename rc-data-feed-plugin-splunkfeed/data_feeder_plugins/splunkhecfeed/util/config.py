# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[splunk_hec_feed]
class=SplunkHECFeed
token=<token>
host=<host>
port=8088
index=data_feeder
# only use event_source_type if using one type. otherwise, the resilient object type (incident, note, artifact, etc.) is used
#event_source_type=txt
event_host=<resilient host>
event_source=resilient
use_ssl=true
"""

    return config_data
