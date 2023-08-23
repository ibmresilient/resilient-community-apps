# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate AWS IAM for Unit and function tests """
import re
import json
import datetime
from dateutil.tz import tzutc

# Mocked IAM RAW Responses for standalone tests.
def get_cli_raw_responses(op):
    response = {
        "get_user": (
            {u'User': {u'UserName': 'iam_test_User_1', u'Tags': [{u'Value': 'A test TAG', u'Key': 'Test_tag1'},
                                                                        {u'Value': 'Another test tag',
                                                                         u'Key': 'Tes Tag2'}],
                       u'PasswordLastUsed': datetime.datetime(2019, 11, 15, 17, 11, 28, tzinfo=tzutc()),
                       u'CreateDate': datetime.datetime(2019, 11, 5, 15, 54, 43, tzinfo=tzutc()),
                       u'UserId': 'AIDA4EQBBG2YGZOQXT2JB', u'Path': '/',
                       u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_1'},
             'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200,
                                  'RequestId': '9af69169-8050-469a-a9c8-bceaab643067',
                                  'HTTPHeaders': {'x-amzn-requestid': '9af69169-8050-469a-a9c8-bceaab643067',
                                                  'date': 'Fri, 13 Dec 2019 11:45:37 GMT', 'content-length': '793',
                                                  'content-type': 'text/xml'}}}

        ),
        "list_users_paginated":([{u'Marker': 'ACyw2PAMHCYgoAcDyZG4reye+85RexJ2qrg663e67SoI9///8iWhpujLGUMOqiDNLzm3vbhb97fUygGS0XEZ0xjv',
                                 u'Users': [{u'UserName': 'iam_test_User_1',
                                             u'PasswordLastUsed': datetime.datetime(2019, 11, 15, 17, 11, 28, tzinfo=tzutc()),
                                             u'CreateDate': datetime.datetime(2019, 11, 5, 15, 54, 43, tzinfo=tzutc()),
                                             u'UserId': 'AIDA4EQBBG2YDOLTU6QSA', u'Path': '/',
                                             u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_1'},
                                            {u'UserName': 'iam_test_User_2', u'Path': '/',
                                             u'CreateDate': datetime.datetime(2019, 11, 18, 18, 11, 33, tzinfo=tzutc()),
                                             u'UserId': 'AIDA4EQBBG2YDOLTU6QSB',
                                             u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_2'}],
                                 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200,
                                                      'RequestId': '013d16e4-2df8-4e84-b798-198c096e4e16',
                                                      'HTTPHeaders': {'x-amzn-requestid': '013d16e4-2df8-4e84-b798-198c096e4e16',
                                                                      'date': 'Fri, 13 Dec 2019 11:05:52 GMT', 'content-length': '1892',
                                                                      'content-type': 'text/xml'}}, u'IsTruncated': True},
                                 {u'Users': [{u'UserName': 'iam_test_User_3', u'Path': '/',
                                              u'CreateDate': datetime.datetime(2019, 11, 18, 18, 11, 34, tzinfo=tzutc()),
                                              u'UserId': 'AIDA4EQBBG2YDOLTU6QSC',
                                              u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_3'},
                                             {u'UserName': 'iam_test_User_4',
                                              u'PasswordLastUsed': datetime.datetime(2019, 12, 10, 17, 10, 40, tzinfo=tzutc()),
                                              u'CreateDate': datetime.datetime(2019, 10, 31, 16, 23, 7, tzinfo=tzutc()),
                                              u'UserId': 'AIDA4EQBBG2YDOLTU6QSD', u'Path': '/',
                                              u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_4'}],
                                  'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200,
                                                       'RequestId': '4b16f25c-43a1-42da-ba1c-406697f0d509',
                                                       'HTTPHeaders': {'x-amzn-requestid': '4b16f25c-43a1-42da-ba1c-406697f0d509',
                                                                       'date': 'Fri, 13 Dec 2019 11:07:44 GMT', 'content-length': '1787',
                                                                       'content-type': 'text/xml'}}, u'IsTruncated': False}]
                                                   ),
        "list_user_tags": ({'Tags': [], 'IsTruncated': False,
                            'ResponseMetadata': {'RequestId': '9fe8ca2a-b5f7-4e42-b4f6-0200675aae9a', 'HTTPStatusCode': 200,
                                                 'HTTPHeaders': {'x-amzn-requestid': '9fe8ca2a-b5f7-4e42-b4f6-0200675aae9a',
                                                                 'content-type': 'text/xml', 'content-length': '300',
                                                                 'date': 'Fri, 06 Dec 2019 16:33:02 GMT'}, 'RetryAttempts': 0}}
                          ),
        "get_login_profile": ({'LoginProfile': {'UserName': 'iam_test_User_1',
                                                'CreateDate': datetime.datetime(2019, 10, 31, 16, 23, 8, tzinfo=tzutc()),
                                                'PasswordResetRequired': False},
                               'ResponseMetadata': {'RequestId': 'e40479f4-7ffb-42bb-8964-4a8bcae352eb',
                                                    'HTTPStatusCode': 200,
                                                    'HTTPHeaders': {'x-amzn-requestid': 'e40479f4-7ffb-42bb-8964-4a8bcae352eb',
                                                                    'content-type': 'text/xml', 'content-length': '453',
                                                                    'date': 'Fri, 06 Dec 2019 17:26:12 GMT'},
                                                    'RetryAttempts': 0
                                                    }
                               }),
        "get_login_profile_1": ({'LoginProfile': {'UserName': 'iam_test_User_3',
                                                  'CreateDate': datetime.datetime(2019, 10, 31, 16, 23, 8,
                                                                                  tzinfo=tzutc()),
                                                  'PasswordResetRequired': False},
                                 'ResponseMetadata': {'RequestId': 'e40479f4-7ffb-42bb-8964-4a8bcae352eb',
                                                      'HTTPStatusCode': 200,
                                                      'HTTPHeaders': {
                                                          'x-amzn-requestid': 'e40479f4-7ffb-42bb-8964-4a8bcae352eb',
                                                          'content-type': 'text/xml', 'content-length': '453',
                                                          'date': 'Fri, 06 Dec 2019 17:26:12 GMT'},
                                                      'RetryAttempts': 0
                                                      }
                                 }),
        "policies": ({'AttachedPolicies': [], 'IsTruncated': False,
                      'ResponseMetadata': {'RequestId': '5e7be591-2cbc-43c1-854a-a94df91c86d2',
                                           'HTTPStatusCode': 200,
                                           'HTTPHeaders': {'x-amzn-requestid': '5e7be591-2cbc-43c1-854a-a94df91c86d2',
                                                           'content-type': 'text/xml', 'content-length': '360',
                                                           'date': 'Fri, 06 Dec 2019 16:26:56 GMT'}, 'RetryAttempts': 0
                                           }
                      }),
        "list_user_policies": ({'PolicyNames': [], 'IsTruncated': False,
                                'ResponseMetadata': {'RequestId': 'fa5b7656-1d2a-45e6-b72a-ea7f6efe5d94',
                                                     'HTTPStatusCode': 200,
                                                     'HTTPHeaders': {
                                                         'x-amzn-requestid': 'fa5b7656-1d2a-45e6-b72a-ea7f6efe5d94',
                                                         'content-type': 'text/xml', 'content-length': '323',
                                                         'date': 'Fri, 06 Dec 2019 16:29:04 GMT'},
                                                     'RetryAttempts': 0
                                                     }
                                }

        ),
        "delete_user": ( {'ResponseMetadata': {'RequestId': 'fa4255b2-67eb-4308-937c-bd7c70a2d0cf',
                                               'HTTPStatusCode': 200,
                                               'HTTPHeaders': {
                                                   'x-amzn-requestid': 'fa4255b2-67eb-4308-937c-bd7c70a2d0cf',
                                                   'content-type': 'text/xml', 'content-length': '200',
                                                   'date': 'Thu, 09 Jan 2020 10:49:57 GMT'},
                                               'RetryAttempts': 0}
                          }
        ),
    }
    return response[op]

## Mock pre-results - Expected results before updates/filters applied.
def mocked_iam_pre_results(type):
    response = {
        "access_keys":([{'UserName': 'iam_test_User_1', 'Status': 'Active',
                               'CreateDate': datetime.datetime(2019, 10, 31, 16, 23, 8, tzinfo=tzutc()),
                               'AccessKeyId': 'AKIA4EQBBG2YO3VWDSN6'},
                              {'UserName': 'iam_test_User_2', 'Status': 'Active',
                               'CreateDate': datetime.datetime(2019, 11, 4, 11, 33, 33, tzinfo=tzutc()),
                               'AccessKeyId': 'AKIA4EQBBG2YP4S4SOEV'}]
        ),
        "groups":([{'Path': '/', 'CreateDate': datetime.datetime(2017, 5, 29, 20, 37, 53, tzinfo=tzutc()),
                    'GroupId': 'AGPAJUCG3BHM64OGVGCBG',
                    'Arn': 'arn:aws:iam::123456789012:group/test-group',
                    'GroupName': 'test-group'}]

        ),
        "get_user": ([{'UserName': 'iam_test_User_2',
                       'Tags': [{'Value': 'test', 'Key': 'Evironment'},
                                {'Value': 'system', 'Key': 'Account_Type'}],
                       'PasswordLastUsed': datetime.datetime(2019, 11, 15, 17, 11, 28, tzinfo=tzutc()),
                       'CreateDate': datetime.datetime(2019, 10, 31, 16, 23, 7, tzinfo=tzutc()),
                       'UserId': 'AIDA4EQBBG2YGZOQXT2JB', 'Path': '/',
                       'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_2'}]
        ),
        "pre_result_add_prop": ([{'UserName': 'iam_test_User_1',
                         'CreateDate': '2019-10-31 16:23:07',
                         'UserId': 'AIDA4EQBBG2YGZOQXT2JA',
                         'Path': '/', 'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_1'}]
        ),
        "pre_result_default_add_prop": ([{'UserName': 'iam_test_User_2',
                                 'Tags': [{'Value': 'test', 'Key': 'Evironment'},
                                          {'Value': 'system', 'Key': 'Account_Type'}],
                                 'PasswordLastUsed': '2019-11-15 17:11:28',
                                 'CreateDate': '2019-10-31 16:23:07',
                                 'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                 'Path': '/', 'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_2'}]
                              ),
        "pre_result_with_profile_add_prop": ([{'UserName': 'iam_test_User_3',
                         'PasswordLastUsed': '2019-11-15 17:11:28',
                         'CreateDate': '2019-10-31 16:23:07',
                         'UserId': 'AIDA4EQBBG2YGZOQXT2JC',
                         'Path': '/', 'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_3'}]
        )
    }
    return response[type]

## Mocked results - Expected results after updates/filters applied.
def mock_client_results(type):

    response = {
        "expected_result_add_prop": ([{'Path': '/', 'UserName': 'iam_test_User_1', 'UserId': 'AIDA4EQBBG2YGZOQXT2JA',
                              'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_1',
                              'CreateDate': '2019-10-31 16:23:07', 'LoginProfileExists': 'No'}]
        ),
        "expected_result_default_add_prop": ([{'UserName': 'iam_test_User_2', 'DefaultUser': 'Yes',
                                      'Tags': [{'Value': 'test', 'Key': 'Evironment'},
                                               {'Value': 'system', 'Key': 'Account_Type'}],
                                      'PasswordLastUsed': '2019-11-15 17:11:28',
                                      'CreateDate': '2019-10-31 16:23:07', 'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                      'LoginProfileExists': 'Yes', 'Path': '/',
                                      'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_2'}]
        ),
        "expected_result_with_profile_add_prop": ([{'Path': '/', 'UserName': 'iam_test_User_3',
                                           'UserId': 'AIDA4EQBBG2YGZOQXT2JC',
                                           'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_3',
                                           'CreateDate': '2019-10-31 16:23:07',
                                           'PasswordLastUsed': '2019-11-15 17:11:28',
                                           'LoginProfileExists': 'Yes'}]
        ),
        "expected_result_upd_group": ([{'Path': '/', 'CreateDate': '2017-05-29 20:37:53',
                                                    'GroupId': 'AGPAJUCG3BHM64OGVGCBG',
                                                    'Arn': 'arn:aws:iam::123456789012:group/test-group',
                                                    'GroupName': 'test-group'}]
        ),
        "expected_result_upd_keys": ([{'UserName': 'iam_test_User_1', 'Status': 'Active',
                                                   'CreateDate': '2019-10-31 16:23:08',
                                                   'AccessKeyId': 'AKIA4EQBBG2YO3VWDSN6'},
                                                  {'UserName': 'iam_test_User_2', 'Status': 'Active',
                                                   'CreateDate': '2019-11-04 11:33:33',
                                                   'AccessKeyId': 'AKIA4EQBBG2YP4S4SOEV'}]

                                    ),
        "expected result_pagination": ([{u'UserName': 'iam_test_User_1', u'PasswordLastUsed': '2019-11-15 17:11:28',
                                         u'CreateDate': '2019-11-05 15:54:43', u'UserId': 'AIDA4EQBBG2YDOLTU6QSA',
                                         'LoginProfileExists': 'No', u'Path': '/',
                                         u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_1'},
                                        {u'UserName': 'iam_test_User_2', 'LoginProfileExists': 'Yes', u'Path': '/',
                                         u'CreateDate': '2019-11-18 18:11:33', u'UserId': 'AIDA4EQBBG2YDOLTU6QSB',
                                         u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_2'},
                                        {u'UserName': 'iam_test_User_3', 'LoginProfileExists': 'Yes', u'Path': '/',
                                         u'CreateDate': '2019-11-18 18:11:34', u'UserId': 'AIDA4EQBBG2YDOLTU6QSC',
                                         u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_3'},
                                        {u'UserName': 'iam_test_User_4', u'PasswordLastUsed': '2019-12-10 17:10:40',
                                         u'CreateDate': '2019-10-31 16:23:07', u'UserId': 'AIDA4EQBBG2YDOLTU6QSD',
                                         'LoginProfileExists': 'No', u'Path': '/',
                                         u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_4'}]
                                      ),
        "expected_result_get": ([{u'UserName': 'iam_test_User_1', 'DefaultUser': 'Yes',
                                 u'Tags': [{u'Key': 'Test_tag1', u'Value': 'A test TAG'},
                                           {u'Key': 'Tes Tag2', u'Value': 'Another test tag'}],
                                 u'PasswordLastUsed': '2019-11-15 17:11:28',
                                 u'CreateDate': '2019-11-05 15:54:43',
                                 u'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                 'LoginProfileExists': 'Yes',
                                 u'Path': '/', u'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_1'}]
                               )

    }
    return response[type]

# Mocked responses for Function tests.
def get_func_responses(op):
    response = {
        "get_user": ([{'Path': '/', 'UserName': 'iam_test_User_1', 'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                         'Arn': 'arn:aws:iam::012345678901:user/iam_test_User_1', 'CreateDate': '2019-10-31 16:23:07',
                         'PasswordLastUsed': '2019-12-10 17:10:40', 'LoginProfileExists': 'Yes', 'DefaultUser': 'Yes'}]
        ),
        "list_users": ([{'Path': '/', 'UserName': 'iam_list_User', 'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                         'Arn': 'arn:aws:iam::012345678901:user/iam_test_User', 'CreateDate': '2019-10-31 16:23:07',
                         'PasswordLastUsed': '2019-12-10 17:10:40', 'LoginProfileExists': 'Yes', 'DefaultUser': 'Yes'},
                        {'Path': '/', 'UserName': 'iam_list_User_1', 'UserId': 'AIDA4EQBBG2YDOLTU6QSM',
                         'Arn': 'arn:aws:iam::012345678901:user/iam_test_User_1', 'CreateDate': '2019-11-05 15:54:43',
                         'PasswordLastUsed': '2019-11-15 17:11:28', 'LoginProfileExists': 'Yes'},
                        {'Path': '/', 'UserName': 'iam_list_User_2', 'UserId': 'AIDA4EQBBG2YAZYSSDGXE',
                         'Arn': 'arn:aws:iam::012345678901:user/iam_test_User_2', 'CreateDate': '2019-11-18 18:11:33',
                         'LoginProfileExists': 'No'},
                        {'Path': '/', 'UserName': 'iam_list_User_3', 'UserId': 'AIDAJJWGAZUIOOUXCUOHA',
                         'Arn': 'arn:aws:iam::012345678901:user/iam_test_User_3', 'CreateDate': '2017-05-29 20:38:09',
                         'LoginProfileExists': 'Yes'}]
                      ),
        "list_users_filtered_by_name_all_types": ([{'AccessKeyIds': [{'AccessKeyId': 'ABC123CDE456FGH789IJ',
                                                            'CreateDate': '2019-10-31 16:23:08',
                                                            'Status': 'Active',
                                                            'UserName': 'iam_test_User_1'},
                                                           {'AccessKeyId': 'BC123CDE456FGH789IJK',
                                                            'CreateDate': '2019-11-04 11:33:33',
                                                            'Status': 'Active',
                                                            'UserName': 'iam_test_User_1'}],
                                          'Arn': 'arn:aws:iam::012345678901:user/iam_test_User_1',
                                          'CreateDate': '2019-10-31 16:23:07',
                                          'DefaultUser': 'Yes',
                                          'Groups': [{'Arn': 'arn:aws:iam::123456789012:group/null_group',
                                                      'CreateDate': '2019-12-04 12:31:47',
                                                      'GroupId': 'AGPA4EQBBG2YAVPJATCNZ',
                                                      'GroupName': 'null_group',
                                                      'Path': '/'},
                                                     {'Arn': 'arn:aws:iam::123456789012:group/denyall_group',
                                                      'CreateDate': '2019-11-29 15:49:34',
                                                      'GroupId': 'AGPA4EQBBG2YPUAIHTA3E',
                                                      'GroupName': 'denyall_group',
                                                      'Path': '/'}],
                                          'LoginProfileExists': 'Yes',
                                          'PasswordLastUsed': '2019-12-10 17:10:40',
                                          'Path': '/',
                                          'Policies': [ {'PolicyName': 'inline_deny_all'},
                                                        {'PolicyArn': 'arn:aws:iam::123456789012:policy/deny_all',
                                                        'PolicyName': 'deny_all'},
                                                       {'PolicyArn': 'arn:aws:iam::aws:policy/AWSDenyAll',
                                                        'PolicyName': 'AWSDenyAll'}],
                                          'Tags': [{'Key': 'Test_tag1', 'Value': 'A test TAG'},
                                                   {'Key': 'Tes Tag2', 'Value': 'Another test tag'}],
                                          'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                          'UserName': 'iam_test_User_1'}]
        ),
        "list_users_filtered_by_group":([{'Arn': 'arn:aws:iam::012345678901:user/iam_test_User',
                                          'CreateDate': '2019-10-31 16:23:07',
                                          'DefaultUser': 'Yes',
                                          'Groups': {'Arn': 'arn:aws:iam::123456789012:group/null_group',
                                                     'CreateDate': '2019-12-04 12:31:47',
                                                     'GroupId': 'AGPA4EQBBG2YAVPJATCNZ',
                                                     'GroupName': 'null_group',
                                                     'Path': '/'},
                                          'LoginProfileExists': 'Yes',
                                          'PasswordLastUsed': '2019-12-10 17:10:40',
                                          'Path': '/',
                                          'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                          'UserName': 'iam_list_User'}]
                                        ),
        "list_users_filtered_by_policy": (  [{'Arn': 'arn:aws:iam::012345678901:user/iam_test_User',
                                              'CreateDate': '2019-10-31 16:23:07',
                                              'DefaultUser': 'Yes',
                                              'LoginProfileExists': 'Yes',
                                              'PasswordLastUsed': '2019-12-10 17:10:40',
                                              'Path': '/',
                                              'Policies': {'PolicyArn': 'arn:aws:iam::123456789012:policy/deny_all',
                                                           'PolicyName': 'deny_all'},
                                              'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                              'UserName': 'iam_list_User'}]
        ),
        "list_users_filtered_by_keys_with_dates": ([{'AccessKeyIds': [{'AccessKeyId': 'ABC123CDE456FGH789IJ',
                                                                    'CreateDate': '2019-10-31 16:23:08',
                                                                    'Status': 'Active',
                                                                    'UserName': 'iam_test_User_1',
                                                                    'key_last_used': {'LastUsedDate': '2020-01-20 12:17:00',
                                                                                      'Region': 'us-east-1',
                                                                                      'ServiceName': 'sts'}},
                                                                   {'AccessKeyId': 'BC123CDE456FGH789IJK',
                                                                    'CreateDate': '2019-11-04 11:33:33',
                                                                    'Status': 'Active',
                                                                    'UserName': 'iam_test_User_1',
                                                                    'key_last_used': {'LastUsedDate': '2020-01-20 12:17:00',
                                                                                      'Region': 'us-east-1',
                                                                                      'ServiceName': 'sts'}}],
                                                  'Arn': 'arn:aws:iam::012345678901:user/iam_test_User',
                                                  'CreateDate': '2019-10-31 16:23:07',
                                                  'DefaultUser': 'Yes',
                                                  'LoginProfileExists': 'Yes',
                                                  'PasswordLastUsed': '2019-12-10 17:10:40',
                                                  'Path': '/',
                                                  'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                                                  'UserName': 'iam_list_User'}]
        ),
        "list_policies": ([{'PolicyName': 'deny_all', 'PolicyId': 'ANPA4EQBBG2YGU5WU75FL',
                            'Arn': 'arn:aws:iam::123456789012:policy/deny_all', 'Path': '/', 'DefaultVersionId': 'v1',
                            'AttachmentCount': 0, 'PermissionsBoundaryUsageCount': 0, 'IsAttachable': True,
                            'CreateDate': '2019-12-04 12:34:33', 'UpdateDate': '2019-12-04 12:34:33'},
                           {'PolicyName': 'test_pol_2', 'PolicyId': 'ANPA4EQBBG2YNU2DAGG5G',
                            'Arn': 'arn:aws:iam::123456789012:policy/test_pol_2', 'Path': '/', 'DefaultVersionId': 'v1',
                            'AttachmentCount': 1, 'PermissionsBoundaryUsageCount': 0, 'IsAttachable': True,
                            'CreateDate': '2019-11-21 11:26:19', 'UpdateDate': '2019-11-21 11:26:19'},
                           {'PolicyName': 'AWSDenyAll', 'PolicyId': 'ANPAZKAPJZG4P43IUQ5E5',
                            'Arn': 'arn:aws:iam::aws:policy/AWSDenyAll', 'Path': '/', 'DefaultVersionId': 'v1',
                            'AttachmentCount': 3, 'PermissionsBoundaryUsageCount': 0, 'IsAttachable': True,
                            'CreateDate': '2019-05-01 22:36:14', 'UpdateDate': '2019-05-01 22:36:14'}]
                         ),
        "list_access_keys": ([{'UserName': 'iam_test_User_1', 'AccessKeyId': 'ABC123CDE456FGH789IJ', 'Status': 'Active',
                               'CreateDate': '2019-10-31 16:23:08'},
                              {'UserName': 'iam_test_User_1', 'AccessKeyId': 'BC123CDE456FGH789IJK', 'Status': 'Active',
                               'CreateDate': '2019-11-04 11:33:33'}]
                            ),
        "list_access_keys_with_klu": ([{'AccessKeyId': 'ABC123CDE456FGH789IJ', 'CreateDate': '2019-10-31 16:23:08',
                                        'Status': 'Active', 'UserName': 'iam_test_User_1',
                                        'key_last_used': {'LastUsedDate': '2020-01-20 12:17:00', 'Region': 'us-east-1',
                                                          'ServiceName': 'sts'
                                                         }
                                       },
                                       {'AccessKeyId': 'BC123CDE456FGH789IJK', 'CreateDate': '2019-11-04 11:33:33',
                                        'Status': 'Active', 'UserName': 'iam_test_User_1',
                                        'key_last_used': {'LastUsedDate': '2020-01-20 12:17:00', 'Region': 'us-east-1',
                                                          'ServiceName': 'sts'
                                                         }
                                       }
                                      ]
        ),
        "list_access_keys_empty": ([]),
        "list_groups_for_user": ([{'Path': '/', 'GroupName': 'null_group', 'GroupId': 'AGPA4EQBBG2YAVPJATCNZ',
                                   'Arn': 'arn:aws:iam::123456789012:group/null_group',
                                   'CreateDate': '2019-12-04 12:31:47'},
                                  {'Path': '/', 'GroupName': 'denyall_group', 'GroupId': 'AGPA4EQBBG2YPUAIHTA3E',
                                   'Arn': 'arn:aws:iam::123456789012:group/denyall_group',
                                   'CreateDate': '2019-11-29 15:49:34'}]
        ),
        "list_groups_for_user_empty": ([]),
        "list_attached_user_policies": ([{'PolicyName': 'deny_all',
                                            'PolicyArn': 'arn:aws:iam::123456789012:policy/deny_all'},
                                           {'PolicyName': 'AWSDenyAll', 'PolicyArn': 'arn:aws:iam::aws:policy/AWSDenyAll'}]
                                       ),
        "list_attached_user_policies_empty": ([]),
        "list_user_policies": ([{'PolicyName': 'inline_deny_all'}]),
        "list_user_policies_empty": (''),
        "list_user_tags": ([{'Key': 'Test_tag1', 'Value': 'A test TAG'},
                            {'Key': 'Tes Tag2', 'Value': 'Another test tag'}]
                          ),
        "list_user_tags_empty": ([]),
        "list_mfa_devices": ([{"UserName": "iam_test_user",
                                 "SerialNumber": "arn:aws:iam::123456789012:mfa/iam_test_user",
                                 "EnableDate": "2015-06-16T22:36:37Z"
                               }]
        ),
        "list_mfa_devices_has_virt": ([{"UserName": "iam_test_user_has_virt",
                                          "SerialNumber": "arn:aws:iam::123456789012:mfa/iam_test_user_has_virt",
                                          "EnableDate": "2015-06-16T22:36:37Z"
                                        }]
        ),
        "list_mfa_devices_nodevs": ([]
        ),
        "list_mfa_devices_nosuch": ({"Status": "NoSuchEntity"}
        ),
        "list_virtual_mfa_devices": ([{"SerialNumber": "arn:aws:iam::123456789012:mfa/iam_test_user_has_virt"}
                                      ]
        ),
        "list_signing_certificates": (
            [{'UserName': 'iam_test_user', 'CertificateId': 'WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD',
              'CertificateBody': '-----BEGIN CERTIFICATE-----MIID...Apg=-----END CERTIFICATE-----',
              'Status': 'Active', 'UploadDate': '2020-02-26 12:25:27'}]
        ),
        "list_signing_certificates_nosuch": ({"Status": "NoSuchEntity"}
        ),
        "list_service_specific_credentials": ([{'UserName': 'iam_test_user', 'Status': 'Active',
                                                'ServiceUserName': 'iam_test_user-at-834299573936',
                                                'CreateDate': '2020-02-25 10:43:24',
                                                'ServiceSpecificCredentialId': 'ACCA4EQBBG2YH6NR76SCQ',
                                                'ServiceName': 'codecommit.amazonaws.com'
                                                }]
        ),
        "list_service_specific_credentials_nosuch": ({"Status": "NoSuchEntity"}
        ),
        "list_ssh_public_keys": ([{'UserName': 'iam_test_user', 'SSHPublicKeyId': 'APKA4EQBBG2YCGOGDY5G',
                                   'Status': 'Active', 'UploadDate': '2020-02-25 11:05:17'
                                   }]
        ),
        "list_ssh_public_keys_nosuch": ({"Status": "NoSuchEntity"}
        ),
        "get_login_profile": (
            {'UserName': 'iam_test_User', 'CreateDate': datetime.datetime(2019, 10, 31, 16, 23, 8, tzinfo=tzutc()),
             'PasswordResetRequired': False}
        ),
        "get_access_key_last_used": ({'LastUsedDate': '2020-01-20 12:17:00', 'ServiceName': 'sts', 'Region': 'us-east-1'}
        ),
        "add_user_to_group_good": ('OK'),
        "add_user_to_group_nosuch":('NoSuchEntity'),
        "attach_user_policy_good": ('OK'),
        "attach_user_policy_nosuch": ('NoSuchEntity'),
        "detach_user_policy_good": ('OK'),
        "detach_user_policy_nosuch": ('NoSuchEntity'),
        "delete_access_key_good": ('OK'),
        "delete_access_key_nosuch": ('NoSuchEntity'),
        "update_access_key_good": ('OK'),
        "update_access_key_nosuch": ('NoSuchEntity'),
        "delete_login_profile_good": ('OK'),
        "delete_login_profile_nosuch": ('NoSuchEntity'),
        "remove_user_from_group": ('OK'),
        "update_login_profile_good": ('OK'),
        "update_login_profile_nosuch": ('NoSuchEntity'),
        "update_login_profile_badpw": ('PasswordPolicyViolation'),
        "delete_user_good": ('OK'),
        "delete_user_nosuch": ('NoSuchEntity'),
        "deactivate_mfa_device_good": ('OK'),
        "deactivate_mfa_device_nosuch": ('NoSuchEntity'),
        "delete_virtual_mfa_device_good": ('OK'),
        "delete_virtual_mfa_device_nosuch": ('NoSuchEntity'),
        "delete_signing_certificate_good": ('OK'),
        "delete_signing_certificate_nosuch": ('NoSuchEntity'),
        "delete_service_specific_credential_good": ('OK'),
        "delete_service_specific_credential_nosuch": ('NoSuchEntity'),
        "delete_ssh_public_key_good": ('OK'),
        "delete_ssh_public_key_nosuch": ('NoSuchEntity')

    }
    return response[op]

# Mocked login profile for standalone tests.
def mocked_client_get_profile(*args, **kwargs):
    def mock_response_get(*args, **kwargs):
        """Class will be used by the mock to replace get profile in circuits tests"""
        if "get_login_profile" in args:
            if "_2" in kwargs["UserName"]:
                return get_cli_raw_responses("get_login_profile")
            elif "_3" in kwargs["UserName"]:
                return get_cli_raw_responses("get_login_profile_1")
            else:
                return False

    return mock_response_get(*args, **kwargs)

# Mocked paginate class for standalone tests.
class Paginate(object):

    def __init__(self, op):
        op = op + "_paginated"
        self.responses = get_cli_raw_responses(op)
        self.index = 0

    def __iter__(self):
        for response in self.responses:
            yield response

# Mocked paginator response for standalone tests.
def mocked_client_paginator(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace paginator in circuits tests in circuits tests"""
        def __init__(self, *args, **kwargs):
           self.op = args[0][0]

        def paginate(self):
            return Paginate(self.op)

    return MockResponse(args, **kwargs)

# Mocked IAM client response for standalone tests.
def mocked_iam(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace iam client in circuits tests"""
        def __init__(self, *args, **kwargs):
            self.exceptions = {}
            self.exceptions["NoSuchEntityException"] = None

        def get_user(self):
            return get_cli_raw_responses("get_user")

        def delete_user(self):
            return get_cli_raw_responses("delete_user")

        def get_login_profile(self, **kwargs):
            return get_cli_raw_responses("get_login_profile")

    return MockResponse(args, **kwargs)

# Mocked default identity raw response for standalone.
def get_default_identity(*args, **kwargs):
    default_identity = {'Account': '012345678901', 'UserId': 'AIDA4EQBBG2YGZOQXT2JB',
                        'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200,
                                             'RequestId': '7103139f-1cd5-11ea-8b40-dfdcff3443b4',
                                             'HTTPHeaders': {'x-amzn-requestid': '7103139f-1cd5-11ea-8b40-dfdcff3443b4',
                                                             'date': 'Thu, 12 Dec 2019 11:49:23 GMT',
                                                             'content-length': '409', 'content-type': 'text/xml'}},
                        'Arn': 'arn:aws:iam::123456789012:user/iam_test_User_2'
                        }
    return default_identity

# Mocked client for Function tests.
def mocked_aws_iam_client(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace amp_client in circuits tests"""
        def __init__(self, *args, **kwargs):
            pass

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get(self, op=None, paginate=False, **kwargs):
            if op == "get_user":
                return get_func_responses("get_user")
            if op == "list_users":
                if "UserName" in kwargs and "iam_test_User_1" == kwargs["UserName"]:
                    return get_func_responses("get_user")
                if "results_filter" in kwargs and "UserName" in kwargs["results_filter"]:
                    if kwargs["results_filter"]["UserName"] == "not_exists":
                        return (0, [])
                    else:
                        return get_func_responses("get_user")
                else:
                    return get_func_responses("list_users")
            if op == "list_policies":
                return get_func_responses("list_policies")
            if op == "list_access_keys":
                if "iam_list_User" in kwargs["UserName"]:
                    if "iam_list_User" == kwargs["UserName"] and "results_filter" in kwargs and "AccessKeyId" \
                            in kwargs["results_filter"] and kwargs["results_filter"]["AccessKeyId"] == "123":
                        return (2, get_func_responses("list_access_keys"))
                    else:
                        return []
                elif "_empty" in kwargs["UserName"]:
                    return get_func_responses("list_access_keys_empty")
                else:
                    return get_func_responses("list_access_keys")
            if op == "get_access_key_last_used":
                return get_func_responses("get_access_key_last_used")
            if op == "list_groups_for_user":
                if "iam_list_User" in kwargs["UserName"]:
                    if "iam_list_User" == kwargs["UserName"] and "results_filter" in kwargs and "GroupName" \
                                in kwargs["results_filter"] and kwargs["results_filter"]["GroupName"] == "null_group":
                        return (1, get_func_responses("list_groups_for_user")[0])
                    else:
                        return []
                elif "_empty" in kwargs["UserName"]:
                    return get_func_responses("list_groups_for_user_empty")
                else:
                    return get_func_responses("list_groups_for_user")
            if op == "list_attached_user_policies":
                if "iam_list_User"  in kwargs["UserName"]:
                    if "iam_list_User" == kwargs["UserName"] and "results_filter" in kwargs and "PolicyName" \
                            in kwargs["results_filter"] and kwargs["results_filter"]["PolicyName"] == "deny_all":
                        return (1, get_func_responses("list_attached_user_policies")[0])
                    else:
                        return []
                elif "_empty" in kwargs["UserName"]:
                    return get_func_responses("list_attached_user_policies_empty")
                else:
                    return get_func_responses("list_attached_user_policies")
            if op == "list_user_policies":
                if "with_inline" in kwargs["UserName"]:
                    return get_func_responses("list_user_policies")
                elif "iam_list_User" in kwargs["UserName"]:
                    return []
                elif "_empty" in kwargs["UserName"]:
                    return get_func_responses("list_user_policies_empty")
                else:
                    return get_func_responses("list_user_policies")
            if op == "list_user_tags":
                if "iam_list_User" in kwargs["UserName"]:
                    return []
                elif "_empty" in kwargs["UserName"]:
                    return get_func_responses("list_user_tags_empty")
                else:
                    return get_func_responses("list_user_tags")

            if op == "get_login_profile":
                return get_func_responses("get_login_profile")
            if op == "list_mfa_devices":
                if  "not_exists" in kwargs["UserName"]:
                    return get_func_responses("list_mfa_devices_nosuch")
                elif "no_devs" in kwargs["UserName"]:
                    return get_func_responses("list_mfa_devices_nodevs")
                elif "has_virt" in kwargs["UserName"]:
                    return get_func_responses("list_mfa_devices_has_virt")
                else:
                    return get_func_responses("list_mfa_devices")
            if op == "list_virtual_mfa_devices":
                return get_func_responses("list_virtual_mfa_devices")
            if op == "list_signing_certificates":
                if "not_exists" in kwargs["UserName"]:
                    return get_func_responses("list_signing_certificates_nosuch")
                else:
                    return get_func_responses("list_signing_certificates")
            if op == "list_service_specific_credentials":
                if "not_exists" in kwargs["UserName"]:
                    return get_func_responses("list_service_specific_credentials_nosuch")
                else:
                    return get_func_responses("list_service_specific_credentials")
            if op == "list_ssh_public_keys":
                if "not_exists" in kwargs["UserName"]:
                    return get_func_responses("list_ssh_public_keys_nosuch")
                else:
                    return get_func_responses("list_ssh_public_keys")

        def post(self, op, **kwargs):
            if op == "add_user_to_group":
                if kwargs["GroupName"] == "denyall_group":
                    return get_func_responses("add_user_to_group_good")
                elif kwargs["GroupName"] == "not_exists":
                    return get_func_responses("add_user_to_group_nosuch")
            elif op == "attach_user_policy":
                if kwargs["PolicyArn"] =='not_exists':
                    return get_func_responses("attach_user_policy_nosuch")
                else:
                    return get_func_responses("attach_user_policy_good")
            elif op == "detach_user_policy":
                if kwargs["PolicyArn"] =='not_exists':
                    return get_func_responses("detach_user_policy_nosuch")
                else:
                    return get_func_responses("detach_user_policy_good")
            elif op == "delete_access_key":
                if "NOSUCH" in kwargs["AccessKeyId"]:
                    return get_func_responses("delete_access_key_nosuch")
                else:
                    return get_func_responses("delete_access_key_good")
            elif op == "update_access_key":
                if "NOSUCH" in kwargs["AccessKeyId"]:
                    return get_func_responses("update_access_key_nosuch")
                else:
                    return get_func_responses("update_access_key_good")
            elif op == "delete_login_profile":
                if kwargs["UserName"] == "iam_test_User_no_profile":
                    return get_func_responses("delete_login_profile_nosuch")
                else:
                    return get_func_responses("delete_login_profile_good")
            elif op == "delete_user":
                if kwargs["UserName"] == "iam_test_User_no_such":
                    return get_func_responses("delete_user_nosuch")
                else:
                    return get_func_responses("delete_user_good")
            if op == "remove_user_from_group":
                return get_func_responses("remove_user_from_group")
            elif op == "update_login_profile":
                if "_good" in kwargs["UserName"]:
                    return get_func_responses("update_login_profile_good")
                elif "_nosuch" in kwargs["UserName"]:
                    return get_func_responses("update_login_profile_nosuch")
                elif "_badpw" in kwargs["UserName"]:
                    return get_func_responses("update_login_profile_badpw")
            elif op == "deactivate_mfa_device":
                if "not_exists" in kwargs["SerialNumber"]:
                    return get_func_responses("deactivate_mfa_device_nosuch")
                else:
                    return get_func_responses("deactivate_mfa_device_good")
            elif op == "delete_virtual_mfa_device":
                if "not_exists" in kwargs["SerialNumber"]:
                    return get_func_responses("delete_virtual_mfa_device_nosuch")
                else:
                    return get_func_responses("delete_virtual_mfa_device_good")
            elif op == "delete_signing_certificate":
                if "not_exists" in kwargs["CertificateId"]:
                    return get_func_responses("delete_signing_certificate_nosuch")
                else:
                    return get_func_responses("delete_signing_certificate_good")
            elif op == "delete_service_specific_credential":
                if "not_exists" in kwargs["ServiceSpecificCredentialId"]:
                    return get_func_responses("delete_service_specific_credential_nosuch")
                else:
                    return get_func_responses("delete_service_specific_credential_good")
            elif op == "delete_ssh_public_key":
                if "not_exists" in kwargs["SSHPublicKeyId"]:
                    return get_func_responses("delete_ssh_public_key_nosuch")
                else:
                    return get_func_responses("delete_ssh_public_key_good")
    return MockResponse(*args, **kwargs)

def get_mock_config():
    config_data = u"""[fn_aws_iam]
aws_iam_access_key_id=AKAABBCCDDEEFFGGHH12
aws_iam_secret_access_key=pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss
# Optional configuration setting to set an AWS IAM region.
#aws_iam_region=None

"""
    return config_data
