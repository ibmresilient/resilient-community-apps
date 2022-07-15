# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_pagerduty"""

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
    Parameters required reload codegen for the fn_pagerduty package
    """
    return {
        "package": u"fn_pagerduty",
        "message_destinations": [u"pagerduty"],
        "functions": [u"pagerduty_create_incident", u"pagerduty_create_note", u"pagerduty_transition_incident"],
        "workflows": [u"pagerduty_create_incident", u"pagerduty_create_note", u"pagerduty_transition_incident"],
        "actions": [u"Create PagerDuty Note", u"Resolve PagerDuty Incident", u"Trigger PagerDuty Incident", u"Update PagerDuty Incident"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - pagerduty
    - Functions:
        - pagerduty_create_incident
        - pagerduty_create_note
        - pagerduty_transition_incident
    - Workflows:
        - pagerduty_create_incident
        - pagerduty_create_note
        - pagerduty_transition_incident
    - Rules:
        - Create PagerDuty Note
        - Resolve PagerDuty Incident
        - Trigger PagerDuty Incident
        - Update PagerDuty Incident
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)