# -*- coding: utf-8 -*-

"""Generate the SOAR customizations required for fn_datatable_utils"""

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
        "functions": [u"dt_utils_create_csv_table", u"dt_utils_delete_row", u"dt_utils_delete_rows", u"dt_utils_get_row", u"dt_utils_get_rows", u"dt_utils_update_row"],
        "workflows": [u"example_create_csv_datatable", u"example_data_table_utils_delete_row", u"example_data_table_utils_delete_row_from_datatable", u"example_data_table_utils_delete_rows", u"example_data_table_utils_delete_rows_from_datatable", u"example_data_table_utils_get_current_row", u"example_data_table_utils_get_row", u"example_data_table_utils_get_rows", u"example_data_table_utils_update_row", u"update_row"],
        "actions": [u"Delete Current Row", u"Delete Data Table Row", u"Delete Data Table Rows", u"Delete Rows by Name", u"Example: Create CSV Datatable", u"Get Current Row", u"Get Data Table Row", u"Get Data Table Rows", u"Update Current Row", u"Update Data Table Row"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"dt_utils_test_data_table"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 41.0.6783

    Contents:
    - Message Destinations:
        - fn_datatable_utils
    - Functions:
        - dt_utils_create_csv_table
        - dt_utils_delete_row
        - dt_utils_delete_rows
        - dt_utils_get_row
        - dt_utils_get_rows
        - dt_utils_update_row
    - Workflows:
        - example_create_csv_datatable
        - example_data_table_utils_delete_row
        - example_data_table_utils_delete_row_from_datatable
        - example_data_table_utils_delete_rows
        - example_data_table_utils_delete_rows_from_datatable
        - example_data_table_utils_get_current_row
        - example_data_table_utils_get_row
        - example_data_table_utils_get_rows
        - example_data_table_utils_update_row
        - update_row
    - Rules:
        - Delete Current Row
        - Delete Data Table Row
        - Delete Data Table Rows
        - Delete Rows by Name
        - Example: Create CSV Datatable
        - Get Current Row
        - Get Data Table Row
        - Get Data Table Rows
        - Update Current Row
        - Update Data Table Row
    - Data Tables:
        - dt_utils_test_data_table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)