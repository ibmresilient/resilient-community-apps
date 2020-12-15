# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""
File contains constants used in the integration.
"""
# Map GuardDuty findings fields to Resilient incident custom fields.
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
# Map Resilient artifact types to GuardDuty properties.
ARTIFACT_TYPES_MAP = {
    "AWS IAM Access Key ID": ["AccessKeyId"],
    "AWS IAM User Name": ["UserName"],
    "IP Address": ["IpAddressV4", "PrivateIpAddress", "PublicIp"],
    "DNS Name": ["PublicDnsName", "PrivateDnsName"],
    "Port": ["Port"]
}
# Resilient artifact names to api names.
ARTIFACT_TYPE_API_NAME = {
    "AWS IAM Access Key ID": "aws_iam_access_key_id",
    "AWS IAM User Name": "aws_iam_user_name",
    "IP Address": "IP Address",
    "DNS Name": "DNS Name",
    "Port": "Port"
}