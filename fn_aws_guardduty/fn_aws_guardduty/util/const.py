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
    "Severity": "aws_guardduty_severity",
    "ResourceType": {"aws_guardduty_resource_type": {"path": "Resource"}},
    "DetectorId": {"aws_guardduty_detector_id": {"path": "Service"}},
    "Count": {"aws_guardduty_count": {"path": "Service"}},
    "Archived": {"aws_guardduty_archived": {"path": "Service"}}
}
# Map Resilient artifact types to GuardDuty properties.
ARTIFACT_TYPES_MAP = {
    "AWS IAM Access Key ID": ["AccessKeyId"],
    "AWS IAM User Name": ["UserName"],
    "AWS S3 Bucket Name": {"gd_props": ["Name"], "path": ["Resource", "S3BucketDetails"]},
    "IP Address": ["IpAddressV4", "PrivateIpAddress", "PublicIp"],
    "DNS Name": ["PublicDnsName", "PrivateDnsName"],
    "Port": ["Port"]
}
# Resilient artifact names to api names.
ARTIFACT_TYPE_API_NAME = {
    "AWS IAM Access Key ID": "aws_iam_access_key_id",
    "AWS IAM User Name": "aws_iam_user_name",
    "AWS S3 Bucket Name": "aws_s3_bucket_name",
    "IP Address": "IP Address",
    "DNS Name": "DNS Name",
    "Port": "Port"
}
# API Name(s) of Data Table(s)
DATA_TABLE_IDS = [
    "gd_finding_overview",
    "gd_action_details",
    "gd_resource_affected",
    "gd_s3_bucket_details",
    "gd_instance_details",
    "gd_access_key_details"
]
# Map of GuardDuty fields to data table columns,
DATA_TABLE_FIELDS_MAP = {
    "gd_finding_overview": [
        {
            "path": [],
            "fields": {
                "Severity": "severity",
                "Region": "region",
                "Count": "count",
                "AccountId": "account_id",
                "ResourceId": "resource_id",
                "CreatedAt": "created_at",
                "UpdatedAt": "updated_at",
            }
        },
        # Default to Instance Id as resource_id.
        {
            "path": ["Resource", "InstanceDetails"],
            "fields": {
                "InstanceId": "resource_id",
            }
        },
        # If bucketname exists will use 1at instance as resource_id instead.
        {
            "path": ["Resource", "S3BucketDetails", 0],
            "fields": {
                "Name": "resource_id",
            }
        },
    ],
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
            "path": ["Service", "Action", "*Action"],
            "fields": {
                "ServiceName": "service_name",
            }
        },
        {
            "path": ["Service", "Action", "*Action"],
            "fields": {
                "ConnectionDirection": "connection_direction",
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
            "path": ["Service"],
            "fields": {
                "ResourceRole": "resource_role",
            }
        },
        {
            "path": ["Resource", "InstanceDetails"],
            "fields": {
                "InstanceId": "instance_id",
                "InstanceType": "instance_type",
            }
        },
    ],
    "gd_s3_bucket_details": [
        {
            "path": ["Resource", "S3BucketDetails", []],
            "fields": {
                "Name": "bucket_name",
                "Type": "bucket_type",
                "Arn": "bucket_arn",
                "Id": "bucket_owner",
                "KmsMasterKeyArn": "kms_master_key_arn",
                "EncryptionType":  "encryption_type",
                "EffectivePermission": "effective_permissions"
            }
        },
    ],
    "gd_instance_details": [
        {
            "path": ["Resource", "InstanceDetails"],
            "fields": {
                "InstanceId": "instance_id",
                "InstanceType": "type",
                "InstanceState": "instance_state"
            }
        },
        {
            "path": ["Resource", "InstanceDetails", "NetworkInterfaces", 0],
            "fields": {
                "PrivateIpAddress": "private_ip",
                "PrivateDnsName": "private_dns_name",
                "PublicIp": "public_ip",
                "PublicDnsName": "public_dns_name",
            }
        }
    ],
    "gd_access_key_details": [
        {
            "path": ["Resource", "AccessKeyDetails"],
            "fields": {
                "AccessKeyId": "access_key_id",
                "PrincipalId": "principal_id",
                "UserType": "user_type",
                "UserName": "user_name"
            }
        }
    ],
}
