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

def get_blocklist_urls():
    return {
        "blacklistUrls": [
            "badhost.com",
            "192.168.12.2"
        ]
    }

def get_blocklist_urls_result(url_filter=None):
    res = get_blocklist_urls()
    total = filtered = 2
    if url_filter:
        regex = r'{}'.format(url_filter)
        res["blacklistUrls"] = [u for u in res["blacklistUrls"] if re.search(regex, u, re.I)]
        filtered = len(res["blacklistUrls"])

    res.update({
        "url_counts": {
            "total": total,
            "filtered": filtered
        }
    })
    return res

def get_allowlist_urls():
    return {
        "whitelistUrls": [
            "goodhost.com",
            "192.168.1.1"
        ]
    }

def get_allowlist_urls_result(url_filter=None):
    res = get_allowlist_urls()
    total = filtered = 2

    if url_filter:
        regex = r'{}'.format(url_filter)
        res["whitelistUrls"] = [u for u in res["whitelistUrls"] if re.search(regex, u, re.I)]
        filtered = len(res["whitelistUrls"])

    res.update({
        'url_counts': {
            "total": total,
            "filtered": filtered
        }
    })
    return res

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

def category_action_result(category_id, configured_name, urls, action):
    result_urls = ["1.1.1.1", "testhost.com","192.168.1.1"]
    urls = list(filter(None, re.split(r"\s+|,|\n", urls)))
    if action == "ADD_TO_LIST":
        result_urls += [a for a in urls if a not in result_urls]
    else:
        result_urls = [a for a in result_urls if a not in urls]
    return {
        "id": category_id,
        "configuredName": configured_name,
        "keywordsRetainingParentCategory": [],
        "urls": result_urls,
        "dbCategorizedUrls": [],
        "customCategory": True,
        "editable": True,
        "description": "CUSTOM_01_DESC",
        "type": "URL_CATEGORY",
        "val": 128,
        "customUrlsCount": 2,
        "urlsRetainingParentCategoryCount": 0
    }

def add_url_category_result(urls, configured_name, custom_category, super_category, keywords):
    urls = list(filter(None, re.split(r"\s+|,|\n", urls)))
    keywords = list(filter(None, re.split(r"\s+|,|\n", keywords)))
    return {
        "id": "CUSTOM_01",
        "configuredName": configured_name,
        "superCategory": super_category,
        "keywords": keywords,
        "keywordsRetainingParentCategory": [],
        "urls": urls,
        "dbCategorizedUrls": [],
        "customCategory": True,
        "editable": True,
        "type": custom_category,
        "val": 130, "customUrlsCount": 2,
        "urlsRetainingParentCategoryCount": 0
    }

def get_url_categories_base():
    base_result = [
        {
            "id": "CUSTOM_01",
            "configuredName": "TEST_CAT_1",
            "superCategory": "USER_DEFINED",
            "keywords": ["test"],
            "keywordsRetainingParentCategory": [],
            "urls": ["testhost.com"],
            "dbCategorizedUrls": [],
            "customCategory": True,
            "editable": True,
            "type": "URL_CATEGORY",
            "val": 128,
            "customUrlsCount": 1,
            "urlsRetainingParentCategoryCount": 0
        },
        {
            "id": "CUSTOM_02",
            "configuredName": "TEST_CAT_2",
            "superCategory": "USER_DEFINED",
            "keywords": ["test2"],
            "keywordsRetainingParentCategory": [],
            "urls": ["testhost2.com", "192.168.1.1"],
            "dbCategorizedUrls": [],
            "customCategory": True,
            "editable": True,
            "type": "URL_CATEGORY",
            "val": 128,
            "customUrlsCount": 2,
            "urlsRetainingParentCategoryCount": 0
        },
    ]

    return base_result

def get_url_categories(custom_only, category_id):
        categories = get_url_categories_base()
        def_category_id = category_id if category_id else "CUSTOM_02"
        return [x for x in categories if x["id"] == def_category_id]

def get_url_categories_result(custom_only, category_id, name_filter=None, url_filter=None ):
    def_category_id = category_id if category_id else "CUSTOM_02"
    cat_total = 1 if category_id else 2

    categories = get_url_categories_base()

    for c in categories:
        c.update({
            "url_counts": {
                "total": len(c["urls"]),
                "filtered": len(c["urls"])
            }
        })
    if url_filter:
        regex_url = r'{}'.format(url_filter)
        for c in categories:
            c["urls"] =  [u for u in c["urls"] if re.search(regex_url, u, re.I)]
            c["url_counts"]["filtered"] = len(c["urls"])

    if name_filter:
        regex_name = r'{}'.format(name_filter)
        categories = [c for c in categories if re.search(regex_name, c["configuredName"], re.I)]
    else:
        categories = [c for c in categories if c["id"] == def_category_id]

    cat_filtered = len(categories)

    res = {
        "categories": categories,
        "category_counts": {"total": cat_total, "filtered": cat_filtered}
    }

    return res

