# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_epo"""

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
    Parameters required reload codegen for the fn_mcafee_epo package
    """
    return {
        "package": u"fn_mcafee_epo",
        "message_destinations": [u"mcafee_epo_message_destination"],
        "functions": [u"mcafee_epo_find_a_system", u"mcafee_epo_list_tags", u"mcafee_epo_remove_tag", u"mcafee_tag_an_epo_asset"],
        "workflows": [u"mcafee_epo_apply_a_tag", u"mcafee_epo_apply_tags", u"mcafee_epo_get_system_info", u"mcafee_epo_list_tags", u"mcafee_epo_remove_tag"],
        "actions": [u"McAfee ePO apply a tag", u"McAfee ePO apply tags", u"McAfee ePO get system info", u"McAfee ePO list tags", u"McAfee ePO remove tags"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"mcafee_epo_tags"],
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
        - mcafee_epo_message_destination
    - Functions:
        - mcafee_epo_find_a_system
        - mcafee_epo_list_tags
        - mcafee_epo_remove_tag
        - mcafee_tag_an_epo_asset
    - Workflows:
        - mcafee_epo_apply_a_tag
        - mcafee_epo_apply_tags
        - mcafee_epo_get_system_info
        - mcafee_epo_list_tags
        - mcafee_epo_remove_tag
    - Rules:
        - McAfee ePO apply a tag
        - McAfee ePO apply tags
        - McAfee ePO get system info
        - McAfee ePO list tags
        - McAfee ePO remove tags
    - Data Tables:
        - mcafee_epo_tags
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)