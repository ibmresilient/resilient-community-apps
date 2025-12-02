# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_proofpoint_trap"""

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
    Parameters required reload codegen for the fn_proofpoint_trap package
    """
    return {
        "package": u"fn_proofpoint_trap",
        "message_destinations": [
            u"fn_proofpoint_trap"
        ],
        "functions": [
            u"fn_proofpoint_trap_add_members_to_list",
            u"fn_proofpoint_trap_delete_list_member",
            u"fn_proofpoint_trap_get_incident_details",
            u"fn_proofpoint_trap_get_list_members",
            u"fn_proofpoint_trap_update_list_member"
        ],
        "workflows": [
            u"wf_proofpoint_trap_add_member_to_list",
            u"wf_proofpoint_trap_delete_list_member",
            u"wf_proofpoint_trap_get_incident_details",
            u"wf_proofpoint_trap_get_list_members",
            u"wf_proofpoint_trap_update_list_member"
        ],
        "actions": [
            u"Example: Proofpoint TRAP: Add Member to List",
            u"Example: Proofpoint TRAP: Delete List Member",
            u"Example: Proofpoint TRAP: Get Incident Details",
            u"Example: Proofpoint TRAP: Get List Members",
            u"Example: Proofpoint TRAP: Update List Member"
        ],
        "incident_fields": [
            u"proofpoint_trap_incident_id"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"proofpoint_trap_events",
            u"trap_list_members"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_proofpoint_trap
    - Functions:
        - fn_proofpoint_trap_add_members_to_list
        - fn_proofpoint_trap_delete_list_member
        - fn_proofpoint_trap_get_incident_details
        - fn_proofpoint_trap_get_list_members
        - fn_proofpoint_trap_update_list_member
    - Workflows:
        - wf_proofpoint_trap_add_member_to_list
        - wf_proofpoint_trap_delete_list_member
        - wf_proofpoint_trap_get_incident_details
        - wf_proofpoint_trap_get_list_members
        - wf_proofpoint_trap_update_list_member
    - Rules:
        - Example: Proofpoint TRAP: Add Member to List
        - Example: Proofpoint TRAP: Delete List Member
        - Example: Proofpoint TRAP: Get Incident Details
        - Example: Proofpoint TRAP: Get List Members
        - Example: Proofpoint TRAP: Update List Member
    - Incident Fields:
        - proofpoint_trap_incident_id
    - Data Tables:
        - proofpoint_trap_events
        - trap_list_members
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)