# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""
File contains constants used in the integration.
"""
# Map GuardDuty findings fields to Resilient incidendt custom fields.
CUSTOM_FIELDS_MAP = {
    "Id": "aws_guardduty_finding_id",
    "Arn": "aws_guardduty_finding_arn",
    "Type": "aws_guardduty_finding_type",
    "UpdatedAt": "aws_guardduty_finding_updated_at",
    "Region": "aws_guardduty_region",
    "Resource": {
        "ResourceType": "aws_guardduty_resource_type"
    },
    "Service": {
        "Count": "aws_guardduty_count",
        "DetectorId": "aws_guardduty_detector_id"
    }
}
