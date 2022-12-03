# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from .common_config import github_config, create_branch
import pytest
from datetime import datetime
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_github"
FUNCTION_NAME = "github_create_branch"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_function(circuits, function_name, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(function_name, function_params)

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
        event = circuits.watcher.wait(f"{function_name}_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestGithubCreateBranch:
    """ Tests for the github_create_branch function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    def test_create_branch(self, circuits_app):
        """ Test calling with sample values for the parameters """

        ts = datetime.now()

        results, branch = create_branch(circuits_app, ts)
        assert(results.get("content", {}).get("ref"))

        # do the test again, will return branch already exists
        results2, branch2 = create_branch(circuits_app, ts)
        assert(not results2.get("success"))
        assert(results2.get("reason") == "422 Reference already exists")

        setup = github_config('get_branch')
        setup['github_branch'] = branch

        results = call_function(circuits_app, "github_get_branch", setup)
        assert(results.get('content', {}).get('name') == branch)

        # delete branch
        delete_branch_setup = github_config("delete_branch")
        delete_branch_setup["github_branch"] = branch

        results = call_function(circuits_app, "github_delete_branch", delete_branch_setup)
        assert(results.get("success"))
