# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
import mock
from .mock_artifact import MockedResponse
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_passivetotal"
FUNCTION_NAME = "fn_passivetotal"

# Fill in and uncomment key to run livetests
config_data = """[fn_passivetotal]
# API credentials
passivetotal_api_key=dummykeyforfirsttest
passivetotal_username=dummyuserforfirsttest
# passivetotal_api_key=$PASSIVETOTAL_KEY
# passivetotal_username=$YOUR_USERNAME

# API URLS
passivetotal_base_url=https://api.passivetotal.org
passivetotal_account_api_url=/v2/account
passivetotal_actions_tags_api_url=/v2/actions/tags
passivetotal_passive_dns_api_url=/v2/dns/passive
passivetotal_actions_class_api_url=/v2/actions/classification
passivetotal_enrich_subdom_api_url=/v2/enrichment/subdomains
passivetotal_community_url=https://community.riskiq.com/search/
passivetotal_tags=compromised,ransomware
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_passivetotal_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_passivetotal", function_params)

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
        event = circuits.watcher.wait("fn_passivetotal_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnPassivetotal:
    """ Tests for the fn_passivetotal function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "passivetotal_artifact_type": "IP Address",
        "passivetotal_artifact_value": "45.146.165.37"
    }

    expected_results_1 = {"success": True}

    expected_results_2 = [
                {'pdns_hit_number': 0},
                {'pdns_first_seen': None},
                {'pdns_last_seen': None},
                {'subdomain_hits_number': None},
                {'first_ten_subdomains': None},
                {'tags_hits_str': 'ransomeware, compromised'},
                {'classification_hit': None},
                {'report_url': 'https://community.riskiq.com/search/45.146.165.37'}
                ]

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with mock.patch("resilient_circuits.app_function_component.RequestsCommon.execute") as mock_execute:
            mock_execute.return_value = MockedResponse()
            results = call_fn_passivetotal_function(circuits_app, mock_inputs)
            assert(expected_results.get('success') == results.get('success'))

    @pytest.mark.parametrize("mock_inputs, expected_results", [ 
        (mock_inputs_1, expected_results_2)
    ])
    @pytest.mark.livetest
    def test_live_apicall(self, circuits_app, mock_inputs, expected_results):
        results = call_fn_passivetotal_function(circuits_app, mock_inputs)
        assert results.get('content') == expected_results