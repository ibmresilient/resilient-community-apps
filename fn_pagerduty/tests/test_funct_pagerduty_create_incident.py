# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.1.824
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_pagerduty"
FUNCTION_NAME = "pagerduty_create_incident"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_pagerduty_create_incident_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("pagerduty_create_incident", function_params)

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
        event = circuits.watcher.wait(
            "pagerduty_create_incident_result", parent=evt, timeout=timeout
        )
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

def mocked_return():
    return {
        "incident": {
            "incident_number": 3,
            "title": "SOAR: Test1",
            "description": "SOAR: Test1",
            "created_at": "2024-04-16T14:16:44Z",
            "updated_at": "2024-04-16T14:16:44Z",
            "status": "triggered",
            "incident_key": "RES-2123",
            "service": {
                "id": "P2BUF3J",
                "type": "service_reference",
                "summary": "Default Service",
                "self": "https://api.pagerduty.com/services/P2BUF3J",
                "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J",
            },
            "assignments": [
                {
                    "at": "2024-04-16T14:16:44Z",
                    "assignee": {
                        "id": "PZ8LY8P",
                        "type": "user_reference",
                        "summary": "John Doe",
                        "self": "https://api.pagerduty.com/users/PZ8LY8P",
                        "html_url": "https://ibmtest-8.pagerduty.com/users/PZ8LY8P",
                    },
                }
            ],
            "assigned_via": "escalation_policy",
            "last_status_change_at": "2024-04-16T14:16:44Z",
            "resolved_at": None,
            "first_trigger_log_entry": {
                "id": "R0D5Q149ACTOT09DXWE8JNPYKA",
                "type": "trigger_log_entry_reference",
                "summary": "Triggered through the website.",
                "self": "https://api.pagerduty.com/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA",
                "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7/log_entries/R0D5Q149ACTOT09DXWE8JNPYKA",
            },
            "alert_counts": {"all": 0, "triggered": 0, "resolved": 0},
            "is_mergeable": True,
            "escalation_policy": {
                "id": "PNR45CQ",
                "type": "escalation_policy_reference",
                "summary": "Default",
                "self": "https://api.pagerduty.com/escalation_policies/PNR45CQ",
                "html_url": "https://ibmtest-8.pagerduty.com/escalation_policies/PNR45CQ",
            },
            "teams": [],
            "impacted_services": [
                {
                    "id": "P2BUF3J",
                    "type": "service_reference",
                    "summary": "Default Service",
                    "self": "https://api.pagerduty.com/services/P2BUF3J",
                    "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J",
                }
            ],
            "pending_actions": [],
            "acknowledgements": [],
            "basic_alert_grouping": None,
            "alert_grouping": None,
            "last_status_change_by": {
                "id": "P2BUF3J",
                "type": "service_reference",
                "summary": "Default Service",
                "self": "https://api.pagerduty.com/services/P2BUF3J",
                "html_url": "https://ibmtest-8.pagerduty.com/service-directory/P2BUF3J",
            },
            "priority": {
                "id": "PODCA25",
                "type": "priority",
                "summary": "P3",
                "self": "https://api.pagerduty.com/priorities/PODCA25",
                "html_url": None,
                "account_id": "PSHM5T7",
                "color": "f9b406",
                "created_at": "2024-04-15T11:57:37Z",
                "description": "",
                "name": "P3",
                "order": 300000000,
                "schema_version": 0,
                "updated_at": "2024-04-15T11:57:37Z",
            },
            "incidents_responders": [],
            "responder_requests": [],
            "subscriber_requests": [],
            "urgency": "high",
            "id": "Q06KVFVBOFHPI7",
            "type": "incident",
            "summary": "[#3] SOAR: Test1",
            "self": "https://api.pagerduty.com/incidents/Q06KVFVBOFHPI7",
            "html_url": "https://ibmtest-8.pagerduty.com/incidents/Q06KVFVBOFHPI7",
            "body": {
                "details": "https://example.SOAR.com:443/#incidents/2123?orgId=Org4\n"
            },
        }
    }


class TestPagerdutyCreateIncident:
    """Tests for the pagerduty_create_incident function"""

    def test_function_definition(self):
        """Test that the package provides customization_data that defines the function"""
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "pd_priority": "p3",
        "pd_incident_key": "RES-2123",
        "pd_service": "Default Service",
        "incidentID": 2123,
        "pd_escalation_policy": "default",
        "pd_title": "SOAR: Test1"
    }

    expected_results_1 = {"pd": mocked_return()}

    @patch("fn_pagerduty.components.funct_pagerduty_create_incident.PDClient", helper.MockClient)
    @pytest.mark.parametrize("mock_inputs, expected_results", [(mock_inputs_1, expected_results_1)])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """Test calling with sample values for the parameters"""
        results = call_pagerduty_create_incident_function(circuits_app, mock_inputs)
        assert expected_results == results.get("content", {})
