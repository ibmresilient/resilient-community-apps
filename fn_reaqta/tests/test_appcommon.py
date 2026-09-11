# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import datetime
from io import BytesIO
import logging
import json
import pytest
import os
from fn_reaqta.lib.app_common import AppCommon
from resilient_lib import RequestsCommon, soar_datetimeformat
from resilient_circuits.helpers import get_configs
from jsonschema import validate
from jsonschema.exceptions import ValidationError

PACKAGE_NAME = "fn_reaqta"

LOG = logging.getLogger(__file__)

@pytest.fixture()
def app_common():
    opts = get_configs()

    # pick just one hive
    hive_label = "{}:".format(PACKAGE_NAME)
    for option_section in opts.keys():
        if option_section.startswith(hive_label):
            options = opts[option_section]
            break

    assert options
    rc = RequestsCommon(opts, options)
    yield AppCommon(rc, options)


class TestReaqtaAttachFile:

    @pytest.mark.livetest
    def test_get_alerts(self, app_common):
        # get all alerts
        lookback = datetime.datetime.now() - datetime.timedelta(minutes=1440)
        entity_list, err_msg = app_common.get_entities_since_ts(None, 0, None)
        assert not err_msg

        schema = get_schema("get_alerts_schema.json")

        status, msg = validate_json(schema, entity_list)
        #assert status, msg

        for alert in entity_list['result']:
            alert_id = alert['id']
            endpoint_id = alert['endpointId']
            happened_at = alert['happenedAt']

            happended_at_ts = soar_datetimeformat(happened_at, split_at=".")

            # try to get based on search criteria
            self._test_get_entities_ts(alert_id, "receivedAfter", happended_at_ts, app_common)

            # get alert by Id
            self._test_get_alert_info(alert_id, app_common)

            # get processes for an endpoint
            if self._test_get_endpoint_processes(endpoint_id, app_common):
                break

    def _test_get_entities_ts(self, alert_id, alert_field, ts, app_common):
        # test search for an alert based on when it was received
        entity_list, err_msg = app_common.get_entities_since_ts("receivedAfter", ts, None)
        assert not err_msg

        found_true = False
        for entity in entity_list['result']:
            if entity['id'] == alert_id:
                found_true = True
                break

        assert found_true

    def _test_get_alert_info(self, alert_id, app_common):
        ### get alert information
        alert_info, err_msg = app_common.get_alert(alert_id)
        assert not err_msg

        schema = get_schema("get_alert_info_schema.json")
        status, msg = validate_json(schema, alert_info)
        assert status, msg

    def _test_get_endpoint_processes(self, endpoint_id, app_common):
        ### get an endpoint's process like, if it's online
        process_info = app_common.get_processes(endpoint_id)
        # offline endpoints return `{"message":"Endpoint offline","details":{"endpointId":"836992866751348736","lastSeenAt":"2022-03-05T03:32:14.322Z"}}`
        if process_info and isinstance(process_info, list):
            schema = get_schema("get_processes_schema.json")
            status, msg = validate_json(schema, process_info)
            assert status, msg

            for process in process_info:
                if process.get("programPath"):
                    self._test_process_file(endpoint_id, process.get("programPath"), app_common)
                    return True

        return False

    def _test_process_file(self, endpoint_id, program_path, app_common):
        ### Get an endpoint program based on it's program path
        process_bytes, err_msg = app_common.get_program_file(endpoint_id, program_path)
        assert not err_msg, err_msg

        assert isinstance(process_bytes, BytesIO)


def get_data_directory():
    return os.path.join(os.path.dirname(__file__), "data")

def get_schema(schema_filename):
    """This function loads the given schema available"""
    with open(os.path.join(get_data_directory(), schema_filename), 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(schema, json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.

    try:
        validate(instance=json_data, schema=schema)
    except ValidationError as err:
        print(err)
        err_msg = "Given JSON data is Invalid"
        return False, err_msg

    message = "Given JSON data is Valid"
    return True, message
