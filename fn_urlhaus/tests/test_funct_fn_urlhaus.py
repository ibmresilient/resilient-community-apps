# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_urlhaus.util.helper import CONFIG_DATA_SECTION
from shared_mock_data import MockedResponse
from mock import patch

PACKAGE_NAME = CONFIG_DATA_SECTION
FUNCTION_NAME = "fn_urlhaus"

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

config_data = """[{0}]
url = https://www.example.com""".format(PACKAGE_NAME)


def call_fn_urlhaus_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_urlhaus", function_params)

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
        event = circuits.watcher.wait("fn_urlhaus_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnUrlhaus:
    """ Tests for the fn_urlhaus function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_bad_url(self, circuits_app):

        function_params = {
            "urlhaus_artifact_value": "123",
            "urlhaus_artifact_type": "URL"
        }

        with pytest.raises(Exception, match=r"Not Found for url"):
            call_fn_urlhaus_function(circuits_app, function_params)

    def test_fields_defined(self, circuits_app):
        with patch("fn_urlhaus.components.funct_fn_urlhaus.RequestsCommon.execute_call_v2"):

            function_params = {
                "urlhaus_artifact_value": "",
                "urlhaus_artifact_type": "URL"
            }

            with pytest.raises(ValueError, match=r"'urlhaus_artifact_value' is mandatory"):
                call_fn_urlhaus_function(circuits_app, function_params)

    def test_function_runs(self, circuits_app):
        with patch("fn_urlhaus.components.funct_fn_urlhaus.RequestsCommon.execute_call_v2") as mock_get:
            mock_get.return_value = MockedResponse()

            function_params = {
                "urlhaus_artifact_value": "123",
                "urlhaus_artifact_type": "URL"
            }

            call_fn_urlhaus_function(circuits_app, function_params)

            mock_get.assert_called_with(
                method="post",
                url="https://www.example.com/url",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"url": "123"}
            )

    def test_function_results(self, circuits_app):
        with patch("fn_urlhaus.components.funct_fn_urlhaus.RequestsCommon.execute_call_v2") as mock_get:
            mock_get.return_value = MockedResponse()

            function_params = {
                "urlhaus_artifact_value": "123",
                "urlhaus_artifact_type": "URL"
            }

            results = call_fn_urlhaus_function(circuits_app, function_params)

            assert results.get("content") == {"mock": "data"}
