# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=<your feeds>
reload=True
# set to true if ElasticSearch errors occur during reload=True
reload_query_api_method=False

# feed_data is the default message destination that will be listened to
queue=feed_data
"""
    return config_data
