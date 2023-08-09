# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate the Resilient customizations required for fn_reaqta"""

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
    Parameters required reload codegen for the fn_reaqta package
    """
    return {
        "package": u"fn_reaqta",
        "message_destinations": [u"fn_reaqta"],
        "functions": [u"reaqta_attach_file", u"reaqta_close_alert", u"reaqta_create_artifact", u"reaqta_create_note", u"reaqta_create_policy", u"reaqta_get_alert_information", u"reaqta_get_endpoint_status", u"reaqta_get_processes", u"reaqta_isolate_machine", u"reaqta_kill_process"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"reaqta_alert_link", u"reaqta_endpoint_id", u"reaqta_endpoint_link", u"reaqta_groups", u"reaqta_hive", u"reaqta_id", u"reaqta_impact", u"reaqta_machine_info", u"reaqta_tags", u"reaqta_trigger_condition"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"reaqta_process_list", u"reaqta_trigger_events"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"reaqta_close_alert", u"reaqta_create_artifact_from_process_path", u"reaqta_create_artifact_from_trigger_event", u"reaqta_create_attachment_from_process_list", u"reaqta_create_attachment_from_triggered_event", u"reaqta_create_note", u"reaqta_create_policy_from_artifact", u"reaqta_create_policy_on_triggered_event", u"reaqta_get_alert_information", u"reaqta_get_endpoint_status", u"reaqta_get_processes", u"reaqta_isolate_endpoint", u"reaqta_kill_process", u"reaqta_refresh_alert_information"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 47.0.8304

    Contents:
    - Message Destinations:
        - fn_reaqta
    - Functions:
        - reaqta_attach_file
        - reaqta_close_alert
        - reaqta_create_artifact
        - reaqta_create_note
        - reaqta_create_policy
        - reaqta_get_alert_information
        - reaqta_get_endpoint_status
        - reaqta_get_processes
        - reaqta_isolate_machine
        - reaqta_kill_process
    - Playbooks:
        - reaqta_close_alert
        - reaqta_create_artifact_from_process_path
        - reaqta_create_artifact_from_trigger_event
        - reaqta_create_attachment_from_process_list
        - reaqta_create_attachment_from_triggered_event
        - reaqta_create_note
        - reaqta_create_policy_from_artifact
        - reaqta_create_policy_on_triggered_event
        - reaqta_get_alert_information
        - reaqta_get_endpoint_status
        - reaqta_get_processes
        - reaqta_isolate_endpoint
        - reaqta_kill_process
        - reaqta_refresh_alert_information
    - Incident Fields:
        - reaqta_alert_link
        - reaqta_endpoint_id
        - reaqta_endpoint_link
        - reaqta_groups
        - reaqta_hive
        - reaqta_id
        - reaqta_impact
        - reaqta_machine_info
        - reaqta_tags
        - reaqta_trigger_condition
    - Data Tables:
        - reaqta_process_list
        - reaqta_trigger_events
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)