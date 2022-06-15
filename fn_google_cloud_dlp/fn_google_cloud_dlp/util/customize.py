# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_google_cloud_dlp"""

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
    Parameters required reload codegen for the fn_google_cloud_dlp package
    """
    return {
        "package": u"fn_google_cloud_dlp",
        "message_destinations": [u"fn_google_cloud_dlp"],
        "functions": [u"google_cloud_dlp_deidentify_content", u"google_cloud_dlp_inspect_content"],
        "workflows": [u"gcp_dlp_deidentify_artifact", u"gcp_dlp_deidentify_attachment", u"gcp_dlp_inspect_attachment"],
        "actions": [u"Example: Google Cloud - Inspect Attachment for PII", u"Example: Google Cloud - Remove PII from Attachment", u"Example: Google Cloud - Remove PII from String"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 40.0.6554

    Contents:
    - Message Destinations:
        - fn_google_cloud_dlp
    - Functions:
        - google_cloud_dlp_deidentify_content
        - google_cloud_dlp_inspect_content
    - Workflows:
        - gcp_dlp_deidentify_artifact
        - gcp_dlp_deidentify_attachment
        - gcp_dlp_inspect_attachment
    - Rules:
        - Example: Google Cloud - Inspect Attachment for PII
        - Example: Google Cloud - Remove PII from Attachment
        - Example: Google Cloud - Remove PII from String
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)