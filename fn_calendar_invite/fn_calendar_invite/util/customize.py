# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_calendar_invite"""

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
    Parameters required reload codegen for the fn_calendar_invite package
    """
    return {
        "package": u"fn_calendar_invite",
        "message_destinations": [u"fn_calendar_invite"],
        "functions": [u"fn_calendar_invite"],
        "workflows": [u"example_calendar_invite"],
        "actions": [u"Example: Calendar Invite"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
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
        - fn_calendar_invite
    - Functions:
        - fn_calendar_invite
    - Workflows:
        - example_calendar_invite
    - Rules:
        - Example: Calendar Invite
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)