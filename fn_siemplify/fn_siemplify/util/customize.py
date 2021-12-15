# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_siemplify"""

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
    Parameters required reload codegen for the fn_siemplify package
    """
    return {
        "package": u"fn_siemplify",
        "message_destinations": [u"fn_siemplify"],
        "functions": [u"siemplify_sync_artifact", u"siemplify_sync_attachment", u"siemplify_sync_case", u"siemplify_sync_comment", u"siemplify_sync_task"],
        "workflows": [u"siemplify_add_comment", u"siemplify_m_sync_case", u"siemplify_sync_artifact", u"siemplify_sync_case", u"siemplify_sync_task"],
        "actions": [u"Siemplify Auto Sync Case", u"Siemplify Sync Artifact", u"Siemplify Sync Case", u"Siemplify Sync Comment", u"Siemplify Sync Task"],
        "incident_fields": [u"siemplify_alert_id", u"siemplify_case_id", u"siemplify_case_link"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.6328

    Contents:
    - Message Destinations:
        - fn_siemplify
    - Functions:
        - siemplify_sync_artifact
        - siemplify_sync_attachment
        - siemplify_sync_case
        - siemplify_sync_comment
        - siemplify_sync_task
    - Workflows:
        - siemplify_add_comment
        - siemplify_m_sync_case
        - siemplify_sync_artifact
        - siemplify_sync_case
        - siemplify_sync_task
    - Rules:
        - Siemplify Auto Sync Case
        - Siemplify Sync Artifact
        - Siemplify Sync Case
        - Siemplify Sync Comment
        - Siemplify Sync Task
    - Incident Fields:
        - siemplify_alert_id
        - siemplify_case_id
        - siemplify_case_link
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)