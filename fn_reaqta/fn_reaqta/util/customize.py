# -*- coding: utf-8 -*-

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
        "functions": [u"reaqta_attach_file", u"reaqta_close_alert", u"reaqta_create_artifact", u"reaqta_create_note", u"reaqta_create_policy", u"reaqta_get_alert_information", u"reaqta_get_processes", u"reaqta_isolate_machine", u"reaqta_kill_process"],
        "workflows": [u"reaqta_attach_file_from_process_list", u"reaqta_attach_file_from_triggered_events", u"reaqta_close_alert", u"reaqta_create_artifact_from_process_path", u"reaqta_create_artifact_from_trigger_event", u"reaqta_create_note", u"reaqta_create_policy_from_artifact", u"reaqta_create_policy_on_triggered_event", u"reaqta_get_alert_information", u"reaqta_get_processes", u"reaqta_isolate_endpoint", u"reaqta_kill_process"],
        "actions": [u"ReaQta: Close Alert", u"ReaQta: Create Artifact from Process Path", u"ReaQta: Create Artifact from Trigger Event", u"ReaQta: Create Attachment from Process List", u"ReaQta: Create Attachment from Triggered Event", u"ReaQta: Create Note", u"ReaQta: Create Policy from Artifact", u"ReaQta: Create Policy on Triggered Event", u"ReaQta: Get Alert Information", u"ReaQta: Get Processes", u"ReaQta: Isolate Endpoint", u"ReaQta: Kill Process"],
        "incident_fields": [u"reaqta_alert_link", u"reaqta_endpoint_id", u"reaqta_groups", u"reaqta_id", u"reaqta_machine_info", u"reaqta_tags", u"reaqta_trigger_condition"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"reaqta_process_list", u"reaqta_trigger_events"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 41.2.41

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
        - reaqta_get_processes
        - reaqta_isolate_machine
        - reaqta_kill_process
    - Workflows:
        - reaqta_attach_file_from_process_list
        - reaqta_attach_file_from_triggered_events
        - reaqta_close_alert
        - reaqta_create_artifact_from_process_path
        - reaqta_create_artifact_from_trigger_event
        - reaqta_create_note
        - reaqta_create_policy_from_artifact
        - reaqta_create_policy_on_triggered_event
        - reaqta_get_alert_information
        - reaqta_get_processes
        - reaqta_isolate_endpoint
        - reaqta_kill_process
    - Rules:
        - ReaQta: Close Alert
        - ReaQta: Create Artifact from Process Path
        - ReaQta: Create Artifact from Trigger Event
        - ReaQta: Create Attachment from Process List
        - ReaQta: Create Attachment from Triggered Event
        - ReaQta: Create Note
        - ReaQta: Create Policy from Artifact
        - ReaQta: Create Policy on Triggered Event
        - ReaQta: Get Alert Information
        - ReaQta: Get Processes
        - ReaQta: Isolate Endpoint
        - ReaQta: Kill Process
    - Incident Fields:
        - reaqta_alert_link
        - reaqta_endpoint_id
        - reaqta_groups
        - reaqta_id
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