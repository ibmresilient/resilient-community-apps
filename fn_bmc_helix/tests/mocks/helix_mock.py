# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Generate Mock responses to simulate Helix for Unit and function tests """

def mock_init():
    class MockClient(object):
        def __init__(self):
            pass

        def build_request_headers(self, *args, **kwargs):
            token = "foo.token"
            reqHeaders = {
                    "content-type": "application/json",
                    "Authorization": "AR-JWT " + token
                }
            return reqHeaders

        def get_form_entry(self, *args, **kwargs):
            status_code = 200
            form = {
                "values": {
                    "Status": "New",
                    "First_Name": "Allen",
                    "Last_Name": "Allbrook",
                    "Request ID": "0000000001"
                },
                "links": {
                    "foo": "bar"
                }
            }
            return form, status_code

        def create_form_entry(self, *args, **kwargs):
            status_code = 201
            form = {
                "values": {
                    "Incident Number": "INC00000001",
                    "Request ID": "0000000001"
                },
                "links": {
                    "foo": "bar"
                }
            }
            return form, status_code

        def update_form_entry(self, *args, **kwargs):
            return {}, 204

        def query_form_entry(self, *args, **kwargs):
            form = {
                "entries": [{
                    "values": {
                        "Status": "New",
                        "First_Name": "Allen",
                        "Last_Name": "Allbrook",
                        "Request ID": "0000000001",
                        "Incident Number": "INC00000001"
                    }
                }]
            }
            return form, 200

    return MockClient()
