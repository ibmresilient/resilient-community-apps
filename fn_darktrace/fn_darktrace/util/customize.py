# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_darktrace"""

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
    Parameters required reload codegen for the fn_darktrace package
    """
    return {
        "package": u"fn_darktrace",
        "message_destinations": [u"fn_darktrace"],
        "functions": [u"darktrace_acknowledge_incident_event", u"darktrace_acknowledge_model_breach", u"darktrace_add_device_tags", u"darktrace_list_similar_devices", u"darktrace_unacknowledge_incident_event"],
        "workflows": [u"darktrace_acknowledge_incident_event", u"darktrace_acknowledge_model_breach", u"darktrace_add_tags_to_device", u"darktrace_list_similar_devices", u"darktrace_unacknowledge_incident_event"],
        "actions": [u"Darktrace: Acknowledge Incident Event", u"Darktrace: Acknowledge Model Breach", u"Darktrace: Add Tags to Device", u"Darktrace: Get External Endpoint Details", u"Darktrace: List Similar Devices", u"Darktrace: Send Comment", u"Darktrace: Unacknowledge Incident Event"],
        "incident_fields": [u"darktrace_aianalyst_incident_group_id", u"darktrace_associated_device_ids", u"darktrace_breach_link", u"darktrace_group_category", u"darktrace_group_score", u"darktrace_incident_group_acknowledged", u"darktrace_incident_group_link", u"darktrace_incident_group_start_time", u"darktrace_incident_last_modified", u"darktrace_initiating_device_ids", u"darktrace_number_of_events_in_group", u"darktrace_pbid"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"darktrace_associated_devices_dt", u"darktrace_incident_events_dt", u"darktrace_model_breaches_dt"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 44.0.7585

    Contents:
    - Message Destinations:
        - fn_darktrace
    - Functions:
        - darktrace_acknowledge_incident_event
        - darktrace_acknowledge_model_breach
        - darktrace_add_device_tags
        - darktrace_list_similar_devices
        - darktrace_unacknowledge_incident_event
    - Workflows:
        - darktrace_acknowledge_incident_event
        - darktrace_acknowledge_model_breach
        - darktrace_add_tags_to_device
        - darktrace_list_similar_devices
        - darktrace_unacknowledge_incident_event
    - Rules:
        - Darktrace: Acknowledge Incident Event
        - Darktrace: Acknowledge Model Breach
        - Darktrace: Add Tags to Device
        - Darktrace: Get External Endpoint Details
        - Darktrace: List Similar Devices
        - Darktrace: Send Comment
        - Darktrace: Unacknowledge Incident Event
    - Incident Fields:
        - darktrace_aianalyst_incident_group_id
        - darktrace_associated_device_ids
        - darktrace_breach_link
        - darktrace_group_category
        - darktrace_group_score
        - darktrace_incident_group_acknowledged
        - darktrace_incident_group_link
        - darktrace_incident_group_start_time
        - darktrace_incident_last_modified
        - darktrace_initiating_device_ids
        - darktrace_number_of_events_in_group
        - darktrace_pbid
    - Data Tables:
        - darktrace_associated_devices_dt
        - darktrace_incident_events_dt
        - darktrace_model_breaches_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)