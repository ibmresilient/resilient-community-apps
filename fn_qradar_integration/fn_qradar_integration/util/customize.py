# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

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
        "workflows": [],
        "actions": [],
        "incident_fields": [u"qradar_destination", u"qradar_id"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"qradar_offense_event", u"qradar_reference_set", u"qradar_reference_table", u"qradar_reference_table_queried_rows"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"find_in_qradar_reference_set_pb", u"get_all_qradar_reference_sets", u"qradar_add_item_to_this_reference_table_example", u"qradar_add_to_reference_set", u"qradar_add_to_reference_table", u"qradar_delete_this_reference_table_item_example", u"qradar_gather_reference_table_data_example", u"qradar_get_all_reference_tables_example", u"qradar_move_from_sample_blocked_to_sample_suspected", u"qradar_update_this_reference_table_item_example", u"search_qradar_for_offense_id"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

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
    - Playbooks:
        - find_in_qradar_reference_set_pb
        - get_all_qradar_reference_sets
        - qradar_add_item_to_this_reference_table_example
        - qradar_add_to_reference_set
        - qradar_add_to_reference_table
        - qradar_delete_this_reference_table_item_example
        - qradar_gather_reference_table_data_example
        - qradar_get_all_reference_tables_example
        - qradar_move_from_sample_blocked_to_sample_suspected
        - qradar_update_this_reference_table_item_example
        - search_qradar_for_offense_id
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