# -*- coding: utf-8 -*-
"""Helper for tests"""

PACKAGE_NAME = "fn_splunk_integration"

config_data = """
[fn_splunk_integration]
host=localhost
port=8089
username=admin
splunkpassword=examplePass
#token=
verify_cert=false
# uncomment as necessary for proxies
#https_proxy=https://yourproxy.com
"""

def update_notable_results():
    return {
        "details": {},
        "success_count": 1,
        "failure_count": 0,
        "warnings": [],
        "success": True,
        "message": "1 event updated successfully"
    }

def delete_threat_intel_item_results():
    return {
        "message": "Delete operation successful.",
        "status": True
    }

def add_threat_intel_item_results():
    return {
        "message": "Create operation successful.",
        "status": True
    }

def search_results():
    return [
        {
            "_key": "1cd1fe20bb194ed9afb1b085c75149ef",
            "disabled": "0",
            "ip": "1.1.1.1",
            "item_key": "1cd1fe20bb194ed9afb1b085c75149ef",
            "threat_collection": "ip_intel",
            "threat_key": "restapi",
            "time": "1697476986",
            "updated": "0"
        },
        {
            "_key": "7ae5b3a9bcd7484eadd00b2d7473c8d0",
            "disabled": "0",
            "ip": "1.1.1.1",
            "item_key": "7ae5b3a9bcd7484eadd00b2d7473c8d0",
            "threat_collection": "ip_intel",
            "threat_key": "restapi",
            "time": "1697477015",
            "updated": "0"
        },
        {
            "_key": "dc3c8a0ce1f2464897d8c1995d66e1e4",
            "disabled": "1",
            "ip": "1.1.1.1",
            "item_key": "dc3c8a0ce1f2464897d8c1995d66e1e4",
            "threat_collection": "ip_intel",
            "threat_key": "restapi",
            "time": "1693317050",
            "updated": "0"
        },
        {
            "_key": "ecbe47f05d3b47788529c89050c1bf56",
            "disabled": "0",
            "ip": "1.1.1.1",
            "item_key": "ecbe47f05d3b47788529c89050c1bf56",
            "threat_collection": "ip_intel",
            "threat_key": "restapi",
            "time": "1693316423",
            "updated": "0"
        }
    ]

def mock_init():
    class MockClient(object):
        """ Add Mock connection data """

        def __init__(self):
            """ Mock """
            pass

        def update_notable(self, event_id, comment, status):
            """ Mock update_notable results """
            return {"content": update_notable_results()}

        def delete_threat_intel_item(self, threat_type, item_key):
            """ mock delete_threat_intel_item results """
            return {"content": delete_threat_intel_item_results()}

        def add_threat_intel_item(self, threat_type, threat_dict):
            """ Mock add_threat_intel_item results """
            return {"content": add_threat_intel_item_results()}

        def search(self, query, max_return):
            """ Mock search """
            return search_results()

    return MockClient()
