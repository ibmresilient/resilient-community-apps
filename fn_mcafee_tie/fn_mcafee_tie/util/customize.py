# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_tie"""

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
    Parameters required reload codegen for the fn_mcafee_tie package
    """
    return {
        "package": u"fn_mcafee_tie",
        "message_destinations": [u"mcafee_tie_md"],
        "functions": [u"mcafee_tie_set_file_reputation", u"mcafee_tie_search_hash"],
        "workflows": [u"mcafee_tie_set_reputation__datatable", u"mcafee_tie_set_file_reputation", u"mcafee_tie_get_latest_reputation", u"mcafee_tie_get_file_reputation"],
        "actions": [u"McAfee TIE Set File Reputation", u"McAfee TIE Get Current Reputation", u"McAfee TIE Get File Reputation", u"McAfee TIE Set File Reputation - Datatable"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"tie_results"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 36.0.5634

    Contents:
    - Message Destinations:
        - mcafee_tie_md
    - Functions:
        - mcafee_tie_set_file_reputation
        - mcafee_tie_search_hash
    - Workflows:
        - mcafee_tie_set_reputation__datatable
        - mcafee_tie_set_file_reputation
        - mcafee_tie_get_latest_reputation
        - mcafee_tie_get_file_reputation
    - Rules:
        - McAfee TIE Set File Reputation
        - McAfee TIE Get Current Reputation
        - McAfee TIE Get File Reputation
        - McAfee TIE Set File Reputation - Datatable
    - Data Tables:
        - tie_results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)