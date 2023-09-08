# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

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
        "functions": [u"pagerduty_create_incident", u"pagerduty_create_note", u"pagerduty_create_service", u"pagerduty_list_incidents", u"pagerduty_list_services", u"pagerduty_transition_incident"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"pd_incident_id", u"pd_incident_url"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"pagerduty_create_incident_pb", u"pagerduty_create_pagerduty_note_pb", u"pagerduty_create_service_pb", u"pagerduty_list_incidents_pb", u"pagerduty_list_services_pb", u"pagerduty_resolve_pagerduty_incident_pb", u"pagerduty_update_pagerduty_incident_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - pagerduty
    - Functions:
        - pagerduty_create_incident
        - pagerduty_create_note
        - pagerduty_create_service
        - pagerduty_list_incidents
        - pagerduty_list_services
        - pagerduty_transition_incident
    - Playbooks:
        - pagerduty_create_incident_pb
        - pagerduty_create_pagerduty_note_pb
        - pagerduty_create_service_pb
        - pagerduty_list_incidents_pb
        - pagerduty_list_services_pb
        - pagerduty_resolve_pagerduty_incident_pb
        - pagerduty_update_pagerduty_incident_pb
    - Incident Fields:
        - pd_incident_id
        - pd_incident_url
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)