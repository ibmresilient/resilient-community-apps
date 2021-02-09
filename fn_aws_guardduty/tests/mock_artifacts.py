# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate AWS IAM for Unit and function tests """

import datetime
from dateutil.tz import tzlocal

def get_mock_config():
    config_data = u"""[fn_aws_guardduty]
aws_gd_access_key_id=<AWS_GUARDDUTY_ACCESS_KEY_ID>
aws_gd_secret_access_key=<AWS_GUARDDUTY_SECRET_ACCESS_KEY>
# Default or master region for the integration
aws_gd_master_region=us-west-2
# Filter by GuardDuty region names. Can be a string or regular expression.
# e.g. aws_gd_regions=^(us|eu).* to get Europe and US regions.
aws_gd_regions=.*
# Interval to refresh regions information (in minutes).
aws_gd_regions_interval=60
# Interval to poll Guardduty (in minutes).
aws_gd_polling_interval=0
# Optional - severity threshold (int) to use in criterion to filter findings 
# results. (default 7).
# Severity ranges: 7.0 - 8.9 -> High, 4.0 - 6.9 -> Medium, 1.0 = 3.9 -> Low
aws_gd_severity_threshold = 7
# Optional - Lookback interval in minutes to check if findings updated
# since last run. Used in criteria for filtering findings retrieval (default 60).
aws_gd_lookback_interval=60
# Optional settings for access to GuardDuty via a proxy.
#http_proxy=http://proxy:80
#https_proxy=http://proxy:80
"""
    return config_data