def url_lookup_result(urls):
    urls = list(filter(None, re.split(r"\s+|,|\n", urls)))
    base_result = [
        {
            "url": "host.com",
            "urlClassifications": ["PROFESSIONAL_SERVICES"],
            "urlClassificationsWithSecurityAlert": []
        },
        {
            "url": "viruses.org",
            "urlClassifications": ["MISCELLANEOUS_OR_UNKNOWN"],
            "urlClassificationsWithSecurityAlert": []
        },
    ]
    return [x for x in base_result if x["url"]  in urls]

def get_sandbox_report_result(full):

    report_type = "full" if full else "summary"
    result = {
        "full": {
            "Full Details": {
                "Summary": {
                    "Status": "COMPLETED",
                    "Category": "EXECS",
                    "FileType": "EXE",
                    "StartTime": 1620229320,
                    "Duration": 658451
                },
                "Classification": {
                    "Type": "MALICIOUS",
                    "Category": "MALWARE_BOTNET",
                    "Score": 80,
                    "DetectedMalware": "Gen:Variant.MSILPerseus.158871"
                },
                "FileProperties": {
                    "FileType": "EXE",
                    "FileSize": 22016,
                    "MD5": "542a09dbd513bf75e29572922ce0687e",
                    "SHA1": "6e0d16aa60b37596774ed0d3054ed2ff39d9378f",
                    "Sha256": "dbcb1fa12366b385224f1a203c8cc24d6740f4bfa3b4f7a9d6d9ff059f470819",
                    "Issuer": '',
                    "DigitalCerificate": '',
                    "SSDeep": "384:UGaRIorFBiFKx5v38y3QLp29Jub/mPkaVIKvtMNokpkjUo165Dt:1JorvjxZPAgyQRt/7jUo1A",
                    "RootCA": ''
                },
                "SystemSummary": [
                    {
                        "Risk": "LOW",
                        "Signature": "Binary contains paths to debug symbols",
                        "SignatureSources": [
                            '',
                            "14351.PDB source: 14351.exe, 00000000.00000002.1064908917.000000001CAC4000.00000004.00000001.sdmp",
                            "C:\\14351.PDB source: 14351.exe, 00000000.00000002.1064908917.000000001CAC4000.00000004.00000001.sdmp",
                            "X8c:\\Users\\Julien\\Documents\\Visual Studio 2013\\Projects\\Botnet\\Botnet\\obj\\Release\\Botnet.pdb source: 14351.exe",
                            "c:\\Users\\Julien\\Documents\\Visual Studio 2013\\Projects\\Botnet\\Botnet\\obj\\Release\\Botnet.pdb source: 14351.exe",
                            "pC:\\14351.PDB source: 14351.exe, 00000000.00000002.1064908917.000000001CAC4000.00000004.00000001.sdmp",
                            "t.pdb source: 14351.exe, 00000000.00000002.1064908917.000000001CAC4000.00000004.00000001.sdmp"
                        ]
                    },
                    {
                        "Risk": "LOW",
                        "Signature": "Classification label",
                        "SignatureSources": [
                            '',
                            "mal52.winEXE@2/1@2/4"
                        ]
                    }

                ],
                "Networking": [
                    {
                        "Risk": "LOW",
                        "Signature": "Downloads files from web servers via HTTP",
                        "SignatureSources": [
                            '',
                            "GET /Yabrod.pdf HTTP/1.1Authorization: Basic enNjYWxlcjp6c2NhbGVyUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like GeckoHost: d1stb3hi9jgowm.cloudfront.net",
                            "GET /Yabrod.pdf HTTP/1.1Authorization: Basic enNjYWxlcjp6c2NhbGVyUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like GeckoHost: d1stb3hi9jgowm.cloudfront.net"
                        ]
                    }
                ],
                "SecurityBypass": [
                    {
                        "Risk": "MODERATE",
                        "Signature": "Found a high number of Window / User specific system calls",
                        "SignatureSources": [
                            '',
                            "foregroundWindowGot 1497",
                            "foregroundWindowGot 494",
                            "threadDelayed 1941",
                            "threadDelayed 36971",
                            "threadDelayed 4118",
                            "threadDelayed 448978"
                        ]
                    }
                ],
                "Exploit": [
                    {
                        "Risk": "LOW",
                        "Signature": "May try to detect the Windows Explorer process",
                        "SignatureSources": [
                            '',
                            "+Mouse><LMouse><LMouse>[Program Manager]",
                            "<LMouse><RMouse><LMouse><RMouse><LMouse><LMouse><LMouse>[Program Manager]p",
                            "<LMouse><RMouse><LMouse><RMouse><LMouse><LMouse>[Program Manager]",
                            "<LMouse><RMouse><LMouse><RMouse><LMouse><LMouse>[Program Manager]p",
                            "<LMouse>[Program Manager]",
                            "Program Manager",
                            "Program Managerp",
                            "[Program Manager] "
                        ]
                    }
                ],
                "Stealth": [
                    {
                        "Risk": "LOW",
                        "Signature": "Disables application error messages",
                        "SignatureSources": [
                            '',
                            "NOOPENFILEERRORBOX",
                        ]
                    }
                ]
            }
        },
        "summary": {
            "Summary": {
                "Summary": {
                    "Status": "COMPLETED",
                    "Category": "EXECS",
                    "FileType": "DLL",
                    "StartTime": 1522111841,
                    "Duration": 481690
                },
                "Classification": {
                    "Type": "MALICIOUS",
                    "Category": "MALWARE_BOTNET",
                    "Score": 82,
                    "DetectedMalware": "Win32/TrojanDownloader.Banload.TNJ trojan"
                },
                "FileProperties": {
                    "FileType": "DLL",
                    "FileSize": 2358272,
                    "MD5": "b3b13c2fe5710507612106cb11ceced3",
                    "SHA1": "6f30404f8b30812758acc06455bc95348c86f9f2",
                    "Sha256": "c77ab4c60b73c8f8135d54162813ab7c63432058f17ff00754d5fd547c22db76",
                    "Issuer": "",
                    "DigitalCerificate": "",
                    "SSDeep": "49152:mQU0HSp/RcGuBLe/PESBbFVZ86MfBWPvGZxnBGVV3NcKRLFcTOJP:mQUn6LsPQp6vkoiKt",
                    "RootCA": ""
                }
            }
        }
    }
    return result[report_type]

