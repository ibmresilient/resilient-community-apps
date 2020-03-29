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
# comma separated list of fields to allow incidents to sync. ex. incident_type_ids in ['Phishing']
matching_incident_fields=
# when using matching_incident_fields, specify whether 'all' or 'any' field needs to match to accept
matching_operator=all
# comma separated list of fields to exclude from an incident. Sections of fields can be used: pii,gdpr,hipaa,cm
exclude_incident_fields=
# include references within the incident to source org_id and incident_id. Values True/False
sync_reference_fields=True
"""
    return config_data
