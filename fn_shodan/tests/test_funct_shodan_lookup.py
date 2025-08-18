# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from mock import NonCallableMagicMock, NonCallableMock
from resilient_lib import RequestsCommon
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_shodan.util.helper import CONFIG_DATA_SECTION

PACKAGE_NAME = CONFIG_DATA_SECTION
FUNCTION_NAME = "shodan_lookup"
MOCK_VULNS = ["mock_vul_1", "mock_vul_2"]
MOCK_PORTS = ["1000", "1001"]

config_data = """[{0}]
shodan_apikey=ABCDEF12345
http_proxy=http://localhost:0000
http_proxys=https://localhost:0000""".format(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_shodan_lookup_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("shodan_lookup", function_params)

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
        event = circuits.watcher.wait("shodan_lookup_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestShodanLookup:
    """ Tests for the shodan_lookup function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_fields_defined(self, circuits_app):

        function_params = {
            "shodan_lookuphost": "",
        }

        with pytest.raises(ValueError, match=r"'shodan_lookuphost' is mandatory"):
            call_shodan_lookup_function(circuits_app, function_params)

    def test_function_runs(self, circuits_app):
        with patch("fn_shodan.components.funct_shodan_lookup.make_api_call") as mock_call:
    
            app_configs = circuits_app.app.opts.get(PACKAGE_NAME)
            rc = RequestsCommon(circuits_app.app.opts, app_configs)

            mock_call.return_value = {
                "vulns": MOCK_VULNS,
                "ports": MOCK_PORTS
            }

            function_params = {
                "shodan_lookuphost": "127.0.0.1",
            }

            mock_results = call_shodan_lookup_function(circuits_app, function_params)

            mock_call.assert_called()
            assert mock_results.get("content").get("vulns") == MOCK_VULNS
            assert mock_results.get("content").get("ports") == MOCK_PORTS
