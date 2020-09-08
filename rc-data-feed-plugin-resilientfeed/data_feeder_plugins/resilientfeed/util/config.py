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
port=443
org=
cafile=false
# identify a sqlite db file to retain mapping between resilient instances.
db_sync_file=/path/to/file
# semicolon separated list of fields to allow incidents to sync. ex. incident_type_ids in ['Phishing'];custom_field == "a"
matching_incident_fields=
# when using matching_incident_fields, specify whether 'all' or 'any' field needs to match to accept. Default: all
matching_operator=all
# semicolon separated list of fields to exclude from an incident. Sections of fields can be used: pii;gdpr;hipaa;cm
exclude_incident_fields=
# include references within the incident to source org_id and incident_id. Values true/false
sync_reference_fields=true
# true|false - specify whether to delete the target incident if the source incident is deleted. Default: false
delete_incidents=false
"""
    return config_data

def apphost_config_section_data():
    return u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=resilient_feed
reload=False
# set to true if ElasticSearch errors occur during reload=True
reload_query_api_method=False
# feed_data is the default message destination that will be listened to
queue=feed_data
"""