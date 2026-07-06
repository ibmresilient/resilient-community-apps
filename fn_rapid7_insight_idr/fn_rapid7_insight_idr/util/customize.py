# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.2.575

"""Generate the SOAR customizations required for fn_rapid7_insight_idr"""

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
    Parameters required reload codegen for the fn_rapid7_insight_idr package
    """
    return {
        "package": u"fn_rapid7_insight_idr",
        "message_destinations": [
            u"fn_rapid7_insight_idr"
        ],
        "functions": [
            u"rapid7_insight_idr_add_attachments_to_soar_case",
            u"rapid7_insight_idr_get_alert_evidence",
            u"rapid7_insight_idr_get_alerts",
            u"rapid7_insight_idr_get_comments",
            u"rapid7_insight_idr_get_investigation",
            u"rapid7_insight_idr_list_attachments",
            u"rapid7_insight_idr_post_comment",
            u"rapid7_insight_idr_set_priority",
            u"rapid7_insight_idr_set_status"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"rapid7_insight_idr_assignee",
            u"rapid7_insight_idr_assignee_email",
            u"rapid7_insight_idr_disposition",
            u"rapid7_insight_idr_link",
            u"rapid7_insight_idr_responsibility",
            u"rapid7_insight_idr_rrn",
            u"rapid7_insight_idr_source",
            u"rapid7_insight_idr_status"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"rapid7_insight_idr_alerts_dt"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"rapid7_insight_idr_close_investigation_on_case_close",
            u"rapid7_insight_idr_closed_by_rapid7_insightidr",
            u"rapid7_insight_idr_get_alert_evidence_dt",
            u"rapid7_insight_idr_get_alerts",
            u"rapid7_insight_idr_get_attachments_from_investigation",
            u"rapid7_insight_idr_send_note_to_rapid7_investigation",
            u"rapid7_insight_idr_set_priority_automatically",
            u"rapid7_insight_idr_set_status_and_disposition",
            u"rapid7_insight_idr_update_case",
            u"rapid7_insight_idr_update_created_case"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 49.0.8803

    Contents:
    - Message Destinations:
        - fn_rapid7_insight_idr
    - Functions:
        - rapid7_insight_idr_add_attachments_to_soar_case
        - rapid7_insight_idr_get_alert_evidence
        - rapid7_insight_idr_get_alerts
        - rapid7_insight_idr_get_comments
        - rapid7_insight_idr_get_investigation
        - rapid7_insight_idr_list_attachments
        - rapid7_insight_idr_post_comment
        - rapid7_insight_idr_set_priority
        - rapid7_insight_idr_set_status
    - Playbooks:
        - rapid7_insight_idr_close_investigation_on_case_close
        - rapid7_insight_idr_closed_by_rapid7_insightidr
        - rapid7_insight_idr_get_alert_evidence_dt
        - rapid7_insight_idr_get_alerts
        - rapid7_insight_idr_get_attachments_from_investigation
        - rapid7_insight_idr_send_note_to_rapid7_investigation
        - rapid7_insight_idr_set_priority_automatically
        - rapid7_insight_idr_set_status_and_disposition
        - rapid7_insight_idr_update_case
        - rapid7_insight_idr_update_created_case
    - Incident Fields:
        - rapid7_insight_idr_assignee
        - rapid7_insight_idr_assignee_email
        - rapid7_insight_idr_disposition
        - rapid7_insight_idr_link
        - rapid7_insight_idr_responsibility
        - rapid7_insight_idr_rrn
        - rapid7_insight_idr_source
        - rapid7_insight_idr_status
    - Data Tables:
        - rapid7_insight_idr_alerts_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)