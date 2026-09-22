# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""Generate the SOAR customizations required for fn_axonius"""

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
    Parameters required reload codegen for the fn_axonius package
    """
    return {
        "package": u"fn_axonius",
        "message_destinations": [
            u"fn_axonius"
        ],
        "functions": [
            u"axonius_get_device_by_id",
            u"axonius_get_device_by_query",
            u"axonius_get_device_count",
            u"axonius_run_enforcement_set"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"axonius_devices_dt"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Axonius: Populate Devices Data Table",
            u"Convert JSON to rich text v1.3"
        ],
        "playbooks": [
            u"axonius_add_artifacts_to_soar",
            u"axonius_add_to_devices_data_table",
            u"axonius_get_device_count",
            u"axonius_query_devices",
            u"axonius_refetch_device_in_row",
            u"axonius_run_enforcement_set",
            u"axonius_write_device_json_to_an_attachment"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 50.0.9097

    Contents:
    - Message Destinations:
        - fn_axonius
    - Functions:
        - axonius_get_device_by_id
        - axonius_get_device_by_query
        - axonius_get_device_count
        - axonius_run_enforcement_set
    - Playbooks:
        - axonius_add_artifacts_to_soar
        - axonius_add_to_devices_data_table
        - axonius_get_device_count
        - axonius_query_devices
        - axonius_refetch_device_in_row
        - axonius_run_enforcement_set
        - axonius_write_device_json_to_an_attachment
    - Data Tables:
        - axonius_devices_dt
    - Scripts:
        - Axonius: Populate Devices Data Table
        - Convert JSON to rich text v1.3
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)