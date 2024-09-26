# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

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
        "workflows": [
            u"example_soar_utilities_artifact_attachment_to_base64",
            u"example_soar_utilities_artifact_hash",
            u"example_soar_utilities_attachment_hash",
            u"example_soar_utilities_attachment_to_base64",
            u"example_soar_utilities_close_incident",
            u"example_soar_utilities_create_incident",
            u"example_soar_utilities_get_incident_contact_info",
            u"example_soar_utilities_get_task_contact_info",
            u"example_soar_utilities_search_incidents",
            u"example_soar_utilities_soar_search",
            u"example_soar_utilities_string_to_attachment",
            u"example_soar_utilities_zip_extract",
            u"example_soar_utilities_zip_extract_to_artifact",
            u"example_soar_utilities_zip_list"
        ],
        "actions": [
            u"Example: SOAR Utilities (Artifact) Attachment to Base64",
            u"Example: SOAR Utilities Artifact Hash",
            u"Example: SOAR Utilities Attachment Hash",
            u"Example: SOAR Utilities Attachment to Base64",
            u"Example: SOAR Utilities Close Incident",
            u"Example: SOAR Utilities Create Incident",
            u"Example: SOAR Utilities Get Incident Contact Info",
            u"Example: SOAR Utilities Get Task Contact Info",
            u"Example: SOAR Utilities Search Incidents",
            u"Example: SOAR Utilities SOAR Search",
            u"Example: SOAR Utilities String to Attachment",
            u"Example: SOAR Utilities Zip Extract",
            u"Example: SOAR Utilities Zip Extract to Artifact",
            u"Example: SOAR Utilities Zip List"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

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
    - Workflows:
        - example_soar_utilities_artifact_attachment_to_base64
        - example_soar_utilities_artifact_hash
        - example_soar_utilities_attachment_hash
        - example_soar_utilities_attachment_to_base64
        - example_soar_utilities_close_incident
        - example_soar_utilities_create_incident
        - example_soar_utilities_get_incident_contact_info
        - example_soar_utilities_get_task_contact_info
        - example_soar_utilities_search_incidents
        - example_soar_utilities_soar_search
        - example_soar_utilities_string_to_attachment
        - example_soar_utilities_zip_extract
        - example_soar_utilities_zip_extract_to_artifact
        - example_soar_utilities_zip_list
    - Rules:
        - Example: SOAR Utilities (Artifact) Attachment to Base64
        - Example: SOAR Utilities Artifact Hash
        - Example: SOAR Utilities Attachment Hash
        - Example: SOAR Utilities Attachment to Base64
        - Example: SOAR Utilities Close Incident
        - Example: SOAR Utilities Create Incident
        - Example: SOAR Utilities Get Incident Contact Info
        - Example: SOAR Utilities Get Task Contact Info
        - Example: SOAR Utilities Search Incidents
        - Example: SOAR Utilities SOAR Search
        - Example: SOAR Utilities String to Attachment
        - Example: SOAR Utilities Zip Extract
        - Example: SOAR Utilities Zip Extract to Artifact
        - Example: SOAR Utilities Zip List
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)