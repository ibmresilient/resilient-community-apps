# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_qradar_integration"""

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
    Parameters required reload codegen for the fn_qradar_integration package
    """
    return {
        "package": u"fn_qradar_integration",
        "message_destinations": [u"fn_qradar_integration"],
        "functions": [u"qradar_reference_table_get_table", u"qradar_get_all_reference_tables", u"qradar_find_reference_sets", u"qradar_reference_table_delete_item", u"qradar_find_reference_set_item", u"qradar_get_reference_set_data", u"qradar_reference_table_add_item", u"qradar_add_reference_set_item", u"qradar_reference_set_update_item", u"qradar_get_all_servers", u"qradar_reference_table_update_item", u"qradar_search", u"qradar_delete_reference_set_item", u"qradar_find_all_reference_sets"],
        "workflows": [u"qradar_find_reference_sets_artifact", u"example_qradar__update_this_reference_table_item", u"example_qradar__get_all_reference_tables", u"example_qradar__gather_reference_set_data", u"example_qradar__get_all_reference_sets", u"example_qradar__delete_this_reference_set_item", u"qradar_find_reference_set_item", u"qradar_move_item_to_different_ref_set", u"qradar_search_event", u"qradar_add_reference_set_item", u"example_qradar__get_all_servers", u"qradar_get_reference_table_data", u"example_qradar__add_reference_table_item_dt", u"example_qradar__delete_reference_table_item_dt", u"example_qradar__update_this_reference_set_item"],
        "actions": [u"Example: QRadar - Add Item to this Reference Table", u"Example: QRadar - Get all Reference Tables", u"Example: QRadar - Add Item to this Reference Set", u"Example: QRadar - Find in Reference Set", u"Example: QRadar - Update this Reference Table Item", u"Example: QRadar - Move from one Reference Set to another Reference Set", u"Example: QRadar - Gather Reference Set Data", u"Example: QRadar - Delete this Reference Set Item", u"Example: QRadar - Get all Reference Sets", u"Example: QRadar - Search for Source IP", u"Example: QRadar - Gather Reference Table Data", u"Example: QRadar - Delete this Reference Table Item", u"Example: QRadar - Get all Servers", u"Example: QRadar - Update this Reference Set Item", u"Example: QRadar - Find All Reference Sets with Artifact"],
        "incident_fields": [u"qradar_id"],
        "incident_artifact_types": [],
        "datatables": [u"qradar_servers", u"qradar_offense_event", u"qradar_reference_set_queried_rows", u"qradar_reference_set", u"qradar_reference_table_queried_rows", u"qradar_reference_table"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.6328

    Contents:
    - Message Destinations:
        - fn_qradar_integration
    - Functions:
        - qradar_reference_table_get_table
        - qradar_get_all_reference_tables
        - qradar_find_reference_sets
        - qradar_reference_table_delete_item
        - qradar_find_reference_set_item
        - qradar_get_reference_set_data
        - qradar_reference_table_add_item
        - qradar_add_reference_set_item
        - qradar_reference_set_update_item
        - qradar_get_all_servers
        - qradar_reference_table_update_item
        - qradar_search
        - qradar_delete_reference_set_item
        - qradar_find_all_reference_sets
    - Workflows:
        - qradar_find_reference_sets_artifact
        - example_qradar__update_this_reference_table_item
        - example_qradar__get_all_reference_tables
        - example_qradar__gather_reference_set_data
        - example_qradar__get_all_reference_sets
        - example_qradar__delete_this_reference_set_item
        - qradar_find_reference_set_item
        - qradar_move_item_to_different_ref_set
        - qradar_search_event
        - qradar_add_reference_set_item
        - example_qradar__get_all_servers
        - qradar_get_reference_table_data
        - example_qradar__add_reference_table_item_dt
        - example_qradar__delete_reference_table_item_dt
        - example_qradar__update_this_reference_set_item
    - Rules:
        - Example: QRadar - Add Item to this Reference Table
        - Example: QRadar - Get all Reference Tables
        - Example: QRadar - Add Item to this Reference Set
        - Example: QRadar - Find in Reference Set
        - Example: QRadar - Update this Reference Table Item
        - Example: QRadar - Move from one Reference Set to another Reference Set
        - Example: QRadar - Gather Reference Set Data
        - Example: QRadar - Delete this Reference Set Item
        - Example: QRadar - Get all Reference Sets
        - Example: QRadar - Search for Source IP
        - Example: QRadar - Gather Reference Table Data
        - Example: QRadar - Delete this Reference Table Item
        - Example: QRadar - Get all Servers
        - Example: QRadar - Update this Reference Set Item
        - Example: QRadar - Find All Reference Sets with Artifact
    - Incident Fields:
        - qradar_id
    - Data Tables:
        - qradar_servers
        - qradar_offense_event
        - qradar_reference_set_queried_rows
        - qradar_reference_set
        - qradar_reference_table_queried_rows
        - qradar_reference_table
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)