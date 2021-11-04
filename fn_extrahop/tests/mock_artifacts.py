# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate ZIA for Unit and function tests """
import json

from requests.models import Response

def get_mock_config():
    config_data = u"""[fn_extrahop]
extrahop_rx_host_url = https://myextrahop.com
extrahop_rx_key_id = "abcdefg123456789"
extrahop_rx_key_secret = "123456789abcdefg987654321abcdefg"
extrahop_rx_api_version = v1
"""
    return config_data

def get_tags():
    return [
        {
            "mod_time": 1635771586176,
            "id": 1,
            "name": "test_tag_1"},
        {
            "mod_time": 1635784783991,
            "id": 2,
            "name": "test_tag_2"}
    ]

def mocked_rx_client(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace ZIA in circuits tests"""
        def __init__(self, *args, **kwargs):
            pass

        def get_devices(self, active_from=None, active_until=None, limit=None, offset=None, device_id=None,
                        search_type="any"):
            return MockGetResponse("{}", 200)

        def search_devices(self, active_from=None, active_until=None, limit=None, offset=None, search_filter=None):
            return MockGetResponse("[]", 200)

        def get_detections(self, detection_id=None, limit=None):
            return MockGetResponse("{}", 200)

        def search_detections(self, search_filter=None, active_from=None, active_until=None, limit=None, offset=None,
                              update_time=None, sort=None):
            return MockGetResponse("[]", 200)

        def get_tags(self, tag_id=None):
            if tag_id == 0:
                return MockGetResponse([get_tags()[0]], 200)
            else:
                return MockGetResponse(get_tags(), 200)

        def create_tag(self, tag_name=None):
            return MockGetResponse({}, 200)

        def assign_tag(self, tag_id=None, device_ids=None):
            return MockGetResponse({}, 200)

        def get_watchlist(self):
            return MockGetResponse([], 200)

        def update_watchlist(self, assign=None, unassign=None):
            return MockGetResponse([], 200)

    return MockSession(*args, **kwargs)

class MockGetResponse:
    """Class will be used by the mock to replace get and post requests in standalone tests"""
    def __init__(self, *args, **kwargs):
        self.headers = {}
        self.r = Response()
        self.r._content = json.dumps(args[0]).encode('utf-8')
        self.status_code = args[1]
        self.r.status_code = args[1]

    def json(self):
        return self.r.json()