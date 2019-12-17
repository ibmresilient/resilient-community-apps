# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[elastic_feed]
class=ElasticFeed
url=https://your_org.com
port=9200
# if using multiple organizations, consider indexes such as resilient_<org_ID>
# each document type will append to this index as elastic 6.0 onlyl supports one document type per index
index_prefix=resilient_
auth_user=
auth_password=
cafile=false
"""
    return config_data
