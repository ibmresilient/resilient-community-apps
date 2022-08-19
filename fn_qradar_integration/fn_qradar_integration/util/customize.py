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
        "functions": [u"qradar_add_reference_set_item", u"qradar_delete_reference_set_item", u"qradar_find_reference_set_item", u"qradar_find_reference_sets", u"qradar_get_all_reference_tables", u"qradar_reference_table_add_item", u"qradar_reference_table_delete_item", u"qradar_reference_table_get_table", u"qradar_reference_table_update_item", u"qradar_search"],
        "workflows": [u"add_a_reference_table_item", u"example_qradar__add_reference_table_item_dt", u"example_qradar__delete_reference_table_item_dt", u"example_qradar__get_all_reference_tables", u"example_qradar__update_this_reference_table_item", u"qradar_add_reference_set_item", u"qradar_find_reference_set_item", u"qradar_find_reference_sets_artifact", u"qradar_get_reference_table_data", u"qradar_move_item_to_different_ref_set", u"qradar_search_event_offense"],
        "actions": [u"Example: QRadar - Add Item to this Reference Table", u"Example: QRadar - Delete this Reference Table Item", u"Example: QRadar - Gather Reference Table Data", u"Example: QRadar - Get all Reference Tables", u"Example: QRadar - Update this Reference Table Item", u"Find All QRadar Reference Sets", u"Find in QRadar Reference Set", u"QRadar Add to Reference Set", u"QRadar Add to Reference Table", u"QRadar Move from Sample Blocked to Sample Suspected", u"Search QRadar for offense id"],
        "incident_fields": [u"qradar_destination", u"qradar_id"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"qradar_offense_event", u"qradar_reference_set", u"qradar_reference_table", u"qradar_reference_table_queried_rows"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 42.0.7058

    Contents:
    - Message Destinations:
        - fn_qradar_integration
    - Functions:
        - qradar_add_reference_set_item
        - qradar_delete_reference_set_item
        - qradar_find_reference_set_item
        - qradar_find_reference_sets
        - qradar_get_all_reference_tables
        - qradar_reference_table_add_item
        - qradar_reference_table_delete_item
        - qradar_reference_table_get_table
        - qradar_reference_table_update_item
        - qradar_search
    - Workflows:
        - add_a_reference_table_item
        - example_qradar__add_reference_table_item_dt
        - example_qradar__delete_reference_table_item_dt
        - example_qradar__get_all_reference_tables
        - example_qradar__update_this_reference_table_item
        - qradar_add_reference_set_item
        - qradar_find_reference_set_item
        - qradar_find_reference_sets_artifact
        - qradar_get_reference_table_data
        - qradar_move_item_to_different_ref_set
        - qradar_search_event_offense
    - Rules:
        - Example: QRadar - Add Item to this Reference Table
        - Example: QRadar - Delete this Reference Table Item
        - Example: QRadar - Gather Reference Table Data
        - Example: QRadar - Get all Reference Tables
        - Example: QRadar - Update this Reference Table Item
        - Find All QRadar Reference Sets
        - Find in QRadar Reference Set
        - QRadar Add to Reference Set
        - QRadar Add to Reference Table
        - QRadar Move from Sample Blocked to Sample Suspected
        - Search QRadar for offense id
    - Incident Fields:
        - qradar_destination
        - qradar_id
    - Data Tables:
        - qradar_offense_event
        - qradar_reference_set
        - qradar_reference_table
        - qradar_reference_table_queried_rows
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)