# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

import pytest
from unittest.mock import patch, MagicMock
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "rc_data_feed"
FUNCTION_NAME = "data_feeder_sync_incidents"

# Inline config data — [resilient] host is required by the circuits_app fixture
config_data = """[resilient]
host=localhost
org=Test Org
api_key_id=test_key_id
api_key_secret=test_key_secret

[rc_data_feed]
feed_names=test_feed
reload=false
reload_types=
reload_query_api_method=false
queue=feed_data
include_attachment_data=false
workspaces=
parallel_execution=False
"""

# Provide a simulation of the Resilient REST API
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_data_feeder_sync_incidents_function(circuits, function_params, timeout=10):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("data_feeder_sync_incidents", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("data_feeder_sync_incidents_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDataFeederSyncIncidents:
    """ Tests for the data_feeder_sync_incidents function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "df_min_incident_id": 100,
        "df_max_incident_id": 105,
        "df_query_api_method": False
    }
    expected_results_1 = {"success": True}

    mock_inputs_2 = {
        "df_min_incident_id": 200,
        "df_max_incident_id": 200,
        "df_query_api_method": True
    }
    expected_results_2 = {"success": True}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        mock_reload = MagicMock()
        mock_reload.reload_all.return_value = 3

        mock_plugin_pool = MagicMock()

        with patch("rc_data_feed.components.data_feeder_sync_incidents.RestClientHelper"), \
             patch("rc_data_feed.components.data_feeder_sync_incidents.PluginPool.get_instance",
                   return_value=mock_plugin_pool), \
             patch("rc_data_feed.components.data_feeder_sync_incidents.Reload",
                   return_value=mock_reload):

            results = call_data_feeder_sync_incidents_function(circuits_app, mock_inputs)
            assert results.get("success") == expected_results.get("success")
            assert "num_of_sync_incidents" in results.get("content", {})
