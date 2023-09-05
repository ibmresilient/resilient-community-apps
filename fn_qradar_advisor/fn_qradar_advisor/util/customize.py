# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_qradar_advisor"""

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
    Parameters required reload codegen for the fn_qradar_advisor package
    """
    return {
        "package": u"fn_qradar_advisor",
        "message_destinations": [u"fn_qradar_advisor"],
        "functions": [u"qradar_advisor_full_search", u"qradar_advisor_map_rule", u"qradar_advisor_offense_analysis", u"qradar_advisor_quick_search"],
        "workflows": [u"qradar_advisor_full_search", u"qradar_advisor_map_rule", u"qradar_advisor_offense_analysis", u"qradar_advisor_quick_search"],
        "actions": [u"Create Artifact (QRadar Advisor Analysis)", u"Create Artifact (Watson Search with Local Context)", u"QRadar Advisor: Map QRadar rule", u"QRadar Advisor: Offense Analysis", u"Watson Search", u"Watson Search with Local Context"],
        "incident_fields": [u"mitre_tactic_name", u"qradar_id", u"qradar_rule"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"qradar_advisor_observable", u"qradar_advisor_observable_for_artifact"],
        "automatic_tasks": [],
        "scripts": [u"Create Artifact for QRadar Advisor Analysis Observable", u"Create Artifact for Watson Search with Local Context"],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 44.0.7583

    Contents:
    - Message Destinations:
        - fn_qradar_advisor
    - Functions:
        - qradar_advisor_full_search
        - qradar_advisor_map_rule
        - qradar_advisor_offense_analysis
        - qradar_advisor_quick_search
    - Workflows:
        - qradar_advisor_full_search
        - qradar_advisor_map_rule
        - qradar_advisor_offense_analysis
        - qradar_advisor_quick_search
    - Rules:
        - Create Artifact (QRadar Advisor Analysis)
        - Create Artifact (Watson Search with Local Context)
        - QRadar Advisor: Map QRadar rule
        - QRadar Advisor: Offense Analysis
        - Watson Search
        - Watson Search with Local Context
    - Incident Fields:
        - mitre_tactic_name
        - qradar_id
        - qradar_rule
    - Data Tables:
        - qradar_advisor_observable
        - qradar_advisor_observable_for_artifact
    - Scripts:
        - Create Artifact for QRadar Advisor Analysis Observable
        - Create Artifact for Watson Search with Local Context
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)