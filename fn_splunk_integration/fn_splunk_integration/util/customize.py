# -*- coding: utf-8 -*-

"""Generate the SOAR customizations required for fn_splunk_integration"""

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
        "message_destinations": [u"splunk_es_rest"],
        "functions": [u"splunk_add_intel_item", u"splunk_delete_threat_intel_item", u"splunk_search", u"splunk_update_notable"],
        "workflows": [u"example_of_deleting_an_intel_entry_in_splunk_es", u"search_splunk_ip_intel", u"splunk_add_new_ip_intel", u"splunk_update_notable"],
        "actions": [u"Add artifact to Splunk ES", u"Delete an intel entry in Splunk ES", u"Search Splunk ES for an artifact", u"Update Splunk ES notable event"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"splunk_intel_results"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 42.0.7058

    Contents:
    - Message Destinations:
        - splunk_es_rest
    - Functions:
        - splunk_add_intel_item
        - splunk_delete_threat_intel_item
        - splunk_search
        - splunk_update_notable
    - Workflows:
        - example_of_deleting_an_intel_entry_in_splunk_es
        - search_splunk_ip_intel
        - splunk_add_new_ip_intel
        - splunk_update_notable
    - Rules:
        - Add artifact to Splunk ES
        - Delete an intel entry in Splunk ES
        - Search Splunk ES for an artifact
        - Update Splunk ES notable event
    - Data Tables:
        - splunk_intel_results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)