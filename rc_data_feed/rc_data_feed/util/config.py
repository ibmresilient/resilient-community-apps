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
reload=true
# use reload_types to limit the types of objects when reload=true.
# Ex: incident,task,note,artifact,attachment,<data_table_api_name>
reload_types=
# set to true if ElasticSearch errors occur during reload=true
reload_query_api_method=false

# feed_data is the default message destination that will be listened to
queue=feed_data

# set to true if attachment data should be part of payload send to plugins
include_attachment_data=false
# if necessary, specify the supported workspace (by label, case sensitive) and the list of feeds associated with it
# ex: 'Default Workspace': ['sqlserver_feed'], 'workspace A': ['kafka_feed', 'resilient_feed']
workspaces=
# support for parallel execution. Default is False
parallel_execution = False
# When to collect time-series data. Because of the extra API call needed to collect this data, it could be more impactful on SOAR when set to 'always'
#  default is 'never'
#timeseries = always | onclose | never
# A comma separated list of time-series fields to collect. Custom select and boolean fields are also possible.
#   Specify wildcard fields with '?' or '*'. ex. ts_* will collect all time-series fields starting with "ts_"
#   default is all timeseries fields
#timeseries_fields = owner_id, phase_id, severity_code, <custom_field>
"""
    return config_data
