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
port=443
api_key_id=
api_key_secret=
#email=
#password=
org=
cafile=false
# all proxy settings can be specified, including proxy_user, and proxy_password
#proxy_host=
#proxy_port=
# identify a sqlite db file to retain mapping between resilient instances.
sqlite_sync_file=/path/to/file
# postgresql db connection if sqlite_sync_file is not used
postgresql_connect=Driver={PostgreSQL};Server=127.0.0.1;DATABASE=<db>;Port=5432;connectTimeout=0
postgresql_uid=<acct>
postgresql_pwd=<pwd>
# semicolon separated list of fields to allow incidents to sync. ex. incident_type_ids in ["Phishing","Malware"];custom_field == a
# use ~ for 'contains', such as description ~ malicious
#matching_incident_fields=
# when using matching_incident_fields, specify whether 'all' or 'any' field needs to match to accept. Default: all
#matching_operator=all
# semicolon separated list of fields to exclude from an incident. Sections of fields can be used: pii;gdpr;hipaa;cm
#exclude_incident_fields=
# include references within the incident to source host, org_id, incident_id and create_date. Values true/false
sync_reference_fields=true
# true|false - specify whether to delete the target incident if the source incident is deleted. Default: false
delete_incidents=false
"""
    return config_data

def apphost_config_section_data():
    return u"""[feeds]
# comma separated section names. ex. sqlserver_feed,file_feed
feed_names=resilient_feed
reload=false
# use reload_types to limit the types of objects when reload=true.
# Ex: incident,task,note,artifact,attachment,<data_table_api_name>
reload_types=
# set to true if synchronization errors occur during reload=true
reload_query_api_method=false

# feed_data is the default message destination that will be listened to
queue=feed_data_resilient

# set to true if attachment data should be part of payload send to plugins
include_attachment_data=false
# if necessary, specify the supported workspace (by label, case sensitive) and the list of feeds associated with it
# ex: 'Default Workspace': ['resilient_feed'], 'workspace A': ['kafka_feed', 'resilient_feed']
workspaces=
# support for parallel execution. Default is False
parallel_execution = False
"""