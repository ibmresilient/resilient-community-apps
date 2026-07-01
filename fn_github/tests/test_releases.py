# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from .common_config import github_config, TS
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_github"
FUNCTION_NAME = "github_create_release"

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

def call_github_create_release_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("github_create_release", function_params)

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
        event = circuits.watcher.wait("github_create_release_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestGithubCreateRelease:
    """ Tests for the github_create_release function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.livetest
    def test_create_release(self, circuits_app):
        """ Test calling with sample values for the parameters """
        create_release_setup = github_config('create_release')
        create_release_setup['github_release_name'] = f"{create_release_setup['github_release_name']}_{TS.strftime('%Y%m%d_%H%M%S')}"
        create_release_setup['github_release_tag'] = f"{create_release_setup['github_release_tag']}_{TS.strftime('%Y%m%d_%H%M%S')}"

        results = call_function(circuits_app, "github_create_release", create_release_setup)
        assert(results['success'])

    @pytest.mark.livetest
    def test_get_release(self, circuits_app):
        """ Test calling with sample values for the parameters """
        get_release_setup = github_config('get_release')
        get_release_setup['github_release_tag'] = f"{get_release_setup['github_release_tag']}_{TS.strftime('%Y%m%d_%H%M%S')}"

        results = call_function(circuits_app, "github_get_release", get_release_setup)
        assert(results['success'])
        assert(results['content'])

    @pytest.mark.livetest
    def test_get_releases(self, circuits_app):
        get_releases_setup = github_config('get_releases')

        results = call_function(circuits_app, "github_get_releases", get_releases_setup)
        assert(results['success'])
        assert(results['content'])

    @pytest.mark.livetest
    def test_get_latest_release(self, circuits_app):
        get_releases_setup = github_config('get_latest_release')

        results = call_function(circuits_app, "github_get_latest_release", get_releases_setup)
        assert(results['success'])
        assert(results['content'])
