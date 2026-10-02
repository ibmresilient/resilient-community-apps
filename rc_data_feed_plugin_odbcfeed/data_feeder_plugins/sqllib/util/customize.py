# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate the Resilient customizations required for rc_data_feed"""

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
    Parameters required reload codegen for the rc_data_feed package
    """
    return {
        "package": u"rc_data_feed",
        "message_destinations": [u"feed_data"],
        "functions": [u"data_feeder_sync_incidents"],
        "workflows": [],
        "actions": [u"Data Feeder: Artifact", u"Data Feeder: Attachment", u"Data Feeder: Incident", u"Data Feeder: Milestone", u"Data Feeder: Note", u"Data Feeder: Task"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"data_feeder_sync_incidents_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - feed_data
    - Functions:
        - data_feeder_sync_incidents
    - Playbooks:
        - data_feeder_sync_incidents_pb
    - Rules:
        - Data Feeder: Artifact
        - Data Feeder: Attachment
        - Data Feeder: Incident
        - Data Feeder: Milestone
        - Data Feeder: Note
        - Data Feeder: Task
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)