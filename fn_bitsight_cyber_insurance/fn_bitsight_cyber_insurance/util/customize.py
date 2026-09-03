# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_bitsight_cyber_insurance"""

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
    Parameters required reload codegen for the fn_bitsight_cyber_insurance package
    """
    return {
        "package": u"fn_bitsight_cyber_insurance",
        "message_destinations": [
            u"fn_bitsight_cyber_insurance"
        ],
        "functions": [
            u"bitsight_cyber_insurance_get_alerts",
            u"bitsight_cyber_insurance_get_company_details",
            u"bitsight_cyber_insurance_get_company_search",
            u"bitsight_cyber_insurance_get_finding_details",
            u"bitsight_cyber_insurance_get_latest_alerts",
            u"bitsight_cyber_insurance_get_portfolio_details"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"bitsight_cyber_insurance_alerts",
            u"bitsight_cyber_insurance_companies"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"bitsight_cyber_insurance_get_alerts",
            u"bitsight_cyber_insurance_get_company_details",
            u"bitsight_cyber_insurance_get_company_search",
            u"bitsight_cyber_insurance_get_finding_details",
            u"bitsight_cyber_insurance_get_latest_alerts",
            u"bitsight_cyber_insurance_get_portfolio_details"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_bitsight_cyber_insurance
    - Functions:
        - bitsight_cyber_insurance_get_alerts
        - bitsight_cyber_insurance_get_company_details
        - bitsight_cyber_insurance_get_company_search
        - bitsight_cyber_insurance_get_finding_details
        - bitsight_cyber_insurance_get_latest_alerts
        - bitsight_cyber_insurance_get_portfolio_details
    - Playbooks:
        - bitsight_cyber_insurance_get_alerts
        - bitsight_cyber_insurance_get_company_details
        - bitsight_cyber_insurance_get_company_search
        - bitsight_cyber_insurance_get_finding_details
        - bitsight_cyber_insurance_get_latest_alerts
        - bitsight_cyber_insurance_get_portfolio_details
    - Data Tables:
        - bitsight_cyber_insurance_alerts
        - bitsight_cyber_insurance_companies
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)