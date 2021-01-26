# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
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
    "ResourceType": {"aws_guardduty_resource_type": {"path": "Resource"}},
    "DetectorId": {"aws_guardduty_detector_id": {"path": "Service"}},
    "Count": {"aws_guardduty_count": {"path": "Service"}},
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
# API Name(s) of Data Table(s)
DATA_TABLE_IDS = [
    "gd_action_details",
    "gd_resource_affected"
]
# Map of GuardDuty fields to data table columns,
DATA_TABLE_FIELDS_MAP = {
    "gd_action_details": [
        {
            "path": ["Service"],
            "fields": {
                "ActionType": "action_type",
                "Api": "action_api",
                "Protocol": "protocol",
                "EventFirstSeen": "event_first_seen",
                "EventLastSeen": "event_last_seen",
                "CallerType": "actor_caller_type",
                "CityName": "city_name",
                "CountryName": "country_name",
                "Asn": "asn",
                "AsnOrg": "asn_org" ,
                "Isp": "isp",
                "Org": "org"
            }
        },
        {
            "path": ["Service", "Action", "DnsRequestAction"],
            "fields": {
                "Domain": "dns_domain_name",
                "Blocked": "dns_blocked"
            }
        },
        {
            "path": ["Service", "Action", "*Action"],
            "fields": {
                "ServiceName": "action_service_name",
            }
        },
        {
            "path": ["Service", "Action", "*Action", "LocalIpDetails"],
            "fields": {
                "IpAddressV4": "local_ip",
            }
        },
        {
            "path": ["Service", "Action", "*Action", "RemoteIpDetails"],
            "fields": {
                "IpAddressV4": "remote_ip",
            }
        },
        {
            "path": ["Service", "Action", "*Action", "RemotePortDetails"],
            "fields": {
                "Port": "remote_port",
            }
        },
        {
            "path": ["Service", "Action", "*Action", "LocalPortDetails"],
            "fields": {
                "Port": "local_port",
            }
        }
    ],
    "gd_resource_affected": [
        {
            "path": ["Resource"],
            "fields": {
                "ResourceType": "resource_type",
            }
        },
        {
            "path": ["Resource", "InstanceDetails"],
            "fields": {
                "InstanceId": "instance_id",
                "InstanceType": "instance_type",
                "InstanceState": "instance_state"
            }
        },
        {
            "path": ["Service"],
            "fields": {
                "ResourceRole": "resource_role",
            }
        },
        {
            "path": ["Resource", "InstanceDetails", "NetworkInterfaces", 0],
            "fields": {
                "PrivateIpAddress": "instance_private_ip",
                "PrivateDnsName": "instance_private_dns",
                "PublicIp": "instance_public_ip",
                "PublicDnsName": "instance_public_dns",
            }
        },
        {
            "path": ["Resource", "S3BucketDetails", 0],
            "fields": {
                "Name": "s3bucket_name",
            }
        },
        {
            "path": ["Resource", "S3BucketDetails", 0, "Owner"],
            "fields": {
                "Id": "s3bucket_owner",
            }
        },
    ]
}
