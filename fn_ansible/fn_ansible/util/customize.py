# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""Generate the SOAR customizations required for fn_ansible"""

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
    Parameters required reload codegen for the fn_ansible package
    """
    return {
        "package": u"fn_ansible",
        "message_destinations": [
            u"fn_ansible"
        ],
        "functions": [
            u"fn_ansible",
            u"fn_ansible_module"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"ansible_run_a_module",
            u"ansible_run_a_playbook",
            u"ansible_run_a_playbook_from_an_artifact"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 50.0.9097

    Contents:
    - Message Destinations:
        - fn_ansible
    - Functions:
        - fn_ansible
        - fn_ansible_module
    - Playbooks:
        - ansible_run_a_module
        - ansible_run_a_playbook
        - ansible_run_a_playbook_from_an_artifact
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)