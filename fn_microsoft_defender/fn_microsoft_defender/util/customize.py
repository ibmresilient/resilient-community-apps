# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_microsoft_defender"""

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
    Parameters required reload codegen for the fn_microsoft_defender package
    """
    return {
        "package": u"fn_microsoft_defender",
        "message_destinations": [u"fn_msdefender"],
        "functions": [u"defender_find_machines_by_file", u"defender_find_machines", u"defender_list_indicators", u"defender_delete_indicator", u"defender_app_execution", u"defender_machine_isolation", u"defender_quarantine_file", u"defender_set_indicator"],
        "workflows": [u"defender_atp_set_indicator", u"defender_atp_app_execution", u"defender_atp_machine_isolation", u"defender_list_indicators", u"defender_atp_find_machines", u"defender_atp_find_machines_by_file_hash", u"defender_atp_update_indicator", u"defender_quarantine_file", u"defender_atp_delete_indicator"],
        "actions": [u"Update Indicator", u"Defender ATP Quarantine Machine File", u"Defender ATP App Execution Restriction", u"Defender ATP Machine Isolate Action", u"Create Artifact from Indicator", u"Delete Indicator", u"Defender ATP List Indicators", u"Defender ATP Set Indicator", u"Defender ATP Find Machines", u"Defender ATP Find Machines by File Hash"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"defender_atp_indicators", u"defender_atp_machines"],
        "automatic_tasks": [],
        "scripts": [u"Create Artifact from Indicator"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 36.0.5634

    Contents:
    - Message Destinations:
        - fn_msdefender
    - Functions:
        - defender_find_machines_by_file
        - defender_find_machines
        - defender_list_indicators
        - defender_delete_indicator
        - defender_app_execution
        - defender_machine_isolation
        - defender_quarantine_file
        - defender_set_indicator
    - Workflows:
        - defender_atp_set_indicator
        - defender_atp_app_execution
        - defender_atp_machine_isolation
        - defender_list_indicators
        - defender_atp_find_machines
        - defender_atp_find_machines_by_file_hash
        - defender_atp_update_indicator
        - defender_quarantine_file
        - defender_atp_delete_indicator
    - Rules:
        - Update Indicator
        - Defender ATP Quarantine Machine File
        - Defender ATP App Execution Restriction
        - Defender ATP Machine Isolate Action
        - Create Artifact from Indicator
        - Delete Indicator
        - Defender ATP List Indicators
        - Defender ATP Set Indicator
        - Defender ATP Find Machines
        - Defender ATP Find Machines by File Hash
    - Data Tables:
        - defender_atp_indicators
        - defender_atp_machines
    - Scripts:
        - Create Artifact from Indicator
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)