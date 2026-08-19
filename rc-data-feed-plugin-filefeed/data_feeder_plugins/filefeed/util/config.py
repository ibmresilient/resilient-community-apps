# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_data_feed"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[file_feed]
class=FileFeed
directory=/path/to/feed_directory
"""

    return config_data

def apphost_config_section_data():
    return u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=file_feed
reload=False
# set to true if ElasticSearch errors occur during reload=True
reload_query_api_method=False
# feed_data is the default message destination that will be listened to
queue=feed_data
"""