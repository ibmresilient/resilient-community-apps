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
        "functions": [u"qradar_find_reference_set_item", u"qradar_delete_reference_set_item", u"qradar_reference_table_add_item", u"qradar_search", u"qradar_reference_table_update_item", u"qradar_reference_table_delete_item", u"qradar_find_reference_sets", u"qradar_reference_table_get_table", u"qradar_add_reference_set_item", u"qradar_get_reference_tables"],
        "workflows": [u"qradar_find_reference_set_item", u"qradar_move_item_to_different_ref_set", u"example_qradar__update_this_reference_table_item", u"qradar_get_reference_table_data", u"example_qradar__add_reference_table_item_dt", u"qradar_search_event_offense", u"example_qradar__get_all_reference_tables", u"qradar_find_reference_sets_artifact", u"qradar_add_reference_set_item", u"example_qradar__delete_reference_table_item_dt"],
        "actions": [u"Find All QRadar Reference Sets", u"Example: QRadar - Gather Reference Table Data", u"Find in QRadar Reference Set", u"Example: QRadar - Get all Reference Tables", u"Search QRadar for offense id", u"QRadar Move from Sample Blocked to Sample Suspected", u"Example: QRadar - Delete this Reference Table Item", u"Example: QRadar - Update this Reference Table Item", u"QRadar Add to Reference Set", u"Example: QRadar - Add Item to this Reference Table"],
        "incident_fields": [u"qradar_id"],
        "incident_artifact_types": [],
        "datatables": [u"qradar_reference_table", u"qradar_offense_event", u"qradar_reference_set", u"qradar_reference_table_queried_rows"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 37.0.5832

    Contents:
    - Message Destinations:
        - fn_qradar_integration
    - Functions:
        - qradar_find_reference_set_item
        - qradar_delete_reference_set_item
        - qradar_reference_table_add_item
        - qradar_search
        - qradar_reference_table_update_item
        - qradar_reference_table_delete_item
        - qradar_find_reference_sets
        - qradar_reference_table_get_table
        - qradar_add_reference_set_item
        - qradar_get_reference_tables
    - Workflows:
        - qradar_find_reference_set_item
        - qradar_move_item_to_different_ref_set
        - example_qradar__update_this_reference_table_item
        - qradar_get_reference_table_data
        - example_qradar__add_reference_table_item_dt
        - qradar_search_event_offense
        - example_qradar__get_all_reference_tables
        - qradar_find_reference_sets_artifact
        - qradar_add_reference_set_item
        - example_qradar__delete_reference_table_item_dt
    - Rules:
        - Find All QRadar Reference Sets
        - Example: QRadar - Gather Reference Table Data
        - Find in QRadar Reference Set
        - Example: QRadar - Get all Reference Tables
        - Search QRadar for offense id
        - QRadar Move from Sample Blocked to Sample Suspected
        - Example: QRadar - Delete this Reference Table Item
        - Example: QRadar - Update this Reference Table Item
        - QRadar Add to Reference Set
        - Example: QRadar - Add Item to this Reference Table
    - Incident Fields:
        - qradar_id
    - Data Tables:
        - qradar_reference_table
        - qradar_offense_event
        - qradar_reference_set
        - qradar_reference_table_queried_rows
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)