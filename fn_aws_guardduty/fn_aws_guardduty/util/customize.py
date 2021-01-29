# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_aws_guardduty"""

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
    Parameters required reload codegen for the fn_aws_guardduty package
    """
    return {
        "package": u"fn_aws_guardduty",
        "message_destinations": [u"fn_aws_gd"],
        "functions": [u"func_aws_guardduty_archive_finding", u"func_aws_guardduty_refresh_finding"],
        "workflows": [u"wf_aws_guardduty_refresh_finding", u"wf_aws_guardduty_archive_finding"],
        "actions": [u"Example: AWS GuardDuty: Refresh Finding", u"Example: AWS GuardDuty: Archive Finding"],
        "incident_fields": [u"aws_guardduty_finding_type", u"aws_guardduty_finding_updated_at", u"aws_guardduty_finding_id", u"aws_guardduty_detector_id", u"aws_guardduty_archived", u"aws_guardduty_resource_type", u"aws_guardduty_count", u"aws_guardduty_finding_arn", u"aws_guardduty_region"],
        "incident_artifact_types": [u"aws_iam_access_key_id", u"aws_iam_user_name"],
        "datatables": [u"gd_action_details", u"gd_resource_affected"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 38.1.4

    Contents:
    - Message Destinations:
        - fn_aws_gd
    - Functions:
        - func_aws_guardduty_archive_finding
        - func_aws_guardduty_refresh_finding
    - Workflows:
        - wf_aws_guardduty_refresh_finding
        - wf_aws_guardduty_archive_finding
    - Rules:
        - Example: AWS GuardDuty: Refresh Finding
        - Example: AWS GuardDuty: Archive Finding
    - Incident Fields:
        - aws_guardduty_finding_type
        - aws_guardduty_finding_updated_at
        - aws_guardduty_finding_id
        - aws_guardduty_detector_id
        - aws_guardduty_archived
        - aws_guardduty_resource_type
        - aws_guardduty_count
        - aws_guardduty_finding_arn
        - aws_guardduty_region
    - Custom Artifact Types:
        - aws_iam_access_key_id
        - aws_iam_user_name
    - Data Tables:
        - gd_action_details
        - gd_resource_affected
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)