# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate Mock responses to simulate ZIA for Unit and function tests """
import json
import os

from requests.models import Response
TESTS_DIR = os.path.dirname(os.path.realpath(__file__))
PCAP_FILE = os.path.join(TESTS_DIR, "example.pcap")
PCAP_FILE_NAME = "example.pcap"

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
def get_test_pcap():
    with open(PCAP_FILE, 'rb') as mockzip:
        data = mockzip.read()
    return data

def mocked_rx_client(*args, **kwargs):
    class MockSession:
        """Class will be used by the mock to replace ZIA in circuits tests"""
        def __init__(self, *args, **kwargs):
            pass

        def get_devices(self, active_from=None, active_until=None, limit=None, offset=None, device_id=None,
                        search_type="any"):
            return MockGetResponse([], 200)

        def search_devices(self, active_from=None, active_until=None, limit=None, offset=None, search_filter=None):
            return MockGetResponse([], 200)

        def get_detections(self, detection_id=None, limit=None):
            return MockGetResponse([], 200)

        def search_detections(self, search_filter=None, active_from=None, active_until=None, limit=None, offset=None,
                              update_time=None, sort=None):
            return MockGetResponse([], 200)

        def get_tags(self, tag_id=None):
            if tag_id == 0:
                return MockGetResponse([get_tags()[0]], 200)
            else:
                return MockGetResponse(get_tags(), 200)

        def create_tag(self, tag_name=None):
            if tag_name == "failed":
                return MockGetResponse({}, 207)

            return MockGetResponse({}, 201)

        def assign_tag(self, tag_id=None, device_ids=None):
            if int(device_ids) == 1:
                return MockGetResponse({}, 204)
            if int(tag_id) == 1:
                return MockGetResponse({}, 207)

            return MockGetResponse({}, 200)

        def get_watchlist(self):
            return MockGetResponse([], 200)

        def update_watchlist(self, assign=None, unassign=None):
            if int(assign) == 1:
                return MockGetResponse({}, 207)

            return MockGetResponse({}, 201)

        def update_detection(self, detection_id=None, incident_id=None, plan_status=None, owner_id=None,
                             resolution_id=None, participants=None):
            if int(detection_id) == 1:
                return MockGetResponse({}, 207)

            return MockGetResponse({}, 201)

        def get_activitymaps(self, activitymap_id=None):
            return MockGetResponse([], 200)

        def search_packets(self, output=None, always_return_body=False, active_from=None, active_until=None,
                           limit_bytes=None, limit_search_duration=None, bpf=None, ip1=None, port1=None, ip2=None,
                           port2=None):

            return MockGetResponse(output, 200)

    return MockSession(*args, **kwargs)


class MockGetResponse:
    """Class will be used by the mock to replace get and post requests in standalone tests"""
    def __init__(self, *args, **kwargs):
        self.headers = {}
        self.r = Response()
        self.status_code = args[1]
        self.r.status_code = args[1]
        self.r._content = json.dumps(args[0]).encode('utf-8')
        if args[0] == "keylog_txt":
            self.content = json.dumps("").encode('utf-8')
            self.r._content = json.dumps("").encode('utf-8')
        elif args[0] == "zip":
            self.status_code = 204
            self.r.status_code = 204
        elif args[0] == "pcap":
            self.headers["Content-Disposition"] = 'attachment; filename="' + PCAP_FILE_NAME + '"'
            self.content = get_test_pcap()
            self.r._content = get_test_pcap()


    def json(self):
        return self.r.json()