# Mocked IAM RAW Responses for standalone tests.
def get_cli_raw_responses(op):
    response = {
        "describe_regions": (
            {'Regions': [{'Endpoint': 'ec2.eu-north-1.amazonaws.com', 'RegionName': 'eu-north-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.ap-south-1.amazonaws.com', 'RegionName': 'ap-south-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.eu-west-3.amazonaws.com', 'RegionName': 'eu-west-3',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.eu-west-2.amazonaws.com', 'RegionName': 'eu-west-2',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.eu-west-1.amazonaws.com', 'RegionName': 'eu-west-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.ap-northeast-2.amazonaws.com', 'RegionName': 'ap-northeast-2',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.ap-northeast-1.amazonaws.com', 'RegionName': 'ap-northeast-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.sa-east-1.amazonaws.com', 'RegionName': 'sa-east-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.ca-central-1.amazonaws.com', 'RegionName': 'ca-central-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.ap-southeast-1.amazonaws.com', 'RegionName': 'ap-southeast-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.ap-southeast-2.amazonaws.com', 'RegionName': 'ap-southeast-2',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.eu-central-1.amazonaws.com', 'RegionName': 'eu-central-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.us-east-1.amazonaws.com', 'RegionName': 'us-east-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.us-east-2.amazonaws.com', 'RegionName': 'us-east-2',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.us-west-1.amazonaws.com', 'RegionName': 'us-west-1',
                          'OptInStatus': 'opt-in-not-required'},
                         {'Endpoint': 'ec2.us-west-2.amazonaws.com', 'RegionName': 'us-west-2',
                          'OptInStatus': 'opt-in-not-required'}],
             'ResponseMetadata': {'RequestId': '3f790a11-b512-4ce5-88b5-3990ffb17ddd', 'HTTPStatusCode': 200,
                                  'HTTPHeaders': {'x-amzn-requestid': '3f790a11-b512-4ce5-88b5-3990ffb17ddd',
                                                  'cache-control': 'no-cache, no-store',
                                                  'strict-transport-security': 'max-age=31536000; includeSubDomains',
                                                  'content-type': 'text/xml;charset=UTF-8', 'content-length': '3655',
                                                  'vary': 'accept-encoding', 'date': 'Tue, 05 Jan 2021 12:23:16 GMT',
                                                  'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
        ),
        "list_detectors":(
            {'ResponseMetadata': {'RequestId': '80ff249e-b880-420e-a6b9-0dea2621538c', 'HTTPStatusCode': 200,
                                  'HTTPHeaders': {'date': 'Tue, 05 Jan 2021 12:38:42 GMT',
                                                  'content-type': 'application/json', 'content-length': '52',
                                                  'connection': 'keep-alive',
                                                  'x-amzn-requestid': '80ff249e-b880-420e-a6b9-0dea2621538c',
                                                  'x-amz-apigw-id': 'YrOY1ELbvHcFkgw=',
                                                  'x-amzn-trace-id': 'Root=1-5ff45dd2-121d57220a7661b070273cf3;Sampled=0'},
                                  'RetryAttempts': 0}, 'DetectorIds': ['f2baedb0ac74f8f42fc929e15f56da6a']}
        ),
        "list_findings": (
            {'ResponseMetadata': {'RequestId': '5ac15376-acfc-4cfc-92df-99a800abcef4', 'HTTPStatusCode': 200,
                                  'HTTPHeaders': {'date': 'Tue, 05 Jan 2021 12:39:39 GMT',
                                                  'content-type': 'application/json', 'content-length': '1827',
                                                  'connection': 'keep-alive',
                                                  'x-amzn-requestid': '5ac15376-acfc-4cfc-92df-99a800abcef4',
                                                  'x-amz-apigw-id': 'YrOhyEPQPHcFXXA=',
                                                  'x-amzn-trace-id': 'Root=1-5ff45e0b-4fe3b87818161b715dcf6423;Sampled=0'},
                                  'RetryAttempts': 0},
             'FindingIds': ['60baffd3f9042e38640f2300d5c5a631', 'b8baffd3f90472ebf26adce5cea33685',
                            '18baffd3f9039ba840cdf3ad226e36f7', '46baffd3f9047da341ecae8fe62222f1',
                            '58baffd3f903af9ee55660d3641e94d0', '86baffd3f9043322d9b01e914bf3ed06',
                            'ecbaffd3f90450f165ef8c16dc6761fa', '32baffd3f90387cc1097fdf9a63469d7',
                            '36baffd3f903e6ef24171ab379d6f2e5', '3ebaffd3f903e855c376579fadac3ab5',
                            '44baee3076b87eb8dc8f9cf466ad7be6', '84baffd3f903f16f015f27f8c5538971',
                            'aebaffd3f90321416f8dc65e7a33432d', 'd6baffd3f9030f1ee7e94aaf9b24dd0f',
                            'f0baffd3f90304127334a900af6b2ec0', 'f2baffd3f903a8b8f3b790876c898dd7',
                            '1cbaffd3f903727580993b3463f58d54', '26baffd3f9028d65d75617c853bbbde3',
                            '4cbaffd3f9032a2afb8f978410910037', '52baffd3f902c25f8bfe50fd3c24e65e',
                            '9cbaffd3f902cb9f1c0d72b159da54a9', 'a0baffd3f90359ef7dabf6e909ac4de5',
                            'b0baffd3f9035d4b2bf7f2f0ef9640f8', 'b4baffd3f903725f70a2ca050d4d069e',
                            'bebaffd3f903497caebd68453183fe6d', 'ccbaffd3f90334ead7c11d7c272e2f62',
                            'eabaffd3f90321c72661e4a6fd2c3a5f', '26baffd3f90271f68a72fd9b4dd70781',
                            '46baffd3f902c428bc63ecfa58b8fcca', '96baffd3f9029e01c233b528fa69beaf',
                            'aabaffd3f902de9df72d792845053730', '5cbaffd3f902047f93b465380729a395',
                            'c6baffd3f9023c12725d124dccc067f2', 'f8baffd3f9020ae11f6865ecd70e0f3b',
                            '4ebaffd3f901acd98e67760e8f59e276', '7abaffd3f901b30ed065c0e1b3ecedf6',
                            'c2baffd3f901f11dd8497af9e33514da', '6abaffd3f900b4dc806783697914ec74',
                            'c6baffd3f9015cef6d96bf4180d4d628', 'f0baffd3f9016aa774371b376f5c9453',
                            'f4baffd3f900aac88ce9932ee235c8e5', 'febaffd3f9017e10f9bfefb50f1a5567',
                            '0abaffd3f9001c147f1d263373f0befd', '14baffd3f900d3d455e790bb312fd897',
                            '58baffd3f90035ff28700f6ed4bd897f', 'b8baffd3f900972453b724a4147cba6f',
                            'e4baffd3f900ab39aace4e4e33237282', 'ecbaffd3f90098b4f377f05bf55aa3d1',
                            '10baffd3f9001e735506ba027e50f6a2', '3ebaffd3f90067948f21e00a686a41c2'],
             'NextToken': '1606403892611-3ebaffd3f90067948f21e00a686a41c2'}
        ),
        "get_findings": (
            {'ResponseMetadata': {'RequestId': 'bad216aa-23fc-41d5-9c3e-bf0aa6188aa9', 'HTTPStatusCode': 200,
                                  'HTTPHeaders': {'date': 'Tue, 05 Jan 2021 12:32:38 GMT',
                                                  'content-type': 'application/json', 'content-length': '4443',
                                                  'connection': 'keep-alive',
                                                  'x-amzn-requestid': 'bad216aa-23fc-41d5-9c3e-bf0aa6188aa9',
                                                  'x-amz-apigw-id': 'YrNf_FTZvHcFbDw=',
                                                  'x-amzn-trace-id': 'Root=1-5ff45c66-7ce841230ba9c7ca49bc09dd;Sampled=0'},
                                  'RetryAttempts': 0}, 'Findings': [{'AccountId': '834299573936',
                                                                     'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                                                                     'CreatedAt': '2020-11-25T13:46:37.960Z',
                                                                     'Description': 'An API was used to access a bucket from an IP address on a custom threat list.',
                                                                     'Id': '60baffd3f9042e38640f2300d5c5a631',
                                                                     'Partition': 'aws', 'Region': 'us-west-2',
                                                                     'Resource': {'AccessKeyDetails': {
                                                                         'AccessKeyId': 'GeneratedFindingAccessKeyId',
                                                                         'PrincipalId': 'GeneratedFindingPrincipalId',
                                                                         'UserName': 'GeneratedFindingUserName',
                                                                         'UserType': 'IAMUser'}, 'S3BucketDetails': [
                                                                         {'Arn': 'arn:aws:s3:::bucketName',
                                                                          'Name': 'bucketName', 'Type': 'Destination',
                                                                          'CreatedAt': datetime.datetime(2017, 12, 18,
                                                                                                         15, 58, 11,
                                                                                                         551000,
                                                                                                         tzinfo=tzlocal()),
                                                                          'Owner': {'Id': 'CanonicalId of Owner'},
                                                                          'Tags': [{'Key': 'foo', 'Value': 'bar'}],
                                                                          'DefaultServerSideEncryption': {
                                                                              'EncryptionType': 'SSEAlgorithm',
                                                                              'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},
                                                                          'PublicAccess': {'PermissionConfiguration': {
                                                                              'BucketLevelPermissions': {
                                                                                  'AccessControlList': {
                                                                                      'AllowsPublicReadAccess': False,
                                                                                      'AllowsPublicWriteAccess': False},
                                                                                  'BucketPolicy': {
                                                                                      'AllowsPublicReadAccess': False,
                                                                                      'AllowsPublicWriteAccess': False},
                                                                                  'BlockPublicAccess': {
                                                                                      'IgnorePublicAcls': False,
                                                                                      'RestrictPublicBuckets': False,
                                                                                      'BlockPublicAcls': False,
                                                                                      'BlockPublicPolicy': False}},
                                                                              'AccountLevelPermissions': {
                                                                                  'BlockPublicAccess': {
                                                                                      'IgnorePublicAcls': False,
                                                                                      'RestrictPublicBuckets': False,
                                                                                      'BlockPublicAcls': False,
                                                                                      'BlockPublicPolicy': False}}},
                                                                                           'EffectivePermission': 'NOT_PUBLIC'}}],
                                                                                  'InstanceDetails': {
                                                                                      'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',
                                                                                      'IamInstanceProfile': {
                                                                                          'Arn': 'arn:aws:iam::834299573936:example/instance/profile',
                                                                                          'Id': 'GeneratedFindingInstanceProfileId'},
                                                                                      'ImageDescription': 'GeneratedFindingInstaceImageDescription',
                                                                                      'ImageId': 'ami-99999999',
                                                                                      'InstanceId': 'i-99999999',
                                                                                      'InstanceState': 'running',
                                                                                      'InstanceType': 'm3.xlarge',
                                                                                      'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',
                                                                                      'LaunchTime': '2016-08-02T02:05:06Z',
                                                                                      'NetworkInterfaces': [
                                                                                          {'Ipv6Addresses': [],
                                                                                           'NetworkInterfaceId': 'eni-bfcffe88',
                                                                                           'PrivateDnsName': 'GeneratedFindingPrivateDnsName',
                                                                                           'PrivateIpAddress': '10.0.0.1',
                                                                                           'PrivateIpAddresses': [{
                                                                                                                      'PrivateDnsName': 'GeneratedFindingPrivateName',
                                                                                                                      'PrivateIpAddress': '10.0.0.1'}],
                                                                                           'PublicDnsName': 'GeneratedFindingPublicDNSName',
                                                                                           'PublicIp': '198.51.100.0',
                                                                                           'SecurityGroups': [{
                                                                                                                  'GroupId': 'GeneratedFindingSecurityId',
                                                                                                                  'GroupName': 'GeneratedFindingSecurityGroupName'}],
                                                                                           'SubnetId': 'GeneratedFindingSubnetId',
                                                                                           'VpcId': 'GeneratedFindingVPCId'}],
                                                                                      'ProductCodes': [{}], 'Tags': [{
                                                                                                                         'Key': 'GeneratedFindingInstaceTag1',
                                                                                                                         'Value': 'GeneratedFindingInstaceValue1'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag2',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue2'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag3',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue3'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag4',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue4'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag5',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue5'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag6',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue6'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag7',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue7'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag8',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue8'},
                                                                                                                     {
                                                                                                                         'Key': 'GeneratedFindingInstaceTag9',
                                                                                                                         'Value': 'GeneratedFindingInstaceTagValue9'}]},
                                                                                  'ResourceType': 'S3Bucket'},
                                                                     'SchemaVersion': '2.0', 'Service': {
                    'Action': {'ActionType': 'AWS_API_CALL',
                               'AwsApiCallAction': {'Api': 'GeneratedFindingAPIName', 'CallerType': 'Remote IP',
                                                    'RemoteIpDetails': {
                                                        'City': {'CityName': 'GeneratedFindingCityName'},
                                                        'Country': {'CountryName': 'GeneratedFindingCountryName'},
                                                        'GeoLocation': {'Lat': 0, 'Lon': 0},
                                                        'IpAddressV4': '198.51.100.0', 'Organization': {'Asn': '-1',
                                                                                                        'AsnOrg': 'GeneratedFindingASNOrg',
                                                                                                        'Isp': 'GeneratedFindingISP',
                                                                                                        'Org': 'GeneratedFindingORG'}},
                                                    'ServiceName': 'GeneratedFindingAPIServiceName'}},
                    'Archived': False, 'Count': 4, 'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',
                    'EventFirstSeen': '2020-11-25T13:46:37.960Z', 'EventLastSeen': '2020-11-26T15:18:12.620Z',
                    'ResourceRole': 'TARGET', 'ServiceName': 'guardduty'}, 'Severity': 2,
                                                                     'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                                                                     'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                                                                     'UpdatedAt': '2020-11-26T15:18:12.620Z'}]}
        ),
        "archive_findings": (
            {'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200,
                                  'RequestId': 'af84ee9f-7267-478e-ade9-4ec1ce50b66c',
                                  'HTTPHeaders': {'x-amzn-requestid': 'af84ee9f-7267-478e-ade9-4ec1ce50b66c',
                                                  'content-length': '0', 'x-amz-apigw-id': 'Z6P_6ET5iYcFlXg=',
                                                  'x-amzn-trace-id': 'Root=1-6013f9ff-7991c29e4458ff242c99d482;Sampled=0',
                                                  'connection': 'keep-alive', 'date': 'Fri, 29 Jan 2021 12:05:19 GMT',
                                                  'content-type': 'application/json'}}}
        )
    }
    return response[op]


## Mock results.
def get_mocked_results(type):
    response = {
        "finding_payload_with_artifacts": (
            {
                'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                'description': {'format': 'text',
                                'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
                'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
                'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                               'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                               'aws_guardduty_region': 'us-west-2', 'aws_guardduty_resource_type': 'S3Bucket',
                               'aws_guardduty_count': '4',
                               'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a'},
                'artifacts': [],
                'comments': [{'text': {'format': 'text',
                                       'content': "AWS GuardDuty finding Payload:\n{   'AccountId': '834299573936',\n    'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',\n    'CreatedAt': '2020-11-25T13:46:37.960Z',\n    'Description': 'An API was used to access a bucket from an IP address on a '\n                   'custom threat list.',\n    'Id': '60baffd3f9042e38640f2300d5c5a631',\n    'Partition': 'aws',\n    'Region': 'us-west-2',\n    'Resource': {   'AccessKeyDetails': {   'AccessKeyId': 'GeneratedFindingAccessKeyId',\n                                            'PrincipalId': 'GeneratedFindingPrincipalId',\n                                            'UserName': 'GeneratedFindingUserName',\n                                            'UserType': 'IAMUser'},\n                    'InstanceDetails': {   'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',\n                                           'IamInstanceProfile': {   'Arn': 'arn:aws:iam::834299573936:example/instance/profile',\n                                                                     'Id': 'GeneratedFindingInstanceProfileId'},\n                                           'ImageDescription': 'GeneratedFindingInstaceImageDescription',\n                                           'ImageId': 'ami-99999999',\n                                           'InstanceId': 'i-99999999',\n                                           'InstanceState': 'running',\n                                           'InstanceType': 'm3.xlarge',\n                                           'LaunchTime': '2016-08-02T02:05:06Z',\n                                           'NetworkInterfaces': [   {   'Ipv6Addresses': [   ],\n                                                                        'NetworkInterfaceId': 'eni-bfcffe88',\n                                                                        'PrivateDnsName': 'GeneratedFindingPrivateDnsName',\n                                                                        'PrivateIpAddress': '10.0.0.1',\n                                                                        'PrivateIpAddresses': [   {   'PrivateDnsName': 'GeneratedFindingPrivateName',\n                                                                                                      'PrivateIpAddress': '10.0.0.1'}],\n                                                                        'PublicDnsName': 'GeneratedFindingPublicDNSName',\n                                                                        'PublicIp': '198.51.100.0',\n                                                                        'SecurityGroups': [   {   'GroupId': 'GeneratedFindingSecurityId',\n                                                                                                  'GroupName': 'GeneratedFindingSecurityGroupName'}],\n                                                                        'SubnetId': 'GeneratedFindingSubnetId',\n                                                                        'VpcId': 'GeneratedFindingVPCId'}],\n                                           'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',\n                                           'ProductCodes': [{}],\n                                           'Tags': [   {   'Key': 'GeneratedFindingInstaceTag1',\n                                                           'Value': 'GeneratedFindingInstaceValue1'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag2',\n                                                           'Value': 'GeneratedFindingInstaceTagValue2'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag3',\n                                                           'Value': 'GeneratedFindingInstaceTagValue3'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag4',\n                                                           'Value': 'GeneratedFindingInstaceTagValue4'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag5',\n                                                           'Value': 'GeneratedFindingInstaceTagValue5'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag6',\n                                                           'Value': 'GeneratedFindingInstaceTagValue6'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag7',\n                                                           'Value': 'GeneratedFindingInstaceTagValue7'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag8',\n                                                           'Value': 'GeneratedFindingInstaceTagValue8'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag9',\n                                                           'Value': 'GeneratedFindingInstaceTagValue9'}]},\n                    'ResourceType': 'S3Bucket',\n                    'S3BucketDetails': [   {   'Arn': 'arn:aws:s3:::bucketName',\n                                               'CreatedAt': '2017-12-18 '\n                                                            '15:58:11',\n                                               'DefaultServerSideEncryption': {   'EncryptionType': 'SSEAlgorithm',\n                                                                                  'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},\n                                               'Name': 'bucketName',\n                                               'Owner': {   'Id': 'CanonicalId '\n                                                                  'of Owner'},\n                                               'PublicAccess': {   'EffectivePermission': 'NOT_PUBLIC',\n                                                                   'PermissionConfiguration': {   'AccountLevelPermissions': {   'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                          'BlockPublicPolicy': False,\n                                                                                                                                                          'IgnorePublicAcls': False,\n                                                                                                                                                          'RestrictPublicBuckets': False}},\n                                                                                                  'BucketLevelPermissions': {   'AccessControlList': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                         'AllowsPublicWriteAccess': False},\n                                                                                                                                'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                         'BlockPublicPolicy': False,\n                                                                                                                                                         'IgnorePublicAcls': False,\n                                                                                                                                                         'RestrictPublicBuckets': False},\n                                                                                                                                'BucketPolicy': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                    'AllowsPublicWriteAccess': False}}}},\n                                               'Tags': [   {   'Key': 'foo',\n                                                               'Value': 'bar'}],\n                                               'Type': 'Destination'}]},\n    'SchemaVersion': '2.0',\n    'Service': {   'Action': {   'ActionType': 'AWS_API_CALL',\n                                 'AwsApiCallAction': {   'Api': 'GeneratedFindingAPIName',\n                                                         'CallerType': 'Remote '\n                                                                       'IP',\n                                                         'RemoteIpDetails': {   'City': {   'CityName': 'GeneratedFindingCityName'},\n                                                                                'Country': {   'CountryName': 'GeneratedFindingCountryName'},\n                                                                                'GeoLocation': {   'Lat': 0,\n                                                                                                   'Lon': 0},\n                                                                                'IpAddressV4': '198.51.100.0',\n                                                                                'Organization': {   'Asn': '-1',\n                                                                                                    'AsnOrg': 'GeneratedFindingASNOrg',\n                                                                                                    'Isp': 'GeneratedFindingISP',\n                                                                                                    'Org': 'GeneratedFindingORG'}},\n                                                         'ServiceName': 'GeneratedFindingAPIServiceName'}},\n                   'Archived': False,\n                   'Count': 4,\n                   'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',\n                   'EventFirstSeen': '2020-11-25T13:46:37.960Z',\n                   'EventLastSeen': '2020-11-26T15:18:12.620Z',\n                   'ResourceRole': 'TARGET',\n                   'ServiceName': 'guardduty'},\n    'Severity': 2,\n    'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a '\n             'custom threat list.',\n    'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',\n    'UpdatedAt': '2020-11-26T15:18:12.620Z'}"}}]}        ),
        "finding_payload_no_artifacts":(
            {
                'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                'description': {'format': 'text',
                                'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
                'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
                'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                               'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                               'aws_guardduty_region': 'us-west-2', 'aws_guardduty_resource_type': 'S3Bucket',
                               'aws_guardduty_count': '4',
                               'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a'}, 'artifacts': [
                {'type': {'name': 'aws_iam_access_key_id'}, 'description': {'format': 'text',
                                                                            'content': "'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'."},
                 'value': 'GeneratedFindingAccessKeyId'}, {'type': {'name': 'aws_iam_user_name'},
                                                           'description': {'format': 'text',
                                                                           'content': "'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'."},
                                                           'value': 'GeneratedFindingUserName'},
                {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                 'content': "'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'."},
                 'value': '198.51.100.0'}, {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                                            'content': "'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                            'value': '10.0.0.1'}, {'type': {'name': 'DNS Name'},
                                                                   'description': {'format': 'text',
                                                                                   'content': "'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                                   'value': 'GeneratedFindingPublicDNSName'},
                {'type': {'name': 'DNS Name'}, 'description': {'format': 'text',
                                                               'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                 'value': 'GeneratedFindingPrivateDnsName'}, {'type': {'name': 'DNS Name'},
                                                              'description': {'format': 'text',
                                                                              'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'."},
                                                              'value': 'GeneratedFindingPrivateName'}], 'comments': [{
                                                                                                                         'text': {
                                                                                                                             'format': 'text',
                                                                                                                             'content': "AWS GuardDuty finding Payload:\n{   'AccountId': '834299573936',\n    'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',\n    'CreatedAt': '2020-11-25T13:46:37.960Z',\n    'Description': 'An API was used to access a bucket from an IP address on a '\n                   'custom threat list.',\n    'Id': '60baffd3f9042e38640f2300d5c5a631',\n    'Partition': 'aws',\n    'Region': 'us-west-2',\n    'Resource': {   'AccessKeyDetails': {   'AccessKeyId': 'GeneratedFindingAccessKeyId',\n                                            'PrincipalId': 'GeneratedFindingPrincipalId',\n                                            'UserName': 'GeneratedFindingUserName',\n                                            'UserType': 'IAMUser'},\n                    'InstanceDetails': {   'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',\n                                           'IamInstanceProfile': {   'Arn': 'arn:aws:iam::834299573936:example/instance/profile',\n                                                                     'Id': 'GeneratedFindingInstanceProfileId'},\n                                           'ImageDescription': 'GeneratedFindingInstaceImageDescription',\n                                           'ImageId': 'ami-99999999',\n                                           'InstanceId': 'i-99999999',\n                                           'InstanceState': 'running',\n                                           'InstanceType': 'm3.xlarge',\n                                           'LaunchTime': '2016-08-02T02:05:06Z',\n                                           'NetworkInterfaces': [   {   'Ipv6Addresses': [   ],\n                                                                        'NetworkInterfaceId': 'eni-bfcffe88',\n                                                                        'PrivateDnsName': 'GeneratedFindingPrivateDnsName',\n                                                                        'PrivateIpAddress': '10.0.0.1',\n                                                                        'PrivateIpAddresses': [   {   'PrivateDnsName': 'GeneratedFindingPrivateName',\n                                                                                                      'PrivateIpAddress': '10.0.0.1'}],\n                                                                        'PublicDnsName': 'GeneratedFindingPublicDNSName',\n                                                                        'PublicIp': '198.51.100.0',\n                                                                        'SecurityGroups': [   {   'GroupId': 'GeneratedFindingSecurityId',\n                                                                                                  'GroupName': 'GeneratedFindingSecurityGroupName'}],\n                                                                        'SubnetId': 'GeneratedFindingSubnetId',\n                                                                        'VpcId': 'GeneratedFindingVPCId'}],\n                                           'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',\n                                           'ProductCodes': [{}],\n                                           'Tags': [   {   'Key': 'GeneratedFindingInstaceTag1',\n                                                           'Value': 'GeneratedFindingInstaceValue1'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag2',\n                                                           'Value': 'GeneratedFindingInstaceTagValue2'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag3',\n                                                           'Value': 'GeneratedFindingInstaceTagValue3'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag4',\n                                                           'Value': 'GeneratedFindingInstaceTagValue4'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag5',\n                                                           'Value': 'GeneratedFindingInstaceTagValue5'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag6',\n                                                           'Value': 'GeneratedFindingInstaceTagValue6'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag7',\n                                                           'Value': 'GeneratedFindingInstaceTagValue7'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag8',\n                                                           'Value': 'GeneratedFindingInstaceTagValue8'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag9',\n                                                           'Value': 'GeneratedFindingInstaceTagValue9'}]},\n                    'ResourceType': 'S3Bucket',\n                    'S3BucketDetails': [   {   'Arn': 'arn:aws:s3:::bucketName',\n                                               'CreatedAt': '2017-12-18 '\n                                                            '15:58:11',\n                                               'DefaultServerSideEncryption': {   'EncryptionType': 'SSEAlgorithm',\n                                                                                  'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},\n                                               'Name': 'bucketName',\n                                               'Owner': {   'Id': 'CanonicalId '\n                                                                  'of Owner'},\n                                               'PublicAccess': {   'EffectivePermission': 'NOT_PUBLIC',\n                                                                   'PermissionConfiguration': {   'AccountLevelPermissions': {   'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                          'BlockPublicPolicy': False,\n                                                                                                                                                          'IgnorePublicAcls': False,\n                                                                                                                                                          'RestrictPublicBuckets': False}},\n                                                                                                  'BucketLevelPermissions': {   'AccessControlList': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                         'AllowsPublicWriteAccess': False},\n                                                                                                                                'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                         'BlockPublicPolicy': False,\n                                                                                                                                                         'IgnorePublicAcls': False,\n                                                                                                                                                         'RestrictPublicBuckets': False},\n                                                                                                                                'BucketPolicy': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                    'AllowsPublicWriteAccess': False}}}},\n                                               'Tags': [   {   'Key': 'foo',\n                                                               'Value': 'bar'}],\n                                               'Type': 'Destination'}]},\n    'SchemaVersion': '2.0',\n    'Service': {   'Action': {   'ActionType': 'AWS_API_CALL',\n                                 'AwsApiCallAction': {   'Api': 'GeneratedFindingAPIName',\n                                                         'CallerType': 'Remote '\n                                                                       'IP',\n                                                         'RemoteIpDetails': {   'City': {   'CityName': 'GeneratedFindingCityName'},\n                                                                                'Country': {   'CountryName': 'GeneratedFindingCountryName'},\n                                                                                'GeoLocation': {   'Lat': 0,\n                                                                                                   'Lon': 0},\n                                                                                'IpAddressV4': '198.51.100.0',\n                                                                                'Organization': {   'Asn': '-1',\n                                                                                                    'AsnOrg': 'GeneratedFindingASNOrg',\n                                                                                                    'Isp': 'GeneratedFindingISP',\n                                                                                                    'Org': 'GeneratedFindingORG'}},\n                                                         'ServiceName': 'GeneratedFindingAPIServiceName'}},\n                   'Archived': False,\n                   'Count': 4,\n                   'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',\n                   'EventFirstSeen': '2020-11-25T13:46:37.960Z',\n                   'EventLastSeen': '2020-11-26T15:18:12.620Z',\n                   'ResourceRole': 'TARGET',\n                   'ServiceName': 'guardduty'},\n    'Severity': 2,\n    'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a '\n             'custom threat list.',\n    'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',\n    'UpdatedAt': '2020-11-26T15:18:12.620Z'}"}}]}
        ),
        "finding_payload_with_artifacts_with_refresh": (
            {
                'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                'description': {'format': 'text',
                                'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
                'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
                'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                               'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                               'aws_guardduty_region': 'us-west-2', 'aws_guardduty_resource_type': 'S3Bucket',
                               'aws_guardduty_count': '4',
                               'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a'}, 'artifacts': [
                {'type': {'name': 'aws_iam_access_key_id'}, 'description': {'format': 'text',
                                                                            'content': "'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'."},
                 'value': 'GeneratedFindingAccessKeyId'}, {'type': {'name': 'aws_iam_user_name'},
                                                           'description': {'format': 'text',
                                                                           'content': "'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'."},
                                                           'value': 'GeneratedFindingUserName'},
                {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                 'content': "'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'."},
                 'value': '198.51.100.0'}, {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                                            'content': "'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                            'value': '10.0.0.1'}, {'type': {'name': 'DNS Name'},
                                                                   'description': {'format': 'text',
                                                                                   'content': "'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                                   'value': 'GeneratedFindingPublicDNSName'},
                {'type': {'name': 'DNS Name'}, 'description': {'format': 'text',
                                                               'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                 'value': 'GeneratedFindingPrivateDnsName'}, {'type': {'name': 'DNS Name'},
                                                              'description': {'format': 'text',
                                                                              'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'."},
                                                              'value': 'GeneratedFindingPrivateName'}], 'comments': [{
                                                                                                                         'text': {
                                                                                                                             'format': 'text',
                                                                                                                             'content': "AWS GuardDuty finding Payload for refresh:\n{   'AccountId': '834299573936',\n    'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',\n    'CreatedAt': '2020-11-25T13:46:37.960Z',\n    'Description': 'An API was used to access a bucket from an IP address on a '\n                   'custom threat list.',\n    'Id': '60baffd3f9042e38640f2300d5c5a631',\n    'Partition': 'aws',\n    'Region': 'us-west-2',\n    'Resource': {   'AccessKeyDetails': {   'AccessKeyId': 'GeneratedFindingAccessKeyId',\n                                            'PrincipalId': 'GeneratedFindingPrincipalId',\n                                            'UserName': 'GeneratedFindingUserName',\n                                            'UserType': 'IAMUser'},\n                    'InstanceDetails': {   'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',\n                                           'IamInstanceProfile': {   'Arn': 'arn:aws:iam::834299573936:example/instance/profile',\n                                                                     'Id': 'GeneratedFindingInstanceProfileId'},\n                                           'ImageDescription': 'GeneratedFindingInstaceImageDescription',\n                                           'ImageId': 'ami-99999999',\n                                           'InstanceId': 'i-99999999',\n                                           'InstanceState': 'running',\n                                           'InstanceType': 'm3.xlarge',\n                                           'LaunchTime': '2016-08-02T02:05:06Z',\n                                           'NetworkInterfaces': [   {   'Ipv6Addresses': [   ],\n                                                                        'NetworkInterfaceId': 'eni-bfcffe88',\n                                                                        'PrivateDnsName': 'GeneratedFindingPrivateDnsName',\n                                                                        'PrivateIpAddress': '10.0.0.1',\n                                                                        'PrivateIpAddresses': [   {   'PrivateDnsName': 'GeneratedFindingPrivateName',\n                                                                                                      'PrivateIpAddress': '10.0.0.1'}],\n                                                                        'PublicDnsName': 'GeneratedFindingPublicDNSName',\n                                                                        'PublicIp': '198.51.100.0',\n                                                                        'SecurityGroups': [   {   'GroupId': 'GeneratedFindingSecurityId',\n                                                                                                  'GroupName': 'GeneratedFindingSecurityGroupName'}],\n                                                                        'SubnetId': 'GeneratedFindingSubnetId',\n                                                                        'VpcId': 'GeneratedFindingVPCId'}],\n                                           'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',\n                                           'ProductCodes': [{}],\n                                           'Tags': [   {   'Key': 'GeneratedFindingInstaceTag1',\n                                                           'Value': 'GeneratedFindingInstaceValue1'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag2',\n                                                           'Value': 'GeneratedFindingInstaceTagValue2'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag3',\n                                                           'Value': 'GeneratedFindingInstaceTagValue3'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag4',\n                                                           'Value': 'GeneratedFindingInstaceTagValue4'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag5',\n                                                           'Value': 'GeneratedFindingInstaceTagValue5'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag6',\n                                                           'Value': 'GeneratedFindingInstaceTagValue6'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag7',\n                                                           'Value': 'GeneratedFindingInstaceTagValue7'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag8',\n                                                           'Value': 'GeneratedFindingInstaceTagValue8'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag9',\n                                                           'Value': 'GeneratedFindingInstaceTagValue9'}]},\n                    'ResourceType': 'S3Bucket',\n                    'S3BucketDetails': [   {   'Arn': 'arn:aws:s3:::bucketName',\n                                               'CreatedAt': '2017-12-18 '\n                                                            '15:58:11',\n                                               'DefaultServerSideEncryption': {   'EncryptionType': 'SSEAlgorithm',\n                                                                                  'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},\n                                               'Name': 'bucketName',\n                                               'Owner': {   'Id': 'CanonicalId '\n                                                                  'of Owner'},\n                                               'PublicAccess': {   'EffectivePermission': 'NOT_PUBLIC',\n                                                                   'PermissionConfiguration': {   'AccountLevelPermissions': {   'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                          'BlockPublicPolicy': False,\n                                                                                                                                                          'IgnorePublicAcls': False,\n                                                                                                                                                          'RestrictPublicBuckets': False}},\n                                                                                                  'BucketLevelPermissions': {   'AccessControlList': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                         'AllowsPublicWriteAccess': False},\n                                                                                                                                'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                         'BlockPublicPolicy': False,\n                                                                                                                                                         'IgnorePublicAcls': False,\n                                                                                                                                                         'RestrictPublicBuckets': False},\n                                                                                                                                'BucketPolicy': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                    'AllowsPublicWriteAccess': False}}}},\n                                               'Tags': [   {   'Key': 'foo',\n                                                               'Value': 'bar'}],\n                                               'Type': 'Destination'}]},\n    'SchemaVersion': '2.0',\n    'Service': {   'Action': {   'ActionType': 'AWS_API_CALL',\n                                 'AwsApiCallAction': {   'Api': 'GeneratedFindingAPIName',\n                                                         'CallerType': 'Remote '\n                                                                       'IP',\n                                                         'RemoteIpDetails': {   'City': {   'CityName': 'GeneratedFindingCityName'},\n                                                                                'Country': {   'CountryName': 'GeneratedFindingCountryName'},\n                                                                                'GeoLocation': {   'Lat': 0,\n                                                                                                   'Lon': 0},\n                                                                                'IpAddressV4': '198.51.100.0',\n                                                                                'Organization': {   'Asn': '-1',\n                                                                                                    'AsnOrg': 'GeneratedFindingASNOrg',\n                                                                                                    'Isp': 'GeneratedFindingISP',\n                                                                                                    'Org': 'GeneratedFindingORG'}},\n                                                         'ServiceName': 'GeneratedFindingAPIServiceName'}},\n                   'Archived': False,\n                   'Count': 4,\n                   'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',\n                   'EventFirstSeen': '2020-11-25T13:46:37.960Z',\n                   'EventLastSeen': '2020-11-26T15:18:12.620Z',\n                   'ResourceRole': 'TARGET',\n                   'ServiceName': 'guardduty'},\n    'Severity': 2,\n    'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a '\n             'custom threat list.',\n    'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',\n    'UpdatedAt': '2020-11-26T15:18:12.620Z'}"}}]}        ),
        "finding_payload_data_tables":(
            {"gd_finding_overview": [{"cells": {"count": {"value": "4"},
                                                "severity": {"value": "2"},
                                                "query_execution_date": {"value": "2021-01-22 15:45:26"},
                                                "resource_id": {"value": "bucketName"},
                                                "created_at": {"value": "2020-11-25T13:46:37.960Z"},
                                                "updated_at": {"value": "2020-11-26T15:18:12.620Z"},
                                                "region": {"value": "us-west-2"},
                                                "account_id": {"value": "834299573936"}}}
                                     ],
             "gd_instance_details": [{"cells": {"public_ip": {"value": "198.51.100.0"},
                                                "private_dns_name": {"value": "GeneratedFindingPrivateDnsName"},
                                                "query_execution_date": {"value": "2021-01-22 15:45:26"},
                                                "instance_id": {"value": "i-99999999"},
                                                "instance_state": {"value": "running"},
                                                "public_dns_name": {"value": "GeneratedFindingPublicDNSName"},
                                                "type": {"value": "m3.xlarge"}, "private_ip": {"value": "10.0.0.1"}}}
                                     ],
             "gd_access_key_details": [{"cells": {"principal_id": {"value": "GeneratedFindingPrincipalId"},
                                                  "user_name": {"value": "GeneratedFindingUserName"},
                                                  "user_type": {"value": "IAMUser"},
                                                  "query_execution_date": {"value": "2021-01-22 15:45:26"},
                                                  "access_key_id": {"value": "GeneratedFindingAccessKeyId"}}}
                                       ],
             "gd_resource_affected": [{"cells": {"instance_id": {"value": "i-99999999"},
                                                 "instance_type": {"value": "m3.xlarge"},
                                                 "resource_role": {"value": "TARGET"},
                                                 "query_execution_date": {"value": "2021-01-22 15:45:26"},
                                                 "resource_type": {"value": "S3Bucket"}}}
                                      ],
             "gd_action_details": [{"cells": {"action_type": {"value": "AWS_API_CALL"},
                                              "query_execution_date": {"value": "2021-01-22 15:45:26"},
                                              "actor_caller_type": {"value": "Remote IP"},
                                              "service_name": {"value": "GeneratedFindingAPIServiceName"},
                                              "isp": {"value": "GeneratedFindingISP"},
                                              "action_api": {"value": "GeneratedFindingAPIName"},
                                              "country_name": {"value": "GeneratedFindingCountryName"},
                                              "event_first_seen": {"value": "2020-11-25T13:46:37.960Z"},
                                              "event_last_seen": {"value": "2020-11-26T15:18:12.620Z"},
                                              "asn_org": {"value": "GeneratedFindingASNOrg"},
                                              "city_name": {"value": "GeneratedFindingCityName"},
                                              "org": {"value": "GeneratedFindingORG"},
                                              "asn": {"value": "-1"},
                                              "remote_ip": {"value": "198.51.100.0"}}}
                                   ],
             "gd_s3_bucket_details": [{"cells": {"bucket_type": {"value": "Destination"},
                                                 "query_execution_date": {"value": "2021-01-22 15:45:26"},
                                                 "encryption_type": {"value": "SSEAlgorithm"},
                                                 "bucket_name": {"value": "bucketName"},
                                                 "kms_master_key_arn": {
                                                     "value": "arn:aws:kms:region:123456789012:key/key-id"},
                                                 "bucket_arn": {"value": "arn:aws:s3:::bucketName"},
                                                 "bucket_owner": {"value": "CanonicalId of Owner"},
                                                 "effective_permissions": {"value": "NOT_PUBLIC"}}}
                                      ]
             }
        ),
        "replace_datetime": (
            {'description': {
                'content': 'An API was used to access a bucket from an IP address on a custom threat list.',
                'format': 'text'},
             'discovered_date': '2020-11-25T13:46:37.960Z',
             'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
             'properties': {'aws_guardduty_archived': 'False',
                            'aws_guardduty_count': '4',
                            'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a',
                            'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                            'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                            'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                            'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                            'aws_guardduty_region': 'us-west-2',
                            'aws_guardduty_resource_type': 'S3Bucket',
                            'aws_guardduty_severity': '2'},
             'severity_code': 'Low'}
        ),
        "refresh_finding_no_artifacts": (
            {
                'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                'description': {'format': 'text',
                                'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
                'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
                'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                               'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                               'aws_guardduty_region': 'us-west-2', 'aws_guardduty_severity': '2',
                               'aws_guardduty_resource_type': 'S3Bucket',
                               'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a',
                               'aws_guardduty_count': '4', 'aws_guardduty_archived': 'False'}, 'artifacts': [
                {'type': {'name': 'aws_iam_access_key_id'}, 'description': {'format': 'text',
                                                                            'content': "'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'."},
                 'value': 'GeneratedFindingAccessKeyId'}, {'type': {'name': 'aws_iam_user_name'},
                                                           'description': {'format': 'text',
                                                                           'content': "'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'."},
                                                           'value': 'GeneratedFindingUserName'},
                {'type': {'name': 'aws_s3_bucket_name'}, 'description': {'format': 'text',
                                                                         'content': "'AWS S3 Bucket Name' extracted from GuardDuty from finding property 'Name' at path '['Resource', 'S3BucketDetails', 0]'."},
                 'value': 'bucketName'}, {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                                          'content': "'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'."},
                                          'value': '198.51.100.0'}, {'type': {'name': 'IP Address'},
                                                                     'description': {'format': 'text',
                                                                                     'content': "'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                                     'value': '10.0.0.1'},
                {'type': {'name': 'DNS Name'}, 'description': {'format': 'text',
                                                               'content': "'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                 'value': 'GeneratedFindingPublicDNSName'}, {'type': {'name': 'DNS Name'},
                                                             'description': {'format': 'text',
                                                                             'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                             'value': 'GeneratedFindingPrivateDnsName'},
                {'type': {'name': 'DNS Name'}, 'description': {'format': 'text',
                                                               'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'."},
                 'value': 'GeneratedFindingPrivateName'}], 'comments': []}
        ),
        "refresh_finding_no_artifacts_py2": (
            {u'discovered_date': u'2020-11-25T13:46:37.960Z', u'description': {
                u'content': u'An API was used to access a bucket from an IP address on a custom threat list.',
                u'format': u'text'}, u'artifacts': [{u'type': {u'name': u'DNS Name'}, u'description': {
                u'content': u"'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'.",
                u'format': u'text'}, u'value': u'GeneratedFindingPublicDNSName'},
                                                    {u'type': {u'name': u'aws_iam_user_name'}, u'description': {
                                                        u'content': u"'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'.",
                                                        u'format': u'text'}, u'value': u'GeneratedFindingUserName'},
                                                    {u'type': {u'name': u'aws_s3_bucket_name'}, u'description': {
                                                        u'content': u"'AWS S3 Bucket Name' extracted from GuardDuty from finding property 'Name' at path '['Resource', 'S3BucketDetails', 0]'.",
                                                        u'format': u'text'}, u'value': u'bucketName'},
                                                    {u'type': {u'name': u'aws_iam_access_key_id'}, u'description': {
                                                        u'content': u"'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'.",
                                                        u'format': u'text'}, u'value': u'GeneratedFindingAccessKeyId'},
                                                    {u'type': {u'name': u'DNS Name'}, u'description': {
                                                        u'content': u"'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'.",
                                                        u'format': u'text'}, u'value': u'GeneratedFindingPrivateName'},
                                                    {u'type': {u'name': u'IP Address'}, u'description': {
                                                        u'content': u"'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'.",
                                                        u'format': u'text'}, u'value': u'198.51.100.0'},
                                                    {u'type': {u'name': u'IP Address'}, u'description': {
                                                        u'content': u"'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'.",
                                                        u'format': u'text'}, u'value': u'10.0.0.1'},
                                                    {u'type': {u'name': u'DNS Name'}, u'description': {
                                                        u'content': u"'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'.",
                                                        u'format': u'text'},
                                                     u'value': u'GeneratedFindingPrivateDnsName'}],
             u'severity_code': u'Low', u'comments': [], u'properties': {u'aws_guardduty_resource_type': u'S3Bucket',
                                                                        u'aws_guardduty_finding_updated_at': u'2020-11-26T15:18:12.620Z',
                                                                        u'aws_guardduty_count': '4',
                                                                        u'aws_guardduty_finding_arn': u'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                                                                        u'aws_guardduty_detector_id': u'f2baedb0ac74f8f42fc929e15f56da6a',
                                                                        u'aws_guardduty_finding_type': u'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                                                                        u'aws_guardduty_finding_id': u'60baffd3f9042e38640f2300d5c5a631',
                                                                        u'aws_guardduty_archived': u'False',
                                                                        u'aws_guardduty_region': u'us-west-2',
                                                                        u'aws_guardduty_severity': '2'},
             u'name': u'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.'}
        ),
        "refresh_finding_with_artifacts": (
            []
        ),
        "refresh_finding_to_json": (
            {'timestamp': '2021-01-22 15:45:26',
             'region': 'us-west-2',
             'finding': {'AccountId': '834299573936',
                         'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                         'CreatedAt': '2020-11-25T13:46:37.960Z',
                         'Description': 'An API was used to access a bucket from an IP address on a custom threat list.',
                         'Id': '60baffd3f9042e38640f2300d5c5a631', 'Partition': 'aws', 'Region': 'us-west-2',
                         'Resource': {'AccessKeyDetails': {'AccessKeyId': 'GeneratedFindingAccessKeyId',
                                                           'PrincipalId': 'GeneratedFindingPrincipalId',
                                                           'UserName': 'GeneratedFindingUserName',
                                                           'UserType': 'IAMUser'}, 'S3BucketDetails': [
                             {'Arn': 'arn:aws:s3:::bucketName', 'Name': 'bucketName', 'Type': 'Destination',
                              'CreatedAt': '2017-12-18 15:58:11', 'Owner': {'Id': 'CanonicalId of Owner'},
                              'Tags': [{'Key': 'foo', 'Value': 'bar'}],
                              'DefaultServerSideEncryption': {'EncryptionType': 'SSEAlgorithm',
                                                              'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},
                              'PublicAccess': {'PermissionConfiguration': {'BucketLevelPermissions': {
                                  'AccessControlList': {'AllowsPublicReadAccess': False,
                                                        'AllowsPublicWriteAccess': False},
                                  'BucketPolicy': {'AllowsPublicReadAccess': False, 'AllowsPublicWriteAccess': False},
                                  'BlockPublicAccess': {'IgnorePublicAcls': False, 'RestrictPublicBuckets': False,
                                                        'BlockPublicAcls': False, 'BlockPublicPolicy': False}},
                                                                           'AccountLevelPermissions': {
                                                                               'BlockPublicAccess': {
                                                                                   'IgnorePublicAcls': False,
                                                                                   'RestrictPublicBuckets': False,
                                                                                   'BlockPublicAcls': False,
                                                                                   'BlockPublicPolicy': False}}},
                                               'EffectivePermission': 'NOT_PUBLIC'}}],
                                      'InstanceDetails': {'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',
                                                          'IamInstanceProfile': {
                                                              'Arn': 'arn:aws:iam::834299573936:example/instance/profile',
                                                              'Id': 'GeneratedFindingInstanceProfileId'},
                                                          'ImageDescription': 'GeneratedFindingInstaceImageDescription',
                                                          'ImageId': 'ami-99999999', 'InstanceId': 'i-99999999',
                                                          'InstanceState': 'running', 'InstanceType': 'm3.xlarge',
                                                          'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',
                                                          'LaunchTime': '2016-08-02T02:05:06Z', 'NetworkInterfaces': [
                                              {'Ipv6Addresses': [], 'NetworkInterfaceId': 'eni-bfcffe88',
                                               'PrivateDnsName': 'GeneratedFindingPrivateDnsName',
                                               'PrivateIpAddress': '10.0.0.1', 'PrivateIpAddresses': [
                                                  {'PrivateDnsName': 'GeneratedFindingPrivateName',
                                                   'PrivateIpAddress': '10.0.0.1'}],
                                               'PublicDnsName': 'GeneratedFindingPublicDNSName',
                                               'PublicIp': '198.51.100.0', 'SecurityGroups': [
                                                  {'GroupId': 'GeneratedFindingSecurityId',
                                                   'GroupName': 'GeneratedFindingSecurityGroupName'}],
                                               'SubnetId': 'GeneratedFindingSubnetId',
                                               'VpcId': 'GeneratedFindingVPCId'}], 'ProductCodes': [{}], 'Tags': [
                                              {'Key': 'GeneratedFindingInstaceTag1',
                                               'Value': 'GeneratedFindingInstaceValue1'},
                                              {'Key': 'GeneratedFindingInstaceTag2',
                                               'Value': 'GeneratedFindingInstaceTagValue2'},
                                              {'Key': 'GeneratedFindingInstaceTag3',
                                               'Value': 'GeneratedFindingInstaceTagValue3'},
                                              {'Key': 'GeneratedFindingInstaceTag4',
                                               'Value': 'GeneratedFindingInstaceTagValue4'},
                                              {'Key': 'GeneratedFindingInstaceTag5',
                                               'Value': 'GeneratedFindingInstaceTagValue5'},
                                              {'Key': 'GeneratedFindingInstaceTag6',
                                               'Value': 'GeneratedFindingInstaceTagValue6'},
                                              {'Key': 'GeneratedFindingInstaceTag7',
                                               'Value': 'GeneratedFindingInstaceTagValue7'},
                                              {'Key': 'GeneratedFindingInstaceTag8',
                                               'Value': 'GeneratedFindingInstaceTagValue8'},
                                              {'Key': 'GeneratedFindingInstaceTag9',
                                               'Value': 'GeneratedFindingInstaceTagValue9'}]},
                                      'ResourceType': 'S3Bucket'}, 'SchemaVersion': '2.0', 'Service': {
                    'Action': {'ActionType': 'AWS_API_CALL',
                               'AwsApiCallAction': {'Api': 'GeneratedFindingAPIName', 'CallerType': 'Remote IP',
                                                    'RemoteIpDetails': {
                                                        'City': {'CityName': 'GeneratedFindingCityName'},
                                                        'Country': {'CountryName': 'GeneratedFindingCountryName'},
                                                        'GeoLocation': {'Lat': 0, 'Lon': 0},
                                                        'IpAddressV4': '198.51.100.0', 'Organization': {'Asn': '-1',
                                                                                                        'AsnOrg': 'GeneratedFindingASNOrg',
                                                                                                        'Isp': 'GeneratedFindingISP',
                                                                                                        'Org': 'GeneratedFindingORG'}},
                                                    'ServiceName': 'GeneratedFindingAPIServiceName'}},
                    'Archived': False, 'Count': 4, 'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',
                    'EventFirstSeen': '2020-11-25T13:46:37.960Z', 'EventLastSeen': '2020-11-26T15:18:12.620Z',
                    'ResourceRole': 'TARGET', 'ServiceName': 'guardduty'}, 'Severity': 2,
                         'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                         'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                         'UpdatedAt': '2020-11-26T15:18:12.620Z'}, 'payload': {
                'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                'description': {'format': 'text',
                                'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
                'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
                'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                               'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                               'aws_guardduty_region': 'us-west-2', 'aws_guardduty_resource_type': 'S3Bucket',
                               'aws_guardduty_count': '4',
                               'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a'}, 'artifacts': [
                    {'type': {'name': 'aws_iam_access_key_id'}, 'description': {'format': 'text',
                                                                                'content': "'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'."},
                     'value': 'GeneratedFindingAccessKeyId'}, {'type': {'name': 'aws_iam_user_name'},
                                                               'description': {'format': 'text',
                                                                               'content': "'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'."},
                                                               'value': 'GeneratedFindingUserName'},
                    {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                     'content': "'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'."},
                     'value': '198.51.100.0'}, {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                                                'content': "'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                'value': '10.0.0.1'}, {'type': {'name': 'DNS Name'},
                                                                       'description': {'format': 'text',
                                                                                       'content': "'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                                       'value': 'GeneratedFindingPublicDNSName'},
                    {'type': {'name': 'DNS Name'}, 'description': {'format': 'text',
                                                                   'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                     'value': 'GeneratedFindingPrivateDnsName'}, {'type': {'name': 'DNS Name'},
                                                                  'description': {'format': 'text',
                                                                                  'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'."},
                                                                  'value': 'GeneratedFindingPrivateName'}],
                'comments': [{'text': {'format': 'text',
                                       'content': "AWS GuardDuty finding Payload:\n{   'AccountId': '834299573936',\n    'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',\n    'CreatedAt': '2020-11-25T13:46:37.960Z',\n    'Description': 'An API was used to access a bucket from an IP address on a '\n                   'custom threat list.',\n    'Id': '60baffd3f9042e38640f2300d5c5a631',\n    'Partition': 'aws',\n    'Region': 'us-west-2',\n    'Resource': {   'AccessKeyDetails': {   'AccessKeyId': 'GeneratedFindingAccessKeyId',\n                                            'PrincipalId': 'GeneratedFindingPrincipalId',\n                                            'UserName': 'GeneratedFindingUserName',\n                                            'UserType': 'IAMUser'},\n                    'InstanceDetails': {   'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',\n                                           'IamInstanceProfile': {   'Arn': 'arn:aws:iam::834299573936:example/instance/profile',\n                                                                     'Id': 'GeneratedFindingInstanceProfileId'},\n                                           'ImageDescription': 'GeneratedFindingInstaceImageDescription',\n                                           'ImageId': 'ami-99999999',\n                                           'InstanceId': 'i-99999999',\n                                           'InstanceState': 'running',\n                                           'InstanceType': 'm3.xlarge',\n                                           'LaunchTime': '2016-08-02T02:05:06Z',\n                                           'NetworkInterfaces': [   {   'Ipv6Addresses': [   ],\n                                                                        'NetworkInterfaceId': 'eni-bfcffe88',\n                                                                        'PrivateDnsName': 'GeneratedFindingPrivateDnsName',\n                                                                        'PrivateIpAddress': '10.0.0.1',\n                                                                        'PrivateIpAddresses': [   {   'PrivateDnsName': 'GeneratedFindingPrivateName',\n                                                                                                      'PrivateIpAddress': '10.0.0.1'}],\n                                                                        'PublicDnsName': 'GeneratedFindingPublicDNSName',\n                                                                        'PublicIp': '198.51.100.0',\n                                                                        'SecurityGroups': [   {   'GroupId': 'GeneratedFindingSecurityId',\n                                                                                                  'GroupName': 'GeneratedFindingSecurityGroupName'}],\n                                                                        'SubnetId': 'GeneratedFindingSubnetId',\n                                                                        'VpcId': 'GeneratedFindingVPCId'}],\n                                           'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',\n                                           'ProductCodes': [{}],\n                                           'Tags': [   {   'Key': 'GeneratedFindingInstaceTag1',\n                                                           'Value': 'GeneratedFindingInstaceValue1'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag2',\n                                                           'Value': 'GeneratedFindingInstaceTagValue2'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag3',\n                                                           'Value': 'GeneratedFindingInstaceTagValue3'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag4',\n                                                           'Value': 'GeneratedFindingInstaceTagValue4'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag5',\n                                                           'Value': 'GeneratedFindingInstaceTagValue5'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag6',\n                                                           'Value': 'GeneratedFindingInstaceTagValue6'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag7',\n                                                           'Value': 'GeneratedFindingInstaceTagValue7'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag8',\n                                                           'Value': 'GeneratedFindingInstaceTagValue8'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag9',\n                                                           'Value': 'GeneratedFindingInstaceTagValue9'}]},\n                    'ResourceType': 'S3Bucket',\n                    'S3BucketDetails': [   {   'Arn': 'arn:aws:s3:::bucketName',\n                                               'CreatedAt': '2017-12-18 '\n                                                            '15:58:11',\n                                               'DefaultServerSideEncryption': {   'EncryptionType': 'SSEAlgorithm',\n                                                                                  'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},\n                                               'Name': 'bucketName',\n                                               'Owner': {   'Id': 'CanonicalId '\n                                                                  'of Owner'},\n                                               'PublicAccess': {   'EffectivePermission': 'NOT_PUBLIC',\n                                                                   'PermissionConfiguration': {   'AccountLevelPermissions': {   'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                          'BlockPublicPolicy': False,\n                                                                                                                                                          'IgnorePublicAcls': False,\n                                                                                                                                                          'RestrictPublicBuckets': False}},\n                                                                                                  'BucketLevelPermissions': {   'AccessControlList': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                         'AllowsPublicWriteAccess': False},\n                                                                                                                                'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                         'BlockPublicPolicy': False,\n                                                                                                                                                         'IgnorePublicAcls': False,\n                                                                                                                                                         'RestrictPublicBuckets': False},\n                                                                                                                                'BucketPolicy': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                    'AllowsPublicWriteAccess': False}}}},\n                                               'Tags': [   {   'Key': 'foo',\n                                                               'Value': 'bar'}],\n                                               'Type': 'Destination'}]},\n    'SchemaVersion': '2.0',\n    'Service': {   'Action': {   'ActionType': 'AWS_API_CALL',\n                                 'AwsApiCallAction': {   'Api': 'GeneratedFindingAPIName',\n                                                         'CallerType': 'Remote '\n                                                                       'IP',\n                                                         'RemoteIpDetails': {   'City': {   'CityName': 'GeneratedFindingCityName'},\n                                                                                'Country': {   'CountryName': 'GeneratedFindingCountryName'},\n                                                                                'GeoLocation': {   'Lat': 0,\n                                                                                                   'Lon': 0},\n                                                                                'IpAddressV4': '198.51.100.0',\n                                                                                'Organization': {   'Asn': '-1',\n                                                                                                    'AsnOrg': 'GeneratedFindingASNOrg',\n                                                                                                    'Isp': 'GeneratedFindingISP',\n                                                                                                    'Org': 'GeneratedFindingORG'}},\n                                                         'ServiceName': 'GeneratedFindingAPIServiceName'}},\n                   'Archived': False,\n                   'Count': 4,\n                   'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',\n                   'EventFirstSeen': '2020-11-25T13:46:37.960Z',\n                   'EventLastSeen': '2020-11-26T15:18:12.620Z',\n                   'ResourceRole': 'TARGET',\n                   'ServiceName': 'guardduty'},\n    'Severity': 2,\n    'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a '\n             'custom threat list.',\n    'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',\n    'UpdatedAt': '2020-11-26T15:18:12.620Z'}"}}]},
             'data_tables': {'gd_action_details': [{'cells': {'action_type': {'value': 'AWS_API_CALL'},
                                                              'action_api': {'value': 'GeneratedFindingAPIName'},
                                                              'event_first_seen': {'value': '2020-11-25T13:46:37.960Z'},
                                                              'event_last_seen': {'value': '2020-11-26T15:18:12.620Z'},
                                                              'actor_caller_type': {'value': 'Remote IP'},
                                                              'city_name': {'value': 'GeneratedFindingCityName'},
                                                              'country_name': {'value': 'GeneratedFindingCountryName'},
                                                              'asn': {'value': '-1'},
                                                              'asn_org': {'value': 'GeneratedFindingASNOrg'},
                                                              'isp': {'value': 'GeneratedFindingISP'},
                                                              'org': {'value': 'GeneratedFindingORG'},
                                                              'action_service_name': {
                                                                  'value': 'GeneratedFindingAPIServiceName'},
                                                              'remote_ip': {'value': '198.51.100.0'}}}],
                             'gd_resource_affected': [{'cells': {'resource_type': {'value': 'S3Bucket'},
                                                                 'instance_id': {'value': 'i-99999999'},
                                                                 'instance_type': {'value': 'm3.xlarge'},
                                                                 'instance_state': {'value': 'running'},
                                                                 'resource_role': {'value': 'TARGET'},
                                                                 'instance_private_ip': {'value': '10.0.0.1'},
                                                                 'instance_private_dns': {
                                                                     'value': 'GeneratedFindingPrivateName'},
                                                                 'instance_public_ip': {'value': '198.51.100.0'},
                                                                 'instance_public_dns': {
                                                                     'value': 'GeneratedFindingPublicDNSName'},
                                                                 's3bucket_name': {'value': 'bucketName'},
                                                                 's3bucket_owner': {
                                                                     'value': 'CanonicalId of Owner'}}}]}}
        )
    }
    return response[type]

## Mock results - Expected results before updates/filters applied.
def get_mocked_finding_data(type):
    response = {
        "replace_datetime_finding":({"Severity": 7,
                             "CreatedAt": datetime.datetime(2017, 12, 18, 15, 58, 11, 551000, tzinfo=tzlocal()),
                             "Dates": [{'TestDate': datetime.datetime(2017, 10, 16, 13, 56, 10, 551000, tzinfo=tzlocal())}],
                             "OtherDates": {'TestDate2': datetime.datetime(2016, 10, 16, 13, 56, 10, 551000, tzinfo=tzlocal())}
                             }
        ),
        "convert_unicode_finding": ({u"Severity": 7,
                                      u"CreatedAt": u"2017-12-26T15:18:12.620Z",
                                      u"Dates": [{'TestDate': u"2019-11-26T15:18:12.620Z"}],
                                      u"OtherDates": {u'TestDate2': u"2020-11-26T15:18:12.620Z"}
                                      }
        ),
    }
    return response[type]

# Mocked resilient for standalone tests.
def get_resilient_responses(op):
    response = {
        "find_resilient_incident_for_req": (
            [{'name': 'AWS GuardDuty: API UpdateLoginProfile was invoked using root credentials.',
              'description': '<div>API UpdateLoginProfile was invoked using root credentials from IP address 173.48.174.220.</div>',
              'phase_id': 1009, 'inc_training': False, 'id': 2167, 'sequence_code': '5908-73',
              'discovered_date': 1605624125336, 'due_date': None, 'create_date': 1610387339603, 'owner_id': 4,
              'severity_code': 100, 'plan_status': 'A'}
             ]
        ),
        "create_incident": (
            {'dtm': {}, 'cm': {'unassigneds': [], 'total': 0, 'geo_counts': {}}, 'regulators': {'ids': []},
             'hipaa': {'hipaa_adverse': None, 'hipaa_misused': None, 'hipaa_acquired': None,
                       'hipaa_additional_misuse': None, 'hipaa_breach': None, 'hipaa_adverse_comment': None,
                       'hipaa_misused_comment': None, 'hipaa_acquired_comment': None,
                       'hipaa_additional_misuse_comment': None, 'hipaa_breach_comment': None}, 'tasks': None,
             'artifacts': [{'id': 1008, 'type': 2, 'value': 'GeneratedFindingPrivateDnsName',
                            'description': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'.",
                            'attachment': None, 'parent_id': None,
                            'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin',
                                        'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com',
                                        'locked': False, 'password_changed': False, 'is_external': False},
                            'inc_id': 2239,
                            'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                            'inc_owner': 4, 'hits': [], 'created': 1610391037106, 'last_modified_time': 1610391037108,
                            'last_modified_by': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                 'display_name': 'Resilient Sysadmin'}, 'pending_sources': [],
                            'perms': {'read': True, 'write': True, 'delete': True}, 'properties': None,
                            'whois': {'pending': False, 'invalid': True}, 'actions': [],
                            'hash': '5c846bd15c8a1acdf13163d01e7cf74a5e7babea8f52563aa1f2a5aba6716447',
                            'relating': None, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                                    'display_name': 'Resilient Sysadmin'},
                            'ip': {'source': None, 'destination': None}},
                           {'id': 1009, 'type': 2, 'value': 'GeneratedFindingPrivateName',
                            'description': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'.",
                            'attachment': None, 'parent_id': None,
                            'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin',
                                        'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com',
                                        'locked': False, 'password_changed': False, 'is_external': False},
                            'inc_id': 2239,
                            'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                            'inc_owner': 4, 'hits': [], 'created': 1610391037123, 'last_modified_time': 1610391037125,
                            'last_modified_by': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                 'display_name': 'Resilient Sysadmin'}, 'pending_sources': [],
                            'perms': {'read': True, 'write': True, 'delete': True}, 'properties': None,
                            'whois': {'pending': False, 'invalid': True}, 'actions': [],
                            'hash': 'c666da9ec698918d2dcd7639f73600bf9df58740d4200e344714e6adcc5c4605',
                            'relating': None, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                                    'display_name': 'Resilient Sysadmin'},
                            'ip': {'source': None, 'destination': None}},
                           {'id': 1004, 'type': 1082, 'value': 'GeneratedFindingUserName',
                            'description': "'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'.",
                            'attachment': None, 'parent_id': None,
                            'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin',
                                        'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com',
                                        'locked': False, 'password_changed': False, 'is_external': False},
                            'inc_id': 2239,
                            'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                            'inc_owner': 4, 'hits': [], 'created': 1610391037036, 'last_modified_time': 1610391037039,
                            'last_modified_by': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                 'display_name': 'Resilient Sysadmin'}, 'pending_sources': [],
                            'perms': {'read': True, 'write': True, 'delete': True}, 'properties': None, 'actions': [],
                            'hash': 'e18bc81b2e031729d3b74245f7e3d42efdf9a8fffc2d484aa424b2f2073e8bfe',
                            'relating': None, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                                    'display_name': 'Resilient Sysadmin'},
                            'ip': {'source': None, 'destination': None}},
                           {'id': 1005, 'type': 1, 'value': '198.51.100.0',
                            'description': "'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'.",
                            'attachment': None, 'parent_id': None,
                            'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin',
                                        'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com',
                                        'locked': False, 'password_changed': False, 'is_external': False},
                            'inc_id': 2239,
                            'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                            'inc_owner': 4, 'hits': [], 'created': 1610391037053, 'last_modified_time': 1610391037055,
                            'last_modified_by': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                 'display_name': 'Resilient Sysadmin'}, 'pending_sources': [],
                            'perms': {'read': True, 'write': True, 'delete': True}, 'properties': None, 'actions': [],
                            'hash': '74d22f6d57644f8a2e67577dec95a74996f8b115f4ea20c4e5bb32b2981111a7',
                            'relating': None, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                                    'display_name': 'Resilient Sysadmin'},
                            'ip': {'source': None, 'destination': None}},
                           {'id': 1003, 'type': 1080, 'value': 'GeneratedFindingAccessKeyId',
                            'description': "'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'.",
                            'attachment': None, 'parent_id': None,
                            'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin',
                                        'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com',
                                        'locked': False, 'password_changed': False, 'is_external': False},
                            'inc_id': 2239,
                            'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                            'inc_owner': 4, 'hits': [], 'created': 1610391037016, 'last_modified_time': 1610391037020,
                            'last_modified_by': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                 'display_name': 'Resilient Sysadmin'}, 'pending_sources': [],
                            'perms': {'read': True, 'write': True, 'delete': True}, 'properties': None, 'actions': [],
                            'hash': '83376857d0fb2499b26c6a6152d92d6dd5bef5380e54b6cd0a3c91161f6f43e9',
                            'relating': None, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                                    'display_name': 'Resilient Sysadmin'},
                            'ip': {'source': None, 'destination': None}}, {'id': 1006, 'type': 1, 'value': '10.0.0.1',
                                                                           'description': "'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'.",
                                                                           'attachment': None, 'parent_id': None,
                                                                           'creator': {'id': 4, 'fname': 'Resilient',
                                                                                       'lname': 'Sysadmin',
                                                                                       'display_name': 'Resilient Sysadmin',
                                                                                       'status': 'A',
                                                                                       'email': 'a@a.com',
                                                                                       'locked': False,
                                                                                       'password_changed': False,
                                                                                       'is_external': False},
                                                                           'inc_id': 2239,
                                                                           'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                                                                           'inc_owner': 4, 'hits': [],
                                                                           'created': 1610391037070,
                                                                           'last_modified_time': 1610391037072,
                                                                           'last_modified_by': {'id': 4, 'type': 'user',
                                                                                                'name': 'a@a.com',
                                                                                                'display_name': 'Resilient Sysadmin'},
                                                                           'pending_sources': [],
                                                                           'perms': {'read': True, 'write': True,
                                                                                     'delete': True},
                                                                           'properties': None, 'actions': [],
                                                                           'hash': 'a4ebc6e0512c26fd6ae1df8ad942c5008a7fdfa7e1339168c8edd94ae488e77d',
                                                                           'relating': None,
                                                                           'creator_principal': {'id': 4,
                                                                                                 'type': 'user',
                                                                                                 'name': 'a@a.com',
                                                                                                 'display_name': 'Resilient Sysadmin'},
                                                                           'ip': {'source': None, 'destination': None}},
                           {'id': 1007, 'type': 2, 'value': 'GeneratedFindingPublicDNSName',
                            'description': "'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'.",
                            'attachment': None, 'parent_id': None,
                            'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin',
                                        'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com',
                                        'locked': False, 'password_changed': False, 'is_external': False},
                            'inc_id': 2239,
                            'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                            'inc_owner': 4, 'hits': [], 'created': 1610391037087, 'last_modified_time': 1610391037089,
                            'last_modified_by': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                 'display_name': 'Resilient Sysadmin'}, 'pending_sources': [],
                            'perms': {'read': True, 'write': True, 'delete': True}, 'properties': None,
                            'whois': {'pending': False, 'invalid': True}, 'actions': [],
                            'hash': '3a733bc5b809b1920418bf12995676ef55c1ef066103874ed15ef5d8b0c46ee8',
                            'relating': None, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com',
                                                                    'display_name': 'Resilient Sysadmin'},
                            'ip': {'source': None, 'destination': None}}],
             'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
             'description': '<div>An API was used to access a bucket from an IP address on a custom threat list.</div>',
             'phase_id': 1009, 'inc_training': False, 'vers': 2, 'addr': None, 'city': None,
             'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin', 'display_name': 'Resilient Sysadmin',
                         'status': 'A', 'email': 'a@a.com', 'locked': False, 'password_changed': False,
                         'is_external': False},
             'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com', 'display_name': 'Resilient Sysadmin'},
             'exposure_type_id': 1, 'incident_type_ids': [], 'reporter': None, 'state': None, 'country': None,
             'zip': None, 'workspace': 2, 'exposure': 0, 'org_handle': 202, 'members': [], 'negative_pr_likely': None,
             'perms': {'read': True, 'write': True, 'comment': True, 'assign': True, 'close': True,
                       'change_members': True, 'attach_file': True, 'read_attachments': True,
                       'delete_attachments': True, 'create_milestones': True, 'list_milestones': True,
                       'create_artifacts': True, 'list_artifacts': True, 'delete': True, 'change_workspace': True},
             'confirmed': False, 'task_changes': {'added': [], 'removed': []},
             'assessment': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n',
             'data_compromised': None, 'draft': False,
             'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                            'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                            'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z', 'aws_guardduty_count': '4',
                            'internal_customizations_field': None,
                            'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                            'aws_guardduty_resource_type': 'S3Bucket',
                            'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a',
                            'aws_guardduty_region': 'us-west-2'}, 'resolution_id': None, 'resolution_summary': None,
             'pii': {'data_compromised': None, 'determined_date': 1606311997960, 'harmstatus_id': 2,
                     'data_encrypted': None, 'data_contained': None, 'impact_likely': None, 'ny_impact_likely': None,
                     'or_impact_likely': None, 'wa_impact_likely': None, 'dc_impact_likely': None,
                     'data_source_ids': [], 'data_format': None,
                     'assessment': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n',
                     'exposure': 0, 'gdpr_harm_risk': None, 'gdpr_lawful_data_processing_categories': [],
                     'alberta_health_risk_assessment': None},
             'gdpr': {'gdpr_breach_circumstances': [], 'gdpr_breach_type': None, 'gdpr_personal_data': None,
                      'gdpr_identification': None, 'gdpr_consequences': None, 'gdpr_final_assessment': None,
                      'gdpr_breach_type_comment': None, 'gdpr_personal_data_comment': None,
                      'gdpr_identification_comment': None, 'gdpr_consequences_comment': None,
                      'gdpr_final_assessment_comment': None, 'gdpr_subsequent_notification': None},
             'regulator_risk': {}, 'inc_last_modified_date': 1610391037140, 'comments': [
                {'type': 'incident', 'id': 253, 'parent_id': None, 'user_id': 4, 'user_fname': 'Resilient',
                 'user_lname': 'Sysadmin',
                 'text': '<div>AWS GuardDuty finding Payload:<br/>&#x7b;&nbsp;  &#x27;AccountId&#x27;: &#x27;834299573936&#x27;,<br/>&nbsp; &nbsp; &#x27;Arn&#x27;: &#x27;arn:aws:guardduty:us&#x2d;west&#x2d;2:834299573936:detector&#x2f;f2baedb0ac74f8f42fc929e15f56da6a&#x2f;finding&#x2f;60baffd3f9042e38640f2300d5c5a631&#x27;,<br/>&nbsp; &nbsp; &#x27;CreatedAt&#x27;: &#x27;2020&#x2d;11&#x2d;25T13:46:37.960Z&#x27;,<br/>&nbsp; &nbsp; &#x27;Description&#x27;: &#x27;An API was used to access a bucket from an IP address on a &#x27;<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;custom threat list.&#x27;,<br/>&nbsp; &nbsp; &#x27;Id&#x27;: &#x27;60baffd3f9042e38640f2300d5c5a631&#x27;,<br/>&nbsp; &nbsp; &#x27;Partition&#x27;: &#x27;aws&#x27;,<br/>&nbsp; &nbsp; &#x27;Region&#x27;: &#x27;us&#x2d;west&#x2d;2&#x27;,<br/>&nbsp; &nbsp; &#x27;Resource&#x27;: &#x7b;&nbsp;  &#x27;AccessKeyDetails&#x27;: &#x7b;&nbsp;  &#x27;AccessKeyId&#x27;: &#x27;GeneratedFindingAccessKeyId&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PrincipalId&#x27;: &#x27;GeneratedFindingPrincipalId&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;UserName&#x27;: &#x27;GeneratedFindingUserName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;UserType&#x27;: &#x27;IAMUser&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;InstanceDetails&#x27;: &#x7b;&nbsp;  &#x27;AvailabilityZone&#x27;: &#x27;GeneratedFindingInstaceAvailabilityZone&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;IamInstanceProfile&#x27;: &#x7b;&nbsp;  &#x27;Arn&#x27;: &#x27;arn:aws:iam::834299573936:example&#x2f;instance&#x2f;profile&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Id&#x27;: &#x27;GeneratedFindingInstanceProfileId&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;ImageDescription&#x27;: &#x27;GeneratedFindingInstaceImageDescription&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;ImageId&#x27;: &#x27;ami&#x2d;99999999&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;InstanceId&#x27;: &#x27;i&#x2d;99999999&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;InstanceState&#x27;: &#x27;running&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;InstanceType&#x27;: &#x27;m3.xlarge&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;LaunchTime&#x27;: &#x27;2016&#x2d;08&#x2d;02T02:05:06Z&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;NetworkInterfaces&#x27;: &#x5b;&nbsp;  &#x7b;&nbsp;  &#x27;Ipv6Addresses&#x27;: &#x5b;&nbsp;  &#x5d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;NetworkInterfaceId&#x27;: &#x27;eni&#x2d;bfcffe88&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PrivateDnsName&#x27;: &#x27;GeneratedFindingPrivateDnsName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PrivateIpAddress&#x27;: &#x27;10.0.0.1&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PrivateIpAddresses&#x27;: &#x5b;&nbsp;  &#x7b;&nbsp;  &#x27;PrivateDnsName&#x27;: &#x27;GeneratedFindingPrivateName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PrivateIpAddress&#x27;: &#x27;10.0.0.1&#x27;&#x7d;&#x5d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PublicDnsName&#x27;: &#x27;GeneratedFindingPublicDNSName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;PublicIp&#x27;: &#x27;198.51.100.0&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;SecurityGroups&#x27;: &#x5b;&nbsp;  &#x7b;&nbsp;  &#x27;GroupId&#x27;: &#x27;GeneratedFindingSecurityId&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;GroupName&#x27;: &#x27;GeneratedFindingSecurityGroupName&#x27;&#x7d;&#x5d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;SubnetId&#x27;: &#x27;GeneratedFindingSubnetId&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;VpcId&#x27;: &#x27;GeneratedFindingVPCId&#x27;&#x7d;&#x5d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;OutpostArn&#x27;: &#x27;arn:aws:outposts:us&#x2d;west&#x2d;2:123456789000:outpost&#x2f;op&#x2d;0fbc006e9abbc73c3&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;ProductCodes&#x27;: &#x5b;&#x7b;&#x7d;&#x5d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Tags&#x27;: &#x5b;&nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag1&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceValue1&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag2&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue2&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag3&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue3&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag4&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue4&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag5&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue5&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag6&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue6&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag7&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue7&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag8&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue8&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;GeneratedFindingInstaceTag9&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;GeneratedFindingInstaceTagValue9&#x27;&#x7d;&#x5d;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;ResourceType&#x27;: &#x27;S3Bucket&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;S3BucketDetails&#x27;: &#x5b;&nbsp;  &#x7b;&nbsp;  &#x27;Arn&#x27;: &#x27;arn:aws:s3:::bucketName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;CreatedAt&#x27;: datetime.datetime(2017, 12, 18, 15, 58, 11, 551000, tzinfo&#x3d;tzlocal()),<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;DefaultServerSideEncryption&#x27;: &#x7b;&nbsp;  &#x27;EncryptionType&#x27;: &#x27;SSEAlgorithm&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;KmsMasterKeyArn&#x27;: &#x27;arn:aws:kms:region:123456789012:key&#x2f;key&#x2d;id&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Name&#x27;: &#x27;bucketName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Owner&#x27;: &#x7b;&nbsp;  &#x27;Id&#x27;: &#x27;CanonicalId &#x27;<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;of Owner&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;PublicAccess&#x27;: &#x7b;&nbsp;  &#x27;EffectivePermission&#x27;: &#x27;NOT&#x5f;PUBLIC&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;PermissionConfiguration&#x27;: &#x7b;&nbsp;  &#x27;AccountLevelPermissions&#x27;: &#x7b;&nbsp;  &#x27;BlockPublicAccess&#x27;: &#x7b;&nbsp;  &#x27;BlockPublicAcls&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;BlockPublicPolicy&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;IgnorePublicAcls&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;RestrictPublicBuckets&#x27;: False&#x7d;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;BucketLevelPermissions&#x27;: &#x7b;&nbsp;  &#x27;AccessControlList&#x27;: &#x7b;&nbsp;  &#x27;AllowsPublicReadAccess&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;AllowsPublicWriteAccess&#x27;: False&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;BlockPublicAccess&#x27;: &#x7b;&nbsp;  &#x27;BlockPublicAcls&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;BlockPublicPolicy&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;IgnorePublicAcls&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;RestrictPublicBuckets&#x27;: False&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;BucketPolicy&#x27;: &#x7b;&nbsp;  &#x27;AllowsPublicReadAccess&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;AllowsPublicWriteAccess&#x27;: False&#x7d;&#x7d;&#x7d;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Tags&#x27;: &#x5b;&nbsp;  &#x7b;&nbsp;  &#x27;Key&#x27;: &#x27;foo&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Value&#x27;: &#x27;bar&#x27;&#x7d;&#x5d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Type&#x27;: &#x27;Destination&#x27;&#x7d;&#x5d;&#x7d;,<br/>&nbsp; &nbsp; &#x27;SchemaVersion&#x27;: &#x27;2.0&#x27;,<br/>&nbsp; &nbsp; &#x27;Service&#x27;: &#x7b;&nbsp;  &#x27;Action&#x27;: &#x7b;&nbsp;  &#x27;ActionType&#x27;: &#x27;AWS&#x5f;API&#x5f;CALL&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;AwsApiCallAction&#x27;: &#x7b;&nbsp;  &#x27;Api&#x27;: &#x27;GeneratedFindingAPIName&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;CallerType&#x27;: &#x27;Remote &#x27;<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;IP&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;RemoteIpDetails&#x27;: &#x7b;&nbsp;  &#x27;City&#x27;: &#x7b;&nbsp;  &#x27;CityName&#x27;: &#x27;GeneratedFindingCityName&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;Country&#x27;: &#x7b;&nbsp;  &#x27;CountryName&#x27;: &#x27;GeneratedFindingCountryName&#x27;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;GeoLocation&#x27;: &#x7b;&nbsp;  &#x27;Lat&#x27;: 0,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Lon&#x27;: 0&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;IpAddressV4&#x27;: &#x27;198.51.100.0&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;Organization&#x27;: &#x7b;&nbsp;  &#x27;Asn&#x27;: &#x27;&#x2d;1&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;AsnOrg&#x27;: &#x27;GeneratedFindingASNOrg&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;Isp&#x27;: &#x27;GeneratedFindingISP&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &#x27;Org&#x27;: &#x27;GeneratedFindingORG&#x27;&#x7d;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;ServiceName&#x27;: &#x27;GeneratedFindingAPIServiceName&#x27;&#x7d;&#x7d;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Archived&#x27;: False,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;Count&#x27;: 4,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;DetectorId&#x27;: &#x27;f2baedb0ac74f8f42fc929e15f56da6a&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;EventFirstSeen&#x27;: &#x27;2020&#x2d;11&#x2d;25T13:46:37.960Z&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;EventLastSeen&#x27;: &#x27;2020&#x2d;11&#x2d;26T15:18:12.620Z&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;ResourceRole&#x27;: &#x27;TARGET&#x27;,<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;ServiceName&#x27;: &#x27;guardduty&#x27;&#x7d;,<br/>&nbsp; &nbsp; &#x27;Severity&#x27;: 2,<br/>&nbsp; &nbsp; &#x27;Title&#x27;: &#x27;API GeneratedFindingAPIName was invoked from an IP address on a &#x27;<br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &#x27;custom threat list.&#x27;,<br/>&nbsp; &nbsp; &#x27;Type&#x27;: &#x27;UnauthorizedAccess:S3&#x2f;MaliciousIPCaller.Custom&#x27;,<br/>&nbsp; &nbsp; &#x27;UpdatedAt&#x27;: &#x27;2020&#x2d;11&#x2d;26T15:18:12.620Z&#x27;&#x7d;</div>',
                 'create_date': 1610391037127, 'modify_date': 1610391037127, 'children': [], 'mentioned_users': [],
                 'is_deleted': False, 'modify_user': {'id': 4, 'first_name': 'Resilient', 'last_name': 'Sysadmin'},
                 'actions': [], 'inc_id': 2239,
                 'inc_name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                 'task_id': None, 'task_name': None, 'task_custom': None, 'task_members': None, 'task_at_id': None,
                 'inc_owner': 4, 'user_name': 'Resilient Sysadmin',
                 'modify_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com', 'display_name': 'Resilient Sysadmin'},
                 'comment_perms': {'update': True, 'delete': True}}], 'actions': [],
             'timer_field_summarized_incident_data': [], 'admin_id': None, 'creator_id': 4, 'crimestatus_id': 1,
             'employee_involved': None, 'end_date': None, 'exposure_dept_id': None, 'exposure_individual_name': None,
             'exposure_vendor_id': None, 'jurisdiction_name': None, 'jurisdiction_reg_id': None, 'start_date': None,
             'inc_start': None, 'org_id': 202, 'is_scenario': False, 'hard_liability': 0, 'nist_attack_vectors': [],
             'id': 2239, 'sequence_code': None, 'discovered_date': 1606311997960, 'due_date': None,
             'create_date': 1610391036688, 'owner_id': 4, 'severity_code': 100, 'plan_status': 'A'}
        ),
        "find_resilient_artifacts_for_incident_with_artifacts": ({
                'GeneratedFindingPrivateName': 'DNS Name',
                '10.0.0.1': 'IP Address',
                'GeneratedFindingPublicDNSName': 'DNS Name',
                'GeneratedFindingAccessKeyId': 'AWS IAM Access Key ID',
                '198.51.100.0': 'IP Address',
                'GeneratedFindingUserName': 'AWS IAM User Name',
                'GeneratedFindingPrivateDnsName': 'DNS Name'
        }),
        "find_resilient_artifacts_for_incident_no_artifacts": (
            {}
        ),
        "page_incidents": (
            {'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.', 'description': '<div>An API was used to access a bucket from an IP address on a custom threat list.</div>', 'phase_id': 1009, 'inc_training': False, 'vers': 2, 'addr': None, 'city': None, 'creator': {'id': 4, 'fname': 'Resilient', 'lname': 'Sysadmin', 'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@a.com', 'locked': False, 'password_changed': False, 'is_external': False}, 'creator_principal': {'id': 4, 'type': 'user', 'name': 'a@a.com', 'display_name': 'Resilient Sysadmin'}, 'exposure_type_id': 1, 'incident_type_ids': [], 'reporter': None, 'state': None, 'country': None, 'zip': None, 'workspace': 2, 'exposure': 0, 'org_handle': 202, 'members': [], 'negative_pr_likely': None, 'perms': {'read': True, 'write': True, 'comment': True, 'assign': True, 'close': True, 'change_members': True, 'attach_file': True, 'read_attachments': True, 'delete_attachments': True, 'create_milestones': True, 'list_milestones': True, 'create_artifacts': True, 'list_artifacts': True, 'delete': True, 'change_workspace': True}, 'confirmed': False, 'task_changes': {'added': [], 'removed': []}, 'assessment': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n', 'data_compromised': None, 'draft': False, 'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631', 'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631', 'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z', 'aws_guardduty_count': '4', 'internal_customizations_field': None, 'aws_guardduty_archived': 'False', 'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom', 'aws_guardduty_resource_type': 'S3Bucket', 'aws_guardduty_severity': '2', 'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a', 'aws_guardduty_region': 'us-west-2'}, 'resolution_id': None, 'resolution_summary': None, 'pii': {'data_compromised': None, 'determined_date': 1606311997960, 'harmstatus_id': 2, 'data_encrypted': None, 'data_contained': None, 'impact_likely': None, 'ny_impact_likely': None, 'or_impact_likely': None, 'wa_impact_likely': None, 'dc_impact_likely': None, 'data_source_ids': [], 'data_format': None, 'assessment': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n', 'exposure': 0, 'gdpr_harm_risk': None, 'gdpr_lawful_data_processing_categories': [], 'alberta_health_risk_assessment': None}, 'gdpr': {'gdpr_breach_circumstances': [], 'gdpr_breach_type': None, 'gdpr_personal_data': None, 'gdpr_identification': None, 'gdpr_consequences': None, 'gdpr_final_assessment': None, 'gdpr_breach_type_comment': None, 'gdpr_personal_data_comment': None, 'gdpr_identification_comment': None, 'gdpr_consequences_comment': None, 'gdpr_final_assessment_comment': None, 'gdpr_subsequent_notification': None}, 'regulator_risk': {}, 'inc_last_modified_date': 1612532328297, 'admin_id': None, 'creator_id': 4, 'crimestatus_id': 1, 'employee_involved': None, 'end_date': None, 'exposure_dept_id': None, 'exposure_individual_name': None, 'exposure_vendor_id': None, 'jurisdiction_name': None, 'jurisdiction_reg_id': None, 'start_date': None, 'inc_start': None, 'org_id': 202, 'is_scenario': False, 'hard_liability': 0, 'nist_attack_vectors': [], 'id': 2100, 'sequence_code': '5908-6', 'discovered_date': 1606311997960, 'due_date': None, 'create_date': 1612532324833, 'owner_id': 4, 'severity_code': 100, 'plan_status': 'A'}
        )
    }
    return response[op]

