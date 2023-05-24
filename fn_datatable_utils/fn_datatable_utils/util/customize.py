# -*- coding: utf-8 -*-
# Generated with resilient-sdk v46.0.8131

"""Generate the Resilient customizations required for fn_datatable_utils"""

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
    Parameters required reload codegen for the fn_datatable_utils package
    """
    return {
        "package": u"fn_datatable_utils",
        "message_destinations": [u"fn_datatable_utils"],
        "functions": [u"dt_utils_add_row", u"dt_utils_clear_datatable", u"dt_utils_create_csv_table", u"dt_utils_delete_row", u"dt_utils_delete_rows", u"dt_utils_get_all_data_table_rows", u"dt_utils_get_row", u"dt_utils_get_rows", u"dt_utils_update_row"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"dt_utils_test_data_table"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"add_row_pb", u"add_row_to_datatable_pb", u"clear_datatable_pb", u"delete_current_row_pb", u"delete_data_table_row_pb", u"delete_data_table_rows_pb", u"delete_rows_by_name_pb", u"example_create_csv_datatable_pb", u"get_all_rows_pb", u"get_current_row_pb", u"get_data_table_row_pb", u"get_data_table_rows_pb", u"update_current_row_pb", u"update_data_table_row_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_datatable_utils
    - Functions:
        - dt_utils_add_row
        - dt_utils_clear_datatable
        - dt_utils_create_csv_table
        - dt_utils_delete_row
        - dt_utils_delete_rows
        - dt_utils_get_all_data_table_rows
        - dt_utils_get_row
        - dt_utils_get_rows
        - dt_utils_update_row
    - Playbooks:
        - add_row_pb
        - add_row_to_datatable_pb
        - clear_datatable_pb
        - delete_current_row_pb
        - delete_data_table_row_pb
        - delete_data_table_rows_pb
        - delete_rows_by_name_pb
        - example_create_csv_datatable_pb
        - get_all_rows_pb
        - get_current_row_pb
        - get_data_table_row_pb
        - get_data_table_rows_pb
        - update_current_row_pb
        - update_data_table_row_pb
    - Data Tables:
        - dt_utils_test_data_table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)