# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_service_now"""

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
        "message_destinations": [u"fn_service_now"],
        "functions": [u"fn_snow_add_attachment_to_record", u"fn_snow_add_note_to_record", u"fn_snow_close_record", u"fn_snow_create_record", u"fn_snow_helper_add_task_note", u"fn_snow_helper_update_datatable", u"fn_snow_lookup_sysid", u"fn_snow_update_record"],
        "workflows": [u"example_sir_snow_update_record_on_severity_change", u"example_snow_add_attachment_to_record", u"example_snow_add_comment_to_record", u"example_snow_add_worknote_to_record", u"example_snow_close_record_from_data_table", u"example_snow_close_record_incident", u"example_snow_close_record_task", u"example_snow_create_record_incident", u"example_snow_create_record_task", u"example_snow_update_datatable_on_status_change_incident", u"example_snow_update_datatable_on_status_change_task", u"example_snow_update_record_on_severity_change"],
        "actions": [u"SNOW: [INC] Update Record on Severity Change", u"SNOW: [SIR] Update Record on Severity Change", u"SNOW: Add Attachment to Record", u"SNOW: Create Record [Incident]", u"SNOW: Create Record [Task]", u"SNOW: Send as Additional Comment", u"SNOW: Send as Work Note", u"SNOW: Update Data Table on Status Change [Incident]", u"SNOW: Update Data Table on Status Change [Task]", u"SNOW: Update/Close Record", u"SNOW: Update/Close Record [Incident]", u"SNOW: Update/Close Record [Task]"],
        "incident_fields": [u"sn_snow_record_id", u"sn_snow_record_link"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"sn_records_dt"],
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
    - Workflows:
        - example_sir_snow_update_record_on_severity_change
        - example_snow_add_attachment_to_record
        - example_snow_add_comment_to_record
        - example_snow_add_worknote_to_record
        - example_snow_close_record_from_data_table
        - example_snow_close_record_incident
        - example_snow_close_record_task
        - example_snow_create_record_incident
        - example_snow_create_record_task
        - example_snow_update_datatable_on_status_change_incident
        - example_snow_update_datatable_on_status_change_task
        - example_snow_update_record_on_severity_change
    - Rules:
        - SNOW: [INC] Update Record on Severity Change
        - SNOW: [SIR] Update Record on Severity Change
        - SNOW: Add Attachment to Record
        - SNOW: Create Record [Incident]
        - SNOW: Create Record [Task]
        - SNOW: Send as Additional Comment
        - SNOW: Send as Work Note
        - SNOW: Update Data Table on Status Change [Incident]
        - SNOW: Update Data Table on Status Change [Task]
        - SNOW: Update/Close Record
        - SNOW: Update/Close Record [Incident]
        - SNOW: Update/Close Record [Task]
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