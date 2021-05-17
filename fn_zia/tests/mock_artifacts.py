# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate ZIA for Unit and function tests """
from requests.models import Response
import json
import re

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

def allowlist_action_result(urls=None):
    if urls:
        urls =  list(filter(None, re.split("\s+|,", urls)))
    else:
        urls = []
    res = {
        "whitelistUrls": []
    }
    for url in urls:
        res["whitelistUrls"].append(url)

    return res

def get_blocklist_urls_result():
    return {
        "blacklistUrls": [
            "badhost.com",
            "192.168.12.2"
        ]
    }

def get_allowlist_urls_result():
    return {
        "whitelistUrls": [
            "goodhost.com",
            "192.168.1.1"
        ]
    }
def add_or_remove_allowlist_urls_result(urls=None):
    if urls:
        urls =  list(filter(None, re.split("\s+|,", urls)))
    else:
        urls = []
    res = {
        "whitelistUrls": []
    }
    for url in urls:
        res["whitelistUrls"].append(url)

    return res

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

        def allowlist_action(self, allowlisturls=None, action=None):
            assert action in ["ADD_TO_LIST", "REMOVE_FROM_LIST"]
            if action in "ADD_TO_LIST":
                if "192.168.1.1" in allowlisturls:
                    return allowlist_action_result("192.168.1.1, goodhost.com")
                else:
                    return allowlist_action_result("goodhost.com")
            elif action in "REMOVE_FROM_LIST":
                if "goodhost.com" in allowlisturls:
                    return allowlist_action_result("")
                elif "192.168.1.1" in allowlisturls:
                    return allowlist_action_result("goodhost.com")

        def get_blocklist_urls(self):
            return get_blocklist_urls_result()

        def get_allowlist_urls(self):
            return get_allowlist_urls_result()

    return MockResponse(*args, **kwargs)

def mocked_requests(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace RequestsCommon in standalone tests"""
        def __init__(self, *arg, **kwargs):
            pass

        def execute_call_v2(self, *args, **kwargs):
            if args[0].lower() == "post":
                if args[1].lower().endswith("/authenticatedsession"):
                    return MockGetResponse(get_auth_headers(), None, 204)
                elif "/advanced/blacklisturls?action=" in args[1].lower():
                    return MockGetResponse(None, None, 204)
            elif args[0].lower() == "get":
                if args[1].lower().endswith("/security/advanced"):
                    return MockGetResponse(None, get_blocklist_urls_result(), 204)
                elif args[1].lower().endswith("/security"):
                    return MockGetResponse(None, get_allowlist_urls_result(), 204)
            elif args[0].lower() == "put":
                if args[1].lower().endswith("/security"):
                    allowlisturls = json.loads(kwargs["data"])["whitelistUrls"]
                    if "192.168.1.1" in allowlisturls:
                        return MockGetResponse(None, add_or_remove_allowlist_urls_result("goodhost.com"), 204)
                    else:
                        return MockGetResponse(None, add_or_remove_allowlist_urls_result(""), 204)

        def get_proxies(self, *args, **kwargs):
            return {}

        def __getitem__(self, key):
            return getattr(self, key)

    return MockSession(*args, **kwargs)

class MockGetResponse:
    """Class will be used by the mock to replace request response in standalone tests"""
    def __init__(self, *args, **kwargs):
        self.headers = {}
        self.content = None
        if args[0] and "Set-Cookie" in args[0]:
            self.headers = args[0]
        self.r = Response()
        if args[0]:
            self.token = args[0]
        if args[1]:
            self.content = self.r._content = json.dumps(args[1]).encode('utf-8')
        self.status_code = args[2]
        self.r.status_code = args[2]

    def json(self):
        return self.r.json()
