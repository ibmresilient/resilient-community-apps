# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_soar_utils"""

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
    Parameters required reload codegen for the fn_soar_utils package
    """
    return {
        "package": u"fn_soar_utils",
        "message_destinations": [
            u"fn_soar_utils"
        ],
        "functions": [
            u"soar_utils_artifact_hash",
            u"soar_utils_attachment_hash",
            u"soar_utils_attachment_to_base64",
            u"soar_utils_attachment_zip_extract",
            u"soar_utils_attachment_zip_list",
            u"soar_utils_base64_to_artifact",
            u"soar_utils_base64_to_attachment",
            u"soar_utils_close_incident",
            u"soar_utils_create_incident",
            u"soar_utils_get_contact_info",
            u"soar_utils_search_incidents",
            u"soar_utils_soar_search",
            u"soar_utils_string_to_attachment"
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
            u"soar_utils_artifact_attachment_to_base64_example_pb",
            u"soar_utils_artifact_hash_example_pb",
            u"soar_utils_attachment_hash_example_pb",
            u"soar_utils_attachment_to_base64_example_pb",
            u"soar_utils_close_incident_example_pb",
            u"soar_utils_create_incident_example_pb",
            u"soar_utils_get_incident_contact_info_example_pb",
            u"soar_utils_get_task_contact_info_example_pb",
            u"soar_utils_search_incidents_example_pb",
            u"soar_utils_soar_search_example_pb",
            u"soar_utils_string_to_attachment_example_pb",
            u"soar_utils_zip_extract_example_pb",
            u"soar_utils_zip_extract_to_artifact_example_pb",
            u"soar_utils_zip_list_example_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_soar_utils
    - Functions:
        - soar_utils_artifact_hash
        - soar_utils_attachment_hash
        - soar_utils_attachment_to_base64
        - soar_utils_attachment_zip_extract
        - soar_utils_attachment_zip_list
        - soar_utils_base64_to_artifact
        - soar_utils_base64_to_attachment
        - soar_utils_close_incident
        - soar_utils_create_incident
        - soar_utils_get_contact_info
        - soar_utils_search_incidents
        - soar_utils_soar_search
        - soar_utils_string_to_attachment
    - Playbooks:
        - soar_utils_artifact_attachment_to_base64_example_pb
        - soar_utils_artifact_hash_example_pb
        - soar_utils_attachment_hash_example_pb
        - soar_utils_attachment_to_base64_example_pb
        - soar_utils_close_incident_example_pb
        - soar_utils_create_incident_example_pb
        - soar_utils_get_incident_contact_info_example_pb
        - soar_utils_get_task_contact_info_example_pb
        - soar_utils_search_incidents_example_pb
        - soar_utils_soar_search_example_pb
        - soar_utils_string_to_attachment_example_pb
        - soar_utils_zip_extract_example_pb
        - soar_utils_zip_extract_to_artifact_example_pb
        - soar_utils_zip_list_example_pb
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)