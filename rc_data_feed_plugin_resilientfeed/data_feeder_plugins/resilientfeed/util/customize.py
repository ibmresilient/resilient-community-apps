# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for rc_data_feed_plugin_resilientfeed"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the rc_data_feed_plugin_resilientfeed package
    """
    return {
        "package": u"rc_data_feed_plugin_resilientfeed",
        "message_destinations": [u"feed_data", "feed_data_resilient"],
        "functions": [],
        "workflows": [],
        "actions": [u"Data Feeder: Artifact", u"Data Feeder: Note", u"Data Feeder: Attachment", u"Data Feeder: Sync Incidents", u"Data Feeder: Task", u"Data Feeder: Milestone", u"Data Feeder: Incident"],
        "incident_fields": ["df_org_id", "df_inc_id", "df_create_date", "df_host"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": ["data_feeder_sync_incidents_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0

    Contents:
    - Message Destinations:
        - feed_data_unused
        - feed_data_resilient
    - Playbooks:
        - data_feeder_sync_incidents_pb
    - Rules:
        - Data Feeder: Artifact
        - Data Feeder: Note
        - Data Feeder: Attachment
        - Data Feeder: Sync Incidents
        - Data Feeder: Task
        - Data Feeder: Milestone
        - Data Feeder: Incident
    - Incident Fields:
        - df_org_id
        - df_host
        - df_create_date
        - df_inc_id
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)
