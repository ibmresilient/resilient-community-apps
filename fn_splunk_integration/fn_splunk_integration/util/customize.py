# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.0.131

"""Generate the Resilient customizations required for fn_splunk_integration"""

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
    Parameters required reload codegen for the fn_splunk_integration package
    """
    return {
        "package": u"fn_splunk_integration",
        "message_destinations": [
            u"splunk_es_rest"
        ],
        "functions": [
            u"splunk_add_intel_item",
            u"splunk_delete_threat_intel_item",
            u"splunk_search",
            u"splunk_update_notable"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"splunk_notable_event_id"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"splunk_intel_results"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"splunk_add_artifact",
            u"splunk_delete_an_intel_entry",
            u"splunk_search_for_an_artifact",
            u"splunk_update_notable_event"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - splunk_es_rest
    - Functions:
        - splunk_add_intel_item
        - splunk_delete_threat_intel_item
        - splunk_search
        - splunk_update_notable
    - Playbooks:
        - splunk_add_artifact
        - splunk_delete_an_intel_entry
        - splunk_search_for_an_artifact
        - splunk_update_notable_event
    - Incident Fields:
        - splunk_notable_event_id
    - Data Tables:
        - splunk_intel_results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)