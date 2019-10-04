# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate Mock responses to simulate Proofpoint TRAP for Unit and function tests """
import re
import json
from sys import version_info
from requests import HTTPError
from requests.models import Response
import datetime

# Responses for standalone tests


def get_list_members():

    response =  [{'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'IP to block', 'enabled': True,
                  'expiration': '2018-12-18T19:08:56Z', 'hash_reputation_id': 123,
                  'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '75.76.13.144', 'id': 20, 'resolution_state': 4, 'ttl': 0,
                           'updated_at': '2017-01-11T03:47:15Z'}, 'host_id': 20, 'id': 8, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2017-01-11T03:47:15Z', 'user_id': None},
                 {'created_at': '2018-01-11T03:43:54Z', 'deleted': False, 'description': 'Hostname to block', 'enabled': True,
                  'expiration': "2018-12-19T19:08:56Z", 'hash_reputation_id': None,
                  'host': {'created_at': '2017-12-29T04:56:13Z', 'host': 'tapdemo.evilscheme.info', 'id': 6, 'resolution_state': 4,
                           'ttl': 0,
                           'updated_at': '2018-01-13T00:45:16Z'}, 'host_id': 6, 'id': 7, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2018-01-11T03:43:54Z', 'user_id': None},
                 {'created_at': '2017-01-11T03:43:54Z', 'deleted': False, 'description': 'test', 'enabled': True,
                  'expiration': '2018-12-20T19:08:56Z', 'hash_reputation_id': None,
                  'host': {'created_at': '2016-12-29T04:56:13Z', 'host': 'string', 'id': 6, 'resolution_state': 4, 'ttl': 0,
                           'updated_at': '2017-01-13T00:45:16Z'}, 'host_id': 6, 'id': 6, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2017-01-11T03:43:54Z', 'user_id': None},
                 {'created_at': '2017-01-11T03:43:54Z', 'deleted': False, 'description': 'Unicode test ɡɢɣɤɥɦ', 'enabled': True,
                  'expiration': "2018-12-22T19:08:56Z", 'hash_reputation_id': None,
                  'host': {'created_at': '2016-12-29T04:56:13Z', 'host': 'ɡɢɣɤɥɦ', 'id': 6, 'resolution_state': 4, 'ttl': 0,
                           'updated_at': '2017-01-13T00:45:16Z'}, 'host_id': 6, 'id': 6, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2017-01-11T03:43:54Z', 'user_id': None}]
    return response

def add_list_member():

    response =  {'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'Test Description', 'enabled':True,
                 'expiration': '2019-09-29T23:00:00Z', 'hash_reputation_id': None,
                 'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '192.168.1.2', 'id': 20, 'resolution_state': 4, 'ttl': 5,
                          'updated_at': '2019-09-25T14:07:46Z'}, 'host_id': 22, 'id': 8, 'list_id': 1, 'response_id': None,
                 'reverse_user_id': None, 'updated_at': '2019-09-25T14:07:46Z', 'user_id': None
                }
    return response

def update_list_member():

    response =  {'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'Updated description', 'enabled': True,
                 'expiration': '2019-09-29T23:00:00Z', 'hash_reputation_id': None,
                 'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '192.168.1.2', 'id': 20, 'resolution_state': 4, 'ttl': 6,
                          'updated_at': '2019-09-25T14:17:17Z'}, 'host_id': 20, 'id': 8, 'list_id': 1, 'response_id': None,
                 'reverse_user_id': None, 'updated_at': '2019-09-25T14:17:17Z', 'user_id': None
                }
    return response

def get_incident_details():

    response =  {"assignee":"Unassigned","created_at":"2018-05-26T21:07:17Z","description":"EvilScheme test message",
                 "event_count":3,"event_sources":["Proofpoint TAP"],
                 "events":[{"attackDirection":"inbound","category":"malware","classified":False,
                            "description":"Infection.PDF.File.Exploit.CVE-2010-0188_LibTIFF.","id":3,
                            "malwareName":"Infection.PDF.File.Exploit.CVE-2010-0188_LibTIFF.",
                            "received":"2018-05-26T21:07:17Z","severity":"Info","source":"Proofpoint TAP",
                            "state":"Linked","threatname":"Infection.PDF.File.Exploit.CVE-2010-0188_LibTIFF."
                            },
                           {"attackDirection":"inbound","category":"spam","classified":False,"id":1,
                            "received":"2018-05-26T21:07:17Z","severity":"Critical","source":"Proofpoint TAP",
                            "state":"Linked","threatname":"Unsolicited Bulk Email"},
                           {"attackDirection":"inbound","category":"spam","classified":False,"id":2,
                            "received":"2018-05-26T21:07:17Z","severity":"Critical","source":"Proofpoint TAP",
                            "state":"Linked","threatname":"Unsolicited Bulk Email"}],"failed_quarantines":0,
                 "hosts":{"attacker":["54.214.13.31","http://tapdemo.evilscheme.org/files/313532373336373133382e33.pdf"],
                          "forensics":["http://tapdemo.evilscheme.org/files/313532373336373133382e33.pdf","tapdemo.evilscheme.org"]
                         },
                 "id":3,
                 "incident_field_values":[{"name":"Attack Vector","value":"Email"},
                                          {"name":"Classification","value":"Spam"},
                                          {"name":"Severity","value":"Critical"}
                                          ],"pending_quarantines":0,
                 "quarantine_results":[],"score":4200,"state":"Open","successful_quarantines":0,
                 "summary":"Unsolicited Bulk Email","team":"Unassigned","type":"Malware","users":["nbadguy"]
                 }


    return response

def delete_list_member():

    response = "OK"
    return response

def mocked_pptr_client(*args):

    class MockResponse:
        """Class will be used by the mock to replace pptr_client in circuits tests"""
        def __init__(self, *arg):
            self.r = Response()

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get_list_members(self, list_id=None, member_id=None, members_type=None):
            return get_list_members()

        def add_list_member(self, list_id=None, member=None, description=None, expiration=None, duration=None):
            return add_list_member()

        def update_list_member(self, list_id=None, member_id=None, description=None, expiration=None, duration=None):
            return update_list_member()

        def delete_list_member(self, list_id=None, member_id=None):
            return delete_list_member()

        def get_incident_details(self, incident_id=None):
            return {
                "href": "https://traptesthost/incidents/{}.json".format(incident_id),
                "data": get_incident_details()
            }
    return MockResponse(*args)

def mocked_request(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace RequestsCommon in pptr_client tests"""
        def __init__(self, *arg, **kwargs):
            pass

        def get_proxies(self):
            proxies = None
            return proxies

        def execute_call_v2(self, *args, **kwargs):
            if args[0].lower() == "get":
                if re.match("^https://traptesthost/lists/1/members.json", args[1]):
                    return MockGetResponse(json.dumps(get_list_members()), None, 200)
                elif re.match("^https://traptesthost/incidents/123.json", args[1]):
                    return MockGetResponse(json.dumps(get_incident_details()), None, 200)
            elif args[0].lower() == "post":
                if re.match("^https://traptesthost/lists/1/members.json$", args[1]):
                    return MockGetResponse(json.dumps(add_list_member()), None, 200)
            elif args[0].lower() == "delete":
                if re.match("^https://traptesthost/lists/1/members/8.json", args[1]):
                    return MockGetResponse(json.dumps(delete_list_member()), None, 200)
            elif args[0].lower() == "put":
                if re.match("^https://traptesthost/lists/1/members/192.168.1.2.json", args[1]):
                    return MockGetResponse(json.dumps(update_list_member()), None, 200)

        def __getitem__(self, key):
            return getattr(self, key)

    return MockSession(*args, **kwargs)

class MockGetResponse:
    """Class will be used by the mock to replace response for RequestsCommon in pptr_client tests"""
    def __init__(self, *args, **kwargs):
        self.headers = {}
        self.r = Response()
        if args[0]:
            self.content = self.r._content = args[0].encode()
        self.status_code = args[2]
        self.r.status_code = args[2]

    def json(self):
        res = self.r.json()
        pass
        return self.r.json()

    def __getitem__(self, key):
        return getattr(self, key)

def get_mock_config():
    config_data = u"""[fn_proofpoint_trap]
base_url=https://traptesthost
api_key=abcd1234-a123-123a-123a-123456abcdef
polling_interval=2
startup_interval=20160
state=open
host_categories=attacker,cnc,forensics,url
"""
    return config_data
