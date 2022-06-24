# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_playbook_maker"""

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
    Parameters required reload codegen for the fn_playbook_maker package
    """
    return {
        "package": u"fn_playbook_maker",
        "message_destinations": [u"fn_playbook_maker"],
        "functions": [u"make_playbook"],
        "workflows": [u"playbook_maker"],
        "actions": [u"Playbook Maker"],
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
        - fn_playbook_maker
    - Functions:
        - make_playbook
    - Workflows:
        - playbook_maker
    - Rules:
        - Playbook Maker
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)