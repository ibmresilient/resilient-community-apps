# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_aws_guardduty"""

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
        "message_destinations": [
            u"fn_aws_gd"
        ],
        "functions": [
            u"func_aws_guardduty_archive_finding",
            u"func_aws_guardduty_refresh_finding"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"aws_guardduty_archived",
            u"aws_guardduty_count",
            u"aws_guardduty_detector_id",
            u"aws_guardduty_finding_arn",
            u"aws_guardduty_finding_id",
            u"aws_guardduty_finding_type",
            u"aws_guardduty_finding_updated_at",
            u"aws_guardduty_region",
            u"aws_guardduty_resource_type",
            u"aws_guardduty_severity",
            u"aws_guardduty_trigger_refresh"
        ],
        "incident_artifact_types": [
            u"aws_iam_access_key_id",
            u"aws_iam_user_name",
            u"aws_s3_bucket_name"
        ],
        "incident_types": [],
        "datatables": [
            u"gd_access_key_details",
            u"gd_action_details",
            u"gd_finding_overview",
            u"gd_instance_details",
            u"gd_resource_affected",
            u"gd_s3_bucket_details"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"example_aws_guardduty_archive_finding_pb",
            u"example_aws_guardduty_refresh_finding_details_pb",
            u"example_aws_guardduty_update_finding_details_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_aws_gd
    - Functions:
        - func_aws_guardduty_archive_finding
        - func_aws_guardduty_refresh_finding
    - Playbooks:
        - example_aws_guardduty_archive_finding_pb
        - example_aws_guardduty_refresh_finding_details_pb
        - example_aws_guardduty_update_finding_details_pb
    - Incident Fields:
        - aws_guardduty_archived
        - aws_guardduty_count
        - aws_guardduty_detector_id
        - aws_guardduty_finding_arn
        - aws_guardduty_finding_id
        - aws_guardduty_finding_type
        - aws_guardduty_finding_updated_at
        - aws_guardduty_region
        - aws_guardduty_resource_type
        - aws_guardduty_severity
        - aws_guardduty_trigger_refresh
    - Custom Artifact Types:
        - aws_iam_access_key_id
        - aws_iam_user_name
        - aws_s3_bucket_name
    - Data Tables:
        - gd_access_key_details
        - gd_action_details
        - gd_finding_overview
        - gd_instance_details
        - gd_resource_affected
        - gd_s3_bucket_details
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)