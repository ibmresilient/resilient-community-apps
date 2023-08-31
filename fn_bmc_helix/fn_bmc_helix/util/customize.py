# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.0.131

"""Generate the Resilient customizations required for fn_bmc_helix"""

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
    Parameters required reload codegen for the fn_bmc_helix package
    """
    return {
        "package": u"fn_bmc_helix",
        "message_destinations": [
            u"fn_bmc_helix"
        ],
        "functions": [
            u"helix_close_incident",
            u"helix_create_incident"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"bmc_helix_assigned_support_organization",
            u"bmc_helix_assigned_to",
            u"bmc_helix_company",
            u"bmc_helix_created_date",
            u"bmc_helix_description",
            u"bmc_helix_impact",
            u"bmc_helix_incident_number",
            u"bmc_helix_organization",
            u"bmc_helix_priority",
            u"bmc_helix_request_id",
            u"bmc_helix_status",
            u"bmc_helix_task_linked",
            u"bmc_helix_urgency"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"bmc_helix_incidents"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"bmc_helix_close_incident",
            u"bmc_helix_close_incident_from_task",
            u"bmc_helix_create_incident",
            u"bmc_helix_create_incident_from_task"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_bmc_helix
    - Functions:
        - helix_close_incident
        - helix_create_incident
    - Playbooks:
        - bmc_helix_close_incident
        - bmc_helix_close_incident_from_task
        - bmc_helix_create_incident
        - bmc_helix_create_incident_from_task
    - Incident Fields:
        - bmc_helix_assigned_support_organization
        - bmc_helix_assigned_to
        - bmc_helix_company
        - bmc_helix_created_date
        - bmc_helix_description
        - bmc_helix_impact
        - bmc_helix_incident_number
        - bmc_helix_organization
        - bmc_helix_priority
        - bmc_helix_request_id
        - bmc_helix_status
        - bmc_helix_task_linked
        - bmc_helix_urgency
    - Data Tables:
        - bmc_helix_incidents
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)