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
        "functions": [u"qradar_get_all_servers", u"qradar_reference_table_update_item", u"qradar_get_all_reference_tables", u"qradar_search", u"qradar_reference_table_delete_item", u"qradar_find_reference_set_item", u"qradar_reference_set_update_item", u"qradar_reference_table_get_table", u"qradar_add_reference_set_item", u"qradar_get_reference_set_data", u"qradar_reference_table_add_item", u"qradar_find_reference_sets", u"qradar_delete_reference_set_item", u"qradar_find_all_reference_sets"],
        "workflows": [u"example_qradar__delete_reference_table_item_dt", u"example_qradar__update_this_reference_table_item", u"qradar_find_reference_sets_artifact", u"example_qradar__get_all_reference_tables", u"add_a_reference_table_item", u"qradar_get_reference_table_data", u"example_qradar__add_reference_table_item_dt", u"qradar_find_reference_set_item", u"qradar_add_reference_set_item", u"qradar_move_item_to_different_ref_set", u"qradar_search_event_offense"],
        "actions": [u"Search QRadar for offense id", u"QRadar Add to Reference Set", u"Find All QRadar Reference Sets", u"QRadar Move from Sample Blocked to Sample Suspected", u"Find in QRadar Reference Set", u"Example: QRadar - Update this Reference Table Item", u"Example: QRadar - Delete this Reference Table Item", u"Example: QRadar - Get all Reference Tables", u"Example: QRadar - Add Item to this Reference Table", u"Example: QRadar - Gather Reference Table Data", u"QRadar Add to Reference Table"],
        "incident_fields": [u"qradar_id", u"qradar_server"],
        "incident_artifact_types": [],
        "datatables": [u"qradar_reference_table", u"qradar_reference_set", u"qradar_reference_table_queried_rows", u"qradar_offense_event"],
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
        - qradar_get_all_servers
        - qradar_reference_table_update_item
        - qradar_get_all_reference_tables
        - qradar_search
        - qradar_reference_table_delete_item
        - qradar_find_reference_set_item
        - qradar_reference_set_update_item
        - qradar_reference_table_get_table
        - qradar_add_reference_set_item
        - qradar_get_reference_set_data
        - qradar_reference_table_add_item
        - qradar_find_reference_sets
        - qradar_delete_reference_set_item
        - qradar_find_all_reference_sets
    - Workflows:
        - example_qradar__delete_reference_table_item_dt
        - example_qradar__update_this_reference_table_item
        - qradar_find_reference_sets_artifact
        - example_qradar__get_all_reference_tables
        - add_a_reference_table_item
        - qradar_get_reference_table_data
        - example_qradar__add_reference_table_item_dt
        - qradar_find_reference_set_item
        - qradar_add_reference_set_item
        - qradar_move_item_to_different_ref_set
        - qradar_search_event_offense
    - Rules:
        - Search QRadar for offense id
        - QRadar Add to Reference Set
        - Find All QRadar Reference Sets
        - QRadar Move from Sample Blocked to Sample Suspected
        - Find in QRadar Reference Set
        - Example: QRadar - Update this Reference Table Item
        - Example: QRadar - Delete this Reference Table Item
        - Example: QRadar - Get all Reference Tables
        - Example: QRadar - Add Item to this Reference Table
        - Example: QRadar - Gather Reference Table Data
        - QRadar Add to Reference Table
    - Incident Fields:
        - qradar_id
        - qradar_server
    - Data Tables:
        - qradar_reference_table
        - qradar_reference_set
        - qradar_reference_table_queried_rows
        - qradar_offense_event
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)