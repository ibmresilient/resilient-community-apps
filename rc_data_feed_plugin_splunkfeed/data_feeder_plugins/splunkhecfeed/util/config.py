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
# Optional settings for accessing Splunk via a proxy.
#http_proxy=http://proxy:8088
#https_proxy=http://proxy:8088
# these settings are only needed for the unit tests
#user=
#password=
# new in v1.2.0 exclude incident fields. Specify fields to exclude one per line. Wildcards such as * and ? may be used. 
#exclude_incident_fields_file = /path/to/exclusion_file.txt
"""

    return config_data

def apphost_config_section_data():
    return u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=splunk_hec_feed
reload=False
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
