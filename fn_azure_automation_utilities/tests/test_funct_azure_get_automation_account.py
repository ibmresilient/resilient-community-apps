# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "azure_get_automation_account"

# Read the default configuration-data section from the package
config_data = helper.config_data

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_azure_get_automation_account_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("azure_get_automation_account", function_params)

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
        event = circuits.watcher.wait("azure_get_automation_account_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestAzureGetAutomationAccount:
    """ Tests for the azure_get_automation_account function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "account_name": "testing352",
        "resource_group_name": "DemoAssets"
    }

    expected_results_1 = {
        "name": "testing352",
        "systemData": {
        "createdAt": "2023-07-25T12:05:22.16+00:00",
        "lastModifiedAt": "2023-07-25T12:05:22.16+00:00"
        },
        "id": "/subscriptions/a4b7e24a-c7aa-4d84-8dae-89e99b336784/resourceGroups/DemoAssets/providers/Microsoft.Automation/automationAccounts/testing352",
        "type": "Microsoft.Automation/AutomationAccounts",
        "location": "eastus",
        "identity": {
        "type": "SystemAssigned",
        "principalId": "ee616124-e026-4ca0-8c64-d34bae779faf",
        "tenantId": "50ad7d3e-b889-434d-802d-13b87c68047b"
        },
        "tags": {},
        "etag": None,
        "properties": {
        "publicNetworkAccess": True,
        "disableLocalAuth": False,
        "sku": {
            "name": "Basic",
            "family": None,
            "capacity": None
        },
        "state": "Ok",
        "RegistrationUrl": "https://99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5.agentsvc.eus.azure-automation.net/accounts/99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5",
        "encryption": {
            "keySource": "Microsoft.Automation",
            "identity": {
            "userAssignedIdentity": None
            }
        },
        "privateEndpointConnections": [],
        "automationHybridServiceUrl": "https://99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5.jrds.eus.azure-automation.net/automationAccounts/99f846f3-c84d-4c96-af2b-cd0f7a5bd5d5",
        "RuntimeConfiguration": {
            "powershell": {
            "builtinModules": {
                "Az": "8.0.0"
            }
            },
            "powershell7": {
            "builtinModules": {
                "Az": "8.0.0"
            }
            }
        },
        "creationTime": "2023-07-25T12:05:22.16+00:00",
        "lastModifiedBy": None,
        "lastModifiedTime": "2023-07-25T12:05:22.16+00:00"
        }
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_azure_automation_utilities.components.funct_azure_get_automation_account.AzureClient") as patch_ack:
            patch_ack.return_value = helper.mock_init()
            results = call_azure_get_automation_account_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
