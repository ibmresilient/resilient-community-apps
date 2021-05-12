# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate ZIA for Unit and function tests """
from requests.models import Response

def get_mock_config():
    config_data = u"""[fn_zia]
zia_api_base_url = https://ziaserver/api/v1
zia_username = ziauser
zia_password = ziapass
zia_api_key = abCDeFIJkl0M
#http_proxy=http://proxy:80
#https_proxy=http://proxy:80
"""
    return config_data

def blocklist_action_result():
    return {"status": "OK"}

def get_blocklist_urls_result():
    return {
        "blacklistUrls": [
            "badhost.com",
            "192.168.12.2"
        ]
    }


def get_auth_headers():
    return {'Strict-Transport-Security': 'max-age=31622400;includeSubDomains;preload',
            'X-Frame-Options': 'SAMEORIGIN', 'X-Content-Type-Options': 'nosniff',
            'X-XSS-Protection': '1; mode=block',
            'Set-Cookie': 'JSESSIONID=971F40D46FE1A27AB4E2783BA77A1C76; '
                          'Path=/; Secure; HttpOnly',
            'Content-Type': 'application/json',
            'Content-Length': '138',
            'Date': 'Wed, 12 May 2021 15:00:27 GMT',
            'Keep-Alive': 'timeout=10',
            'Connection': 'keep-alive',
            'Server': 'Zscaler'
            }


def mocked_zia_client(*args, **kwargs):
    class MockResponse:
        """Class will be used by the mock to replace ZIA in circuits tests"""
        def __init__(self, *args, **kwargs):
            pass

        def blocklist_action(self, blocklisturls=None, action=None):
            assert action in ["ADD_TO_LIST", "REMOVE_FROM_LIST"]
            return blocklist_action_result()

        def get_blocklist_urls(self):
            return get_blocklist_urls_result()

    return MockResponse(*args, **kwargs)

def mocked_requests(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace RequestsCommon in standalone tests"""
        def __init__(self, *arg, **kwargs):
            pass

        def execute_call_v2(self, *args, **kwargs):
            if args[0].lower() == "post":
                if args[1].lower() == "/authenticatedsession":
                    return MockGetResponse(get_auth_headers(), None, 204)
            elif args[0].lower() == "get":
                pass

        def get_proxies(self, *args, **kwargs):
            return {}

        def __getitem__(self, key):
            return getattr(self, key)

    return MockSession(*args, **kwargs)

class MockGetResponse:
    """Class will be used by the mock to replace request response in standalone tests"""
    def __init__(self, *args, **kwargs):
        self.headers = args[0] if "Set-Cookie" in args[0] else {}
        self.r = Response()
        if args[0]:
            self.token = args[0]
        if args[1]:
            self.r._content = (args[1]).encode()
        self.status_code = args[2]
        self.r.status_code = args[2]
