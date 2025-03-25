# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Tests using pytest_resilient_circuits"""

import pytest
from rc_data_feed.components.threadpool import get_time_series_data
from rc_data_feed.lib.type_info import convert_timer_fields, convert_timer_field

MOCK_TIMER_DATA = {
  "entities": [
    {
      "referenceObject": {
        "parent": None,
        "object_id": 3074,
        "object_name": "test artifact_type",
        "type_id": 0,
        "type_name": "incident"
      },
      "timer_fields": [
        {
          "field_name": "owner_id",
          "field_label": "Owner",
          "field_values": [
            {
              "field_value": "Resilient Sysadmin",
              "duration_in_seconds": 63679,
              "running": True
            }
          ]
        },
        {
          "field_name": "phase_id",
          "field_label": "Phase",
          "field_values": [
            {
              "field_value": "Respond",
              "duration_in_seconds": 63679,
              "running": True
            }
          ]
        },
        {
          "field_name": "severity_code",
          "field_label": "Severity",
          "field_values": [
            {
              "field_value": "Low",
              "duration_in_seconds": 63679,
              "running": True
            }
          ]
        },
        {
          "field_name": "ts_bool",
          "field_label": "ts_bool",
          "field_values": [
            {
              "field_value": "false",
              "duration_in_seconds": 34,
              "running": True
            },
            {
              "field_value": "true",
              "duration_in_seconds": 22,
              "running": False
            }
          ]
        },
        {
          "field_name": "ts_select",
          "field_label": "ts_select",
          "field_values": [
            {
              "field_value": "select_a",
              "duration_in_seconds": 22,
              "running": False
            },
            {
              "field_value": "select_b",
              "duration_in_seconds": 34,
              "running": True
            }
          ]
        }
      ]
    }
  ]
}

class MockRestClient():
    def post(self, url, body):
        return MOCK_TIMER_DATA

@pytest.mark.parametrize("filter_list, expected_result", [
        ([], 7),
        (["*"], 7),
        (["NOTFOUND"], 0),
        (["owner_id"], 1),
        (["owner_id", "NOTFOUND"], 1),
        (["owner_id", "phase_id"], 2),
        (["*_id"], 2),
        (["owner_id", "*"], 7),
])
def test_get_time_series_data(filter_list, expected_result):
    mock_rest_client = MockRestClient()
    time_series_list = get_time_series_data(mock_rest_client, 123, filter_list)
    assert len(time_series_list) == expected_result

@pytest.mark.parametrize("index, field_name, value", [
        (0, "timeseries__owner_id__resilient_sysadmin", 63679),
        (1, "timeseries__phase_id__respond", 63679),
        (2, "timeseries__severity_code__low", 63679),
        (3, "timeseries__ts_bool__true", 22),
        (3, "timeseries__ts_bool__false", 34),
        (4, "timeseries__ts_select__select_a", 22),
        (4, "timeseries__ts_select__select_b", 34),
])
def test_convert_timer_field(index, field_name, value):
    result = convert_timer_field(MOCK_TIMER_DATA["entities"][0]["timer_fields"][index])
    assert field_name in result
    assert result[field_name] == value
