# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_mitre_integration"""

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
    Parameters required reload codegen for the fn_mitre_integration package
    """
    return {
        "package": u"fn_mitre_integration",
        "message_destinations": [
            u"fn_mitre_integration"
        ],
        "functions": [
            u"mitre_groups_technique_intersection",
            u"mitre_groups_using_technique",
            u"mitre_tactic_information",
            u"mitre_technique_information",
            u"mitre_techniques_software"
        ],
        "workflows": [
            u"mitre_get_groups_using_all_techniques",
            u"mitre_get_groups_using_techniques",
            u"mitre_get_software_for_a_technique",
            u"mitre_get_tactic_information",
            u"mitre_get_technique_information",
            u"mitre_technique_task"
        ],
        "actions": [
            u"MITRE: Create Task for ATT&CK Technique",
            u"MITRE: Get Groups per Technique",
            u"MITRE: Get Groups using all Techniques",
            u"MITRE: Get Tactic information",
            u"MITRE: Get Technique information",
            u"MITRE: Get Technique's Software"
        ],
        "incident_fields": [
            u"mitre_tactic_id",
            u"mitre_tactic_name",
            u"mitre_technique_id",
            u"mitre_technique_name"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"mitre_attack_groups",
            u"mitre_attack_of_incident",
            u"mitre_attack_software",
            u"mitre_attack_techniques"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_mitre_integration
    - Functions:
        - mitre_groups_technique_intersection
        - mitre_groups_using_technique
        - mitre_tactic_information
        - mitre_technique_information
        - mitre_techniques_software
    - Workflows:
        - mitre_get_groups_using_all_techniques
        - mitre_get_groups_using_techniques
        - mitre_get_software_for_a_technique
        - mitre_get_tactic_information
        - mitre_get_technique_information
        - mitre_technique_task
    - Rules:
        - MITRE: Create Task for ATT&CK Technique
        - MITRE: Get Groups per Technique
        - MITRE: Get Groups using all Techniques
        - MITRE: Get Tactic information
        - MITRE: Get Technique information
        - MITRE: Get Technique's Software
    - Incident Fields:
        - mitre_tactic_id
        - mitre_tactic_name
        - mitre_technique_id
        - mitre_technique_name
    - Data Tables:
        - mitre_attack_groups
        - mitre_attack_of_incident
        - mitre_attack_software
        - mitre_attack_techniques
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)