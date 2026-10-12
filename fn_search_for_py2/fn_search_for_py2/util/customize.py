# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_search_for_py2"""

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
    Parameters required reload codegen for the fn_search_for_py2 package
    """
    return {
        "package": u"fn_search_for_py2",
        "message_destinations": [
            u"fn_search_for_py2"
        ],
        "functions": [
            u"convert_to_python_3",
            u"fn_search_for_py2"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"search_for_py2_results"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"convert_to_python_3",
            u"search_for_py2",
            u"search_for_python_2_datatable"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_search_for_py2
    - Functions:
        - convert_to_python_3
        - fn_search_for_py2
    - Playbooks:
        - convert_to_python_3
        - search_for_py2
        - search_for_python_2_datatable
    - Data Tables:
        - search_for_py2_results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)