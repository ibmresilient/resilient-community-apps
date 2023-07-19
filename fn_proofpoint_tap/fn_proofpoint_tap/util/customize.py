# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate the Resilient customizations required for fn_proofpoint_tap"""

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
    Parameters required reload codegen for the fn_proofpoint_tap package
    """
    return {
        "package": u"fn_proofpoint_tap",
        "message_destinations": [u"fn_proofpoint_tap"],
        "functions": [u"fn_pp_campaign", u"fn_pp_forensics"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"campaignId", u"messageID"],
        "incident_artifact_types": [u"proofpoint_campaign_id", u"proofpoint_threat_id"],
        "incident_types": [],
        "datatables": [u"proofpoint_tap_campaign_object_dt"],
        "automatic_tasks": [],
        "scripts": [u"Example: Proofpoint TAP - Create Artifact for Campaign Object Name or Threat"],
        "playbooks": [u"example_proofpoint_tap__aggregate_forensics_by_campaign_id_pb", u"example_proofpoint_tap__aggregate_malicious_forensics_by_threat_id_pb", u"example_proofpoint_tap__aggregate_malicious_forensics_for_entire_campaign_associated_with_threat_id_pb", u"example_proofpoint_tap__create_artifact_for_campaign_object_name_or_threat_pb", u"example_proofpoint_tap__get_campaign_information_by_campaign_id_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 49.0.8803

    Contents:
    - Message Destinations:
        - fn_proofpoint_tap
    - Functions:
        - fn_pp_campaign
        - fn_pp_forensics
    - Playbooks:
        - example_proofpoint_tap__aggregate_forensics_by_campaign_id_pb
        - example_proofpoint_tap__aggregate_malicious_forensics_by_threat_id_pb
        - example_proofpoint_tap__aggregate_malicious_forensics_for_entire_campaign_associated_with_threat_id_pb
        - example_proofpoint_tap__create_artifact_for_campaign_object_name_or_threat_pb
        - example_proofpoint_tap__get_campaign_information_by_campaign_id_pb
    - Incident Fields:
        - campaignId
        - messageID
    - Custom Artifact Types:
        - proofpoint_campaign_id
        - proofpoint_threat_id
    - Data Tables:
        - proofpoint_tap_campaign_object_dt
    - Scripts:
        - Example: Proofpoint TAP - Create Artifact for Campaign Object Name or Threat
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)