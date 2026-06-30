# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.7.2.16540

"""Generate the SOAR customizations required for fn_artifact_utils"""

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
    Parameters required reload codegen for the fn_artifact_utils package
    """
    return {
        "package": u"fn_artifact_utils",
        "message_destinations": [
            u"fn_artifact_utils"
        ],
        "functions": [
            u"artifact_utils_add_tags",
            u"artifact_utils_delete_artifacts",
            u"artifact_utils_remove_tags",
            u"artifact_utils_search_artifacts"
        ],
        "workflows": [
            u"example_artifact_utils_add_tags_based_on_artifact_query",
            u"example_artifact_utils_delete_artifacts_based_on_query",
            u"example_artifact_utils_remove_tags_based_on_artifact_query"
        ],
        "actions": [
            u"Example: Artifact Utils: Add Tag(s) Based on Search",
            u"Example: Artifact Utils: Delete Artifacts",
            u"Example: Artifact Utils: Remove Tag(s) Based on Search"
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

    IBM SOAR Platform Version: 51.0.4.0.10290

    Contents:
    - Message Destinations:
        - fn_artifact_utils
    - Functions:
        - artifact_utils_add_tags
        - artifact_utils_delete_artifacts
        - artifact_utils_remove_tags
        - artifact_utils_search_artifacts
    - Workflows:
        - example_artifact_utils_add_tags_based_on_artifact_query
        - example_artifact_utils_delete_artifacts_based_on_query
        - example_artifact_utils_remove_tags_based_on_artifact_query
    - Rules:
        - Example: Artifact Utils: Add Tag(s) Based on Search
        - Example: Artifact Utils: Delete Artifacts
        - Example: Artifact Utils: Remove Tag(s) Based on Search
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)