# -*- coding: utf-8 -*-

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
        "functions": [u"dt_utils_create_csv_table", u"dt_utils_get_rows", u"dt_utils_update_row", u"dt_utils_delete_row", u"dt_utils_get_row", u"dt_utils_delete_rows"],
        "workflows": [u"example_data_table_utils_update_row", u"example_data_table_utils_delete_row", u"example_data_table_utils_delete_rows_from_datatable", u"example_data_table_utils_get_rows", u"example_data_table_utils_delete_rows", u"example_data_table_utils_get_row", u"update_row", u"example_data_table_utils_delete_row_from_datatable", u"example_create_csv_datatable"],
        "actions": [u"Example: Create CSV Datatable", u"Delete Data Table Rows", u"Update Data Table Row", u"Get Data Table Rows", u"Delete Current Row", u"Delete Data Table Row", u"Update Current Row", u"Delete Rows by Name", u"Get Data Table Row"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"dt_utils_test_data_table"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 36.0.5634

    Contents:
    - Message Destinations:
        - fn_datatable_utils
    - Functions:
        - dt_utils_create_csv_table
        - dt_utils_get_rows
        - dt_utils_update_row
        - dt_utils_delete_row
        - dt_utils_get_row
        - dt_utils_delete_rows
    - Workflows:
        - example_data_table_utils_update_row
        - example_data_table_utils_delete_row
        - example_data_table_utils_delete_rows_from_datatable
        - example_data_table_utils_get_rows
        - example_data_table_utils_delete_rows
        - example_data_table_utils_get_row
        - update_row
        - example_data_table_utils_delete_row_from_datatable
        - example_create_csv_datatable
    - Rules:
        - Example: Create CSV Datatable
        - Delete Data Table Rows
        - Update Data Table Row
        - Get Data Table Rows
        - Delete Current Row
        - Delete Data Table Row
        - Update Current Row
        - Delete Rows by Name
        - Get Data Table Row
    - Data Tables:
        - dt_utils_test_data_table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)