def activate_result(activate):
    if activate:
        return {"status": "Activated"}
    return {"status": "Not_selected"}

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

        def get_blocklist_urls(self, url_filter=None):
            return get_blocklist_urls_result(url_filter=url_filter)

        def get_allowlist_urls(self, url_filter=None):
            return get_allowlist_urls_result(url_filter=url_filter)

        def category_action(self, category_id, configured_name, urls, action):
            return category_action_result(category_id, configured_name, urls, action)

        def add_url_category(self, urls, configured_name, custom_category, super_category, keywords):
            return add_url_category_result(urls, configured_name, custom_category, super_category, keywords)

        def get_url_categories(self, custom_only, category_id, name_filter=None, url_filter=None):
            return get_url_categories_result(custom_only, category_id, name_filter=name_filter, url_filter=url_filter)

        def url_lookup(self, urls=None):
            return url_lookup_result(urls)

        def activate(self, activate):
            return activate_result(activate)

        def get_sandbox_report(self, md5, full):
            return get_sandbox_report_result(full)

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
                elif args[1].lower().endswith("urlcategories"):
                    payload = json.loads(kwargs.get("data"))
                    return MockGetResponse(None, add_url_category_result(payload["configuredName"], payload["customCategory"],
                                                                         payload["superCategory"], payload["keywords"],
                                                                         ", ".join(payload["urls"])), 204)
                elif args[1].lower().endswith("urllookup"):
                    urls = ", ".join(json.loads(kwargs.get("data")))
                    return MockGetResponse(None, url_lookup_result(urls), 204)
                elif args[1].lower().endswith("status/activate"):
                    return MockGetResponse(None, activate_result(True), 204)

            elif args[0].lower() == "get":
                if args[1].lower().endswith("/security/advanced"):
                    return MockGetResponse(None, get_blocklist_urls(), 204)
                elif args[1].lower().endswith("/security"):
                    return MockGetResponse(None, get_allowlist_urls(), 204)
                elif args[1].lower().endswith("urlcategories/custom_01"):
                    return MockGetResponse(None, get_url_categories("true", "CUSTOM_01"), 204)
                elif args[1].lower().endswith("urlcategories"):
                    return MockGetResponse(None, get_url_categories("true", None), 204)
                elif "sandbox/report" in args[1].lower():
                    params = kwargs.get("params")
                    full = True if params and params.get("details") == "full" else False
                    return MockGetResponse(None, get_sandbox_report_result(full), 204)
            elif args[0].lower() == "put":
                if args[1].lower().endswith("/security"):
                    allowlisturls = json.loads(kwargs["data"])["whitelistUrls"]
                    if "192.168.1.1" in allowlisturls:
                        return MockGetResponse(None, add_or_remove_allowlist_urls_result("goodhost.com"), 204)
                    else:
                        return MockGetResponse(None, add_or_remove_allowlist_urls_result(""), 204)
                elif args[1].lower().endswith("urlcategories/custom_01"):
                    payload = json.loads(kwargs.get("data"))
                    params = kwargs.get("params")
                    return MockGetResponse(None, category_action_result("CUSTOM_01", payload["configuredName"],
                                                                        ", ".join(payload["urls"]), params["action"]), 204)

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