# Mocked function parameters.
def get_function_params(op):
    response = {
        "data": (
            {
                'name': 'AWS GuardDuty: API GeneratedFindingAPIName was invoked from an IP address on a custom threat list.',
                'description': {'format': 'text',
                                'content': 'An API was used to access a bucket from an IP address on a custom threat list.'},
                'discovered_date': '2020-11-25T13:46:37.960Z', 'severity_code': 'Low',
                'properties': {'aws_guardduty_finding_id': '60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',
                               'aws_guardduty_finding_type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',
                               'aws_guardduty_finding_updated_at': '2020-11-26T15:18:12.620Z',
                               'aws_guardduty_region': 'us-west-2', 'aws_guardduty_resource_type': 'S3Bucket',
                               'aws_guardduty_count': '4',
                               'aws_guardduty_detector_id': 'f2baedb0ac74f8f42fc929e15f56da6a'},
                'artifacts': [
                {'type': {'name': 'aws_iam_access_key_id'}, 'description': {'format': 'text',
                                                                            'content': "'AWS IAM Access Key ID' extracted from GuardDuty from finding property 'AccessKeyId' at path '['Resource', 'AccessKeyDetails']'."},
                 'value': 'GeneratedFindingAccessKeyId'}, {'type': {'name': 'aws_iam_user_name'},
                                                           'description': {'format': 'text',
                                                                           'content': "'AWS IAM User Name' extracted from GuardDuty from finding property 'UserName' at path '['Resource', 'AccessKeyDetails']'."},
                                                           'value': 'GeneratedFindingUserName'},
                {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                 'content': "'IP Address' extracted from GuardDuty from finding property 'IpAddressV4' at path '['Service', 'Action', 'AwsApiCallAction', 'RemoteIpDetails']'."},
                 'value': '198.51.100.0'}, {'type': {'name': 'IP Address'}, 'description': {'format': 'text',
                                                                                            'content': "'IP Address' extracted from GuardDuty from finding property 'PrivateIpAddress' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                            'value': '10.0.0.1'}, {'type': {'name': 'DNS Name'},
                                                                   'description': {'format': 'text',
                                                                                   'content': "'DNS Name' extracted from GuardDuty from finding property 'PublicDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                                                                   'value': 'GeneratedFindingPublicDNSName'},
                {'type': {'name': 'DNS Name'}, 'description': {'format': 'text',
                                                               'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0]'."},
                 'value': 'GeneratedFindingPrivateDnsName'}, {'type': {'name': 'DNS Name'},
                                                              'description': {'format': 'text',
                                                                              'content': "'DNS Name' extracted from GuardDuty from finding property 'PrivateDnsName' at path '['Resource', 'InstanceDetails', 'NetworkInterfaces', 0, 'PrivateIpAddresses', 0]'."},
                                                              'value': 'GeneratedFindingPrivateName'}], 'comments': [{
                                                                                                                         'text': {
                                                                                                                             'format': 'text',
                                                                                                                             'content': "AWS GuardDuty finding Payload:\n{   'AccountId': '834299573936',\n    'Arn': 'arn:aws:guardduty:us-west-2:834299573936:detector/f2baedb0ac74f8f42fc929e15f56da6a/finding/60baffd3f9042e38640f2300d5c5a631',\n    'CreatedAt': '2020-11-25T13:46:37.960Z',\n    'Description': 'An API was used to access a bucket from an IP address on a '\n                   'custom threat list.',\n    'Id': '60baffd3f9042e38640f2300d5c5a631',\n    'Partition': 'aws',\n    'Region': 'us-west-2',\n    'Resource': {   'AccessKeyDetails': {   'AccessKeyId': 'GeneratedFindingAccessKeyId',\n                                            'PrincipalId': 'GeneratedFindingPrincipalId',\n                                            'UserName': 'GeneratedFindingUserName',\n                                            'UserType': 'IAMUser'},\n                    'InstanceDetails': {   'AvailabilityZone': 'GeneratedFindingInstaceAvailabilityZone',\n                                           'IamInstanceProfile': {   'Arn': 'arn:aws:iam::834299573936:example/instance/profile',\n                                                                     'Id': 'GeneratedFindingInstanceProfileId'},\n                                           'ImageDescription': 'GeneratedFindingInstaceImageDescription',\n                                           'ImageId': 'ami-99999999',\n                                           'InstanceId': 'i-99999999',\n                                           'InstanceState': 'running',\n                                           'InstanceType': 'm3.xlarge',\n                                           'LaunchTime': '2016-08-02T02:05:06Z',\n                                           'NetworkInterfaces': [   {   'Ipv6Addresses': [   ],\n                                                                        'NetworkInterfaceId': 'eni-bfcffe88',\n                                                                        'PrivateDnsName': 'GeneratedFindingPrivateDnsName',\n                                                                        'PrivateIpAddress': '10.0.0.1',\n                                                                        'PrivateIpAddresses': [   {   'PrivateDnsName': 'GeneratedFindingPrivateName',\n                                                                                                      'PrivateIpAddress': '10.0.0.1'}],\n                                                                        'PublicDnsName': 'GeneratedFindingPublicDNSName',\n                                                                        'PublicIp': '198.51.100.0',\n                                                                        'SecurityGroups': [   {   'GroupId': 'GeneratedFindingSecurityId',\n                                                                                                  'GroupName': 'GeneratedFindingSecurityGroupName'}],\n                                                                        'SubnetId': 'GeneratedFindingSubnetId',\n                                                                        'VpcId': 'GeneratedFindingVPCId'}],\n                                           'OutpostArn': 'arn:aws:outposts:us-west-2:123456789000:outpost/op-0fbc006e9abbc73c3',\n                                           'ProductCodes': [{}],\n                                           'Tags': [   {   'Key': 'GeneratedFindingInstaceTag1',\n                                                           'Value': 'GeneratedFindingInstaceValue1'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag2',\n                                                           'Value': 'GeneratedFindingInstaceTagValue2'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag3',\n                                                           'Value': 'GeneratedFindingInstaceTagValue3'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag4',\n                                                           'Value': 'GeneratedFindingInstaceTagValue4'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag5',\n                                                           'Value': 'GeneratedFindingInstaceTagValue5'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag6',\n                                                           'Value': 'GeneratedFindingInstaceTagValue6'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag7',\n                                                           'Value': 'GeneratedFindingInstaceTagValue7'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag8',\n                                                           'Value': 'GeneratedFindingInstaceTagValue8'},\n                                                       {   'Key': 'GeneratedFindingInstaceTag9',\n                                                           'Value': 'GeneratedFindingInstaceTagValue9'}]},\n                    'ResourceType': 'S3Bucket',\n                    'S3BucketDetails': [   {   'Arn': 'arn:aws:s3:::bucketName',\n                                               'CreatedAt': datetime.datetime(2017, 12, 18, 15, 58, 11, 551000, tzinfo=tzlocal()),\n                                               'DefaultServerSideEncryption': {   'EncryptionType': 'SSEAlgorithm',\n                                                                                  'KmsMasterKeyArn': 'arn:aws:kms:region:123456789012:key/key-id'},\n                                               'Name': 'bucketName',\n                                               'Owner': {   'Id': 'CanonicalId '\n                                                                  'of Owner'},\n                                               'PublicAccess': {   'EffectivePermission': 'NOT_PUBLIC',\n                                                                   'PermissionConfiguration': {   'AccountLevelPermissions': {   'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                          'BlockPublicPolicy': False,\n                                                                                                                                                          'IgnorePublicAcls': False,\n                                                                                                                                                          'RestrictPublicBuckets': False}},\n                                                                                                  'BucketLevelPermissions': {   'AccessControlList': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                         'AllowsPublicWriteAccess': False},\n                                                                                                                                'BlockPublicAccess': {   'BlockPublicAcls': False,\n                                                                                                                                                         'BlockPublicPolicy': False,\n                                                                                                                                                         'IgnorePublicAcls': False,\n                                                                                                                                                         'RestrictPublicBuckets': False},\n                                                                                                                                'BucketPolicy': {   'AllowsPublicReadAccess': False,\n                                                                                                                                                    'AllowsPublicWriteAccess': False}}}},\n                                               'Tags': [   {   'Key': 'foo',\n                                                               'Value': 'bar'}],\n                                               'Type': 'Destination'}]},\n    'SchemaVersion': '2.0',\n    'Service': {   'Action': {   'ActionType': 'AWS_API_CALL',\n                                 'AwsApiCallAction': {   'Api': 'GeneratedFindingAPIName',\n                                                         'CallerType': 'Remote '\n                                                                       'IP',\n                                                         'RemoteIpDetails': {   'City': {   'CityName': 'GeneratedFindingCityName'},\n                                                                                'Country': {   'CountryName': 'GeneratedFindingCountryName'},\n                                                                                'GeoLocation': {   'Lat': 0,\n                                                                                                   'Lon': 0},\n                                                                                'IpAddressV4': '198.51.100.0',\n                                                                                'Organization': {   'Asn': '-1',\n                                                                                                    'AsnOrg': 'GeneratedFindingASNOrg',\n                                                                                                    'Isp': 'GeneratedFindingISP',\n                                                                                                    'Org': 'GeneratedFindingORG'}},\n                                                         'ServiceName': 'GeneratedFindingAPIServiceName'}},\n                   'Archived': False,\n                   'Count': 4,\n                   'DetectorId': 'f2baedb0ac74f8f42fc929e15f56da6a',\n                   'EventFirstSeen': '2020-11-25T13:46:37.960Z',\n                   'EventLastSeen': '2020-11-26T15:18:12.620Z',\n                   'ResourceRole': 'TARGET',\n                   'ServiceName': 'guardduty'},\n    'Severity': 2,\n    'Title': 'API GeneratedFindingAPIName was invoked from an IP address on a '\n             'custom threat list.',\n    'Type': 'UnauthorizedAccess:S3/MaliciousIPCaller.Custom',\n    'UpdatedAt': '2020-11-26T15:18:12.620Z'}"}}]}
        ),
        "tables": (
            {'gd_action_details': [{'cells': {'action_type': {'value': 'AWS_API_CALL'},
                                              'action_api': {'value': 'GeneratedFindingAPIName'},
                                              'event_first_seen': {'value': '2020-11-25T13:46:37.960Z'},
                                              'event_last_seen': {'value': '2020-11-26T15:18:12.620Z'},
                                              'actor_caller_type': {'value': 'Remote IP'},
                                              'city_name': {'value': 'GeneratedFindingCityName'},
                                              'country_name': {'value': 'GeneratedFindingCountryName'},
                                              'asn': {'value': '-1'}, 'asn_org': {'value': 'GeneratedFindingASNOrg'},
                                              'isp': {'value': 'GeneratedFindingISP'},
                                              'org': {'value': 'GeneratedFindingORG'},
                                              'action_service_name': {'value': 'GeneratedFindingAPIServiceName'},
                                              'remote_ip': {'value': '198.51.100.0'}}}],
             'gd_resource_affected': [{'cells': {'resource_type': {'value': 'S3Bucket'},
                                                 'instance_id': {'value': 'i-99999999'},
                                                 'instance_type': {'value': 'm3.xlarge'},
                                                 'instance_state': {'value': 'running'},
                                                 'resource_role': {'value': 'TARGET'},
                                                 'instance_private_ip': {'value': '10.0.0.1'},
                                                 'instance_private_dns': {'value': 'GeneratedFindingPrivateName'},
                                                 'instance_public_ip': {'value': '198.51.100.0'},
                                                 'instance_public_dns': {'value': 'GeneratedFindingPublicDNSName'},
                                                 's3bucket_name': {'value': 'bucketName'},
                                                 's3bucket_owner': {'value': 'CanonicalId of Owner'}
                                                 }
                                       }
                                      ]
             }
        )
    }
    return response[op]

# Mocked GuardDuty AWS client response for standalone tests.
def mocked_aws(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace gd client in circuits tests"""
        def __init__(self, *args, **kwargs):
            self.exceptions = {}

        def get_findings(self):
            return get_cli_raw_responses("get_findings")

        def __init__(self, *args, **kwargs):
            self.exceptions = {}

        def can_paginate(self, op):
            if  op in ["list_findings", "list_detectors"]:
                return True
            else:
                return False

        def archive_findings(self):
            return get_cli_raw_responses("archive_findings")

    return MockResponse(args, **kwargs)


# Mocked paginate class for standalone tests.
class Paginate(object):

    def __init__(self, op):
        #op = op + "_paginated"
        self.responses = [get_cli_raw_responses(op)]
        self.index = 0

    def __iter__(self):
        for response in self.responses:
            yield response

# Mocked paginator response for standalone tests.
def mocked_client_paginator(*args, **kwargs):
    class MockPaginate:
        """Class will be used by the mock to replace paginator in circuits tests"""
        def __init__(self, *args, **kwargs):
           self.op = args[0][0]

        def paginate(self):
            return Paginate(self.op)

    return MockPaginate(args, **kwargs)


def mocked_gd_client(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace amp_client in circuits tests"""
        def __init__(self, *args, **kwargs):
            pass

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get(self, op=None, paginate=False, **kwargs):
            if op == "describe_regions":
                return get_cli_raw_responses("describe_regions")["Regions"]
            if op == "list_detectors":
                return get_cli_raw_responses("list_detectors")["DetectorIds"]
            if op == "list_findings":
                return get_cli_raw_responses("list_findings")["FindingIds"]
            if op == "get_findings":
                if "60baffd3f9042e38640f2300d5c5a630" in kwargs["FindingIds"]:
                    return []
                else:
                    return get_cli_raw_responses("get_findings")["Findings"]

        def post(self, op, **kwargs):
            if op == "archive_findings":
                if "32b7017d2019dfe922abc4e07c3fdfff" in kwargs["DetectorId"]:
                    return {"status": "error",
                            "msg": "An error occurred (BadRequestException) when calling the ArchiveFindings operation: "
                                   "The request is rejected because the input detectorId is not owned by the current account."}
                else:
                    return{"status": "ok"}

    return MockResponse(*args, **kwargs)

def mocked_ResSvc(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace AWS GuardDuty resilient_service in circuits tests"""
        def __init__(self, *args, **kwargs):
            pass

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def find_resilient_incident_for_req(self, finding, f_fields):
            return get_resilient_responses("find_resilient_incident_for_req")
        def create_incident(self, finding, f_fields):
            return get_resilient_responses("create_incident")
        def add_datatables(self, i_payload):
            return
        def find_resilient_artifacts_for_incident(self, incident_id):
            if  incident_id == 1:
                return get_resilient_responses("find_resilient_artifacts_for_incident_with_artifacts")
            else:
                return get_resilient_responses("find_resilient_artifacts_for_incident_no_artifacts")
        def add_comment(self, incident_id, note):
            return

        def page_incidents(self, region=None, f_fields=None):
            yield get_resilient_responses("page_incidents")

    return MockResponse(*args, **kwargs)

def get_mock_config():
    config_data = u"""[fn_aws_guardduty]
aws_gd_access_key_id=AKAABBCCDDEEFFGGHH12
aws_gd_secret_access_key=pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss
aws_gd_master_region="us-west-2"
aws_gd_regions=".*"
aws_gd_regions_interval=2
aws_gd_polling_interval=1
aws_gd_severity_threshold = 7
aws_gd_lookback_interval=60
#http_proxy=http://proxy:80
#https_proxy=http://proxy:443
"""
    return config_data