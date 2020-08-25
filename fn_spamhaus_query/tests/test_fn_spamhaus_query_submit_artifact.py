# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_lib import IntegrationError
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_spamhaus_query.util.spamhaus_helper import CONFIG_DATA_SECTION


PACKAGE_NAME = CONFIG_DATA_SECTION
FUNCTION_NAME = "fn_spamhaus_query_submit_artifact"

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

config_data = """[{0}]
spamhaus_wqs_url = https://www.example.com/
spamhaus_dqs_key = ABCDEF""".format(PACKAGE_NAME)


class MockedResponse:
    def __init__(self):
        self.success = True
        self.status_code = 200

    def json(self):
        return {"resp": ["1002"]}


def call_fn_spamhaus_query_submit_artifact_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_spamhaus_query_submit_artifact", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[0]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_spamhaus_query_submit_artifact_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnSpamhausQuerySubmitArtifact:
    """ Tests for the fn_spamhaus_query_submit_artifact function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_bad_api_key(self, circuits_app):
        with patch.dict(circuits_app.app.opts[PACKAGE_NAME], {"spamhaus_wqs_url": "https://apibl.spamhaus.net/lookup/v1/"}):

            function_params = {
                "spamhaus_query_string": "1002",
                "spamhaus_search_resource": "info"
            }

            with pytest.raises(IntegrationError, match=r"Unauthorized"):
                call_fn_spamhaus_query_submit_artifact_function(circuits_app, function_params)

    def test_bad_url(self, circuits_app):
        with patch.dict(circuits_app.app.opts[PACKAGE_NAME], {"spamhaus_wqs_url": "https://www.example.com/"}):

            function_params = {
                "spamhaus_query_string": "123",
                "spamhaus_search_resource": "info"
            }

            with pytest.raises(IntegrationError, match=r"Not Found for url"):
                call_fn_spamhaus_query_submit_artifact_function(circuits_app, function_params)

    def test_fields_defined(self, circuits_app):
        with patch("fn_spamhaus_query.components.fn_spamhaus_query_submit_artifact.RequestsCommon.execute_call_v2") as mock_get:
            mock_get.return_value = MockedResponse()

            function_params = {
                "spamhaus_query_string": "1002",
                "spamhaus_search_resource": ""
            }

            with pytest.raises(ValueError, match=r"'spamhaus_search_resource' is mandatory"):
                call_fn_spamhaus_query_submit_artifact_function(circuits_app, function_params)

    def test_success(self, circuits_app):
        with patch("fn_spamhaus_query.components.fn_spamhaus_query_submit_artifact.RequestsCommon.execute_call_v2") as mock_get:
            mock_get.return_value = MockedResponse()

            function_params = {
                "spamhaus_query_string": "1002",
                "spamhaus_search_resource": "info"
            }

            call_fn_spamhaus_query_submit_artifact_function(circuits_app, function_params)

            mock_get.assert_called_with(
                method="get",
                url="https://www.example.com/info/1002",
                headers={"Authorization": "Bearer ABCDEF"}
            )
