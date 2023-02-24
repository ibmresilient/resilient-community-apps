# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.3934

"""Generate the Resilient customizations required for fn_trusteer_ppd"""

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
    Parameters required reload codegen for the fn_trusteer_ppd package
    """
    return {
        "package": u"fn_trusteer_ppd",
        "message_destinations": [u"fn_trusteer_ppd"],
        "functions": [u"trusteer_ppd_get_url_links_to_trusteer", u"trusteer_ppd_update_alert_classification"],
        "workflows": [],
        "actions": [u"Trusteer PPD: Parse Trusteer Email"],
        "incident_fields": [u"trusteer_ppd_application_id", u"trusteer_ppd_classification", u"trusteer_ppd_link_to_puid", u"trusteer_ppd_puid"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"trusteer_ppd_dt_trusteer_alerts"],
        "automatic_tasks": [],
        "scripts": [u"Trusteer PPD: Create Case from Email"],
        "playbooks": [u"trusteer_ppd_update_classification_in_trusteer", u"trusteer_ppd_update_device_url_link", u"trusteer_ppd_update_puid_url_link"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_trusteer_ppd
    - Functions:
        - trusteer_ppd_get_url_links_to_trusteer
        - trusteer_ppd_update_alert_classification
    - Playbooks:
        - trusteer_ppd_update_classification_in_trusteer
        - trusteer_ppd_update_device_url_link
        - trusteer_ppd_update_puid_url_link
    - Rules:
        - Trusteer PPD: Parse Trusteer Email
    - Incident Fields:
        - trusteer_ppd_application_id
        - trusteer_ppd_classification
        - trusteer_ppd_link_to_puid
        - trusteer_ppd_puid
    - Data Tables:
        - trusteer_ppd_dt_trusteer_alerts
    - Scripts:
        - Trusteer PPD: Create Case from Email
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)