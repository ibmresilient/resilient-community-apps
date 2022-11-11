# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import re
from unittest.mock import patch

import pytest
import requests_mock
from resilient import SimpleHTTPException
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_lib import IntegrationError

PACKAGE_NAME = "fn_darktrace"
FUNCTION_NAME = "darktrace_clear_data_table"

# Read the default configuration-data section from the package
config_data = """[fn_darktrace]
api_key=abcd-efgh
api_secret=1234-abcd-56789-efgh
instance_url=https://fake.cloud.darktrace.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_darktrace_clear_data_table_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("darktrace_clear_data_table", function_params)

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
        event = circuits.watcher.wait("darktrace_clear_data_table_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDarktraceClearDataTable:
    """ Tests for the darktrace_clear_data_table function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_success(self, circuits_app):
        """ Test calling with sample values for the parameters """
        mock_inputs = {
            "darktrace_data_table_name": "mock_dt",
            "darktrace_soar_case_id": 1234
        }

        with requests_mock.Mocker() as mock_soar_api:
            mock_soar_api.register_uri(
                "DELETE",
                re.compile(r"/rest/orgs/\d+/incidents/.*/table_data/.*/row_data.*"),
                json={},
                status_code=200
            )
            results = call_darktrace_clear_data_table_function(circuits_app, mock_inputs)
        assert({} == results.get("content"))

    def test_failure(self, circuits_app, caplog):
        """ Test calling with sample values for the parameters """
        mock_inputs = {
            "darktrace_data_table_name": "mock_dt",
            "darktrace_soar_case_id": 1234
        }
        class FakeResponse:
            reason = ""
            text = ""

        with patch("fn_darktrace.components.funct_darktrace_clear_data_table.FunctionComponent.rest_client") as mock_delete:
            # can't use requests_mock like above for negative testing
            # because of the default retry parameters -- will timeout before test is complete
            fake_response = FakeResponse()
            fake_response.reason = "Failed to delete on server"
            fake_response.text = "Because this is a test"
            mock_delete.side_effect = SimpleHTTPException(fake_response)
            with pytest.raises(IntegrationError):
                call_darktrace_clear_data_table_function(circuits_app, mock_inputs)

        assert "Failed to clear table" in caplog.text
