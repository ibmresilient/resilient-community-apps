# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_darktrace"""

import base64
import io
import os

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
        "functions": [u"darktrace_acknowledge_incident_event", u"darktrace_acknowledge_model_breach", u"darktrace_add_device_tags", u"darktrace_clear_data_table", u"darktrace_get_devices", u"darktrace_get_incident_events", u"darktrace_get_incident_group", u"darktrace_list_similar_devices", u"darktrace_unacknowledge_incident_event", u"darktrace_unacknowledge_model_breach"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"darktrace_aianalyst_incident_group_id", u"darktrace_associated_device_ids", u"darktrace_breach_link", u"darktrace_group_category", u"darktrace_group_score", u"darktrace_incident_group_acknowledged", u"darktrace_incident_group_link", u"darktrace_incident_group_start_time", u"darktrace_incident_last_modified", u"darktrace_initiating_device_ids", u"darktrace_number_of_events_in_group"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"darktrace_associated_devices_dt", u"darktrace_incident_events_dt", u"darktrace_model_breaches_dt"],
        "automatic_tasks": [],
        "scripts": [u"Parse Darktrace Details to Incident Properties", u"Parse Darktrace Device Details to Artifacts", u"Parse Darktrace Device Details to Data Table", u"Parse Darktrace Incident Events Details to Data Table", u"Parse Darktrace Model Breaches Details to Data Table"],
        "playbooks": [u"darktrace_acknowledge_incident_event", u"darktrace_acknowledge_model_breach", u"darktrace_add_tags_to_device", u"darktrace_automatic_populate_incident_events_table", u"darktrace_list_similar_devices", u"darktrace_populate_devices_table", u"darktrace_unacknowledge_incident_event", u"darktrace_unacknowledge_model_breach", u"darktrace_update_all_data_tables", u"darktrace_update_devices_data_table", u"darktrace_update_incident_events_data_table", u"darktrace_update_model_breaches_data_table", u"dartkrace_automatic_populate_ai_analyst_group_details"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_darktrace
    - Functions:
        - darktrace_acknowledge_incident_event
        - darktrace_acknowledge_model_breach
        - darktrace_add_device_tags
        - darktrace_clear_data_table
        - darktrace_get_devices
        - darktrace_get_incident_events
        - darktrace_get_incident_group
        - darktrace_list_similar_devices
        - darktrace_unacknowledge_incident_event
        - darktrace_unacknowledge_model_breach
    - Playbooks:
        - darktrace_acknowledge_incident_event
        - darktrace_acknowledge_model_breach
        - darktrace_add_tags_to_device
        - darktrace_automatic_populate_incident_events_table
        - darktrace_list_similar_devices
        - darktrace_populate_devices_table
        - darktrace_unacknowledge_incident_event
        - darktrace_unacknowledge_model_breach
        - darktrace_update_all_data_tables
        - darktrace_update_devices_data_table
        - darktrace_update_incident_events_data_table
        - darktrace_update_model_breaches_data_table
        - dartkrace_automatic_populate_ai_analyst_group_details
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
    - Data Tables:
        - darktrace_associated_devices_dt
        - darktrace_incident_events_dt
        - darktrace_model_breaches_dt
    - Scripts:
        - Parse Darktrace Details to Incident Properties
        - Parse Darktrace Device Details to Artifacts
        - Parse Darktrace Device Details to Data Table
        - Parse Darktrace Incident Events Details to Data Table
        - Parse Darktrace Model Breaches Details to Data Table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)
