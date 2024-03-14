# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.1.0.695

"""Generate the SOAR customizations required for fn_service_now"""

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
    Parameters required reload codegen for the fn_service_now package
    """
    return {
        "package": u"fn_service_now",
        "message_destinations": [
            u"fn_service_now"
        ],
        "functions": [
            u"fn_snow_add_attachment_to_record",
            u"fn_snow_add_note_to_record",
            u"fn_snow_close_record",
            u"fn_snow_create_record",
            u"fn_snow_helper_add_task_note",
            u"fn_snow_helper_update_datatable",
            u"fn_snow_lookup_sysid",
            u"fn_snow_update_record"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"sn_snow_record_id",
            u"sn_snow_record_link"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"sn_records_dt"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"snow_add_attachment_to_record",
            u"snow_create_record_incident_pb",
            u"snow_create_record_task_pb",
            u"snow_inc_update_record_on_severity_change_pb",
            u"snow_send_as_additional_comment_pb",
            u"snow_send_as_work_note_pb",
            u"snow_sir_update_record_on_severity_change_pb",
            u"snow_update_data_table_on_status_change_incident_pb",
            u"snow_update_data_table_on_status_change_task_pb",
            u"snow_updateclose_record_incident_pb",
            u"snow_updateclose_record_pb",
            u"snow_updateclose_record_task_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 49.0.8803

    Contents:
    - Message Destinations:
        - fn_service_now
    - Functions:
        - fn_snow_add_attachment_to_record
        - fn_snow_add_note_to_record
        - fn_snow_close_record
        - fn_snow_create_record
        - fn_snow_helper_add_task_note
        - fn_snow_helper_update_datatable
        - fn_snow_lookup_sysid
        - fn_snow_update_record
    - Playbooks:
        - snow_add_attachment_to_record
        - snow_create_record_incident_pb
        - snow_create_record_task_pb
        - snow_inc_update_record_on_severity_change_pb
        - snow_send_as_additional_comment_pb
        - snow_send_as_work_note_pb
        - snow_sir_update_record_on_severity_change_pb
        - snow_update_data_table_on_status_change_incident_pb
        - snow_update_data_table_on_status_change_task_pb
        - snow_updateclose_record_incident_pb
        - snow_updateclose_record_pb
        - snow_updateclose_record_task_pb
    - Incident Fields:
        - sn_snow_record_id
        - sn_snow_record_link
    - Data Tables:
        - sn_records_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)