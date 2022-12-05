# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
from datetime import datetime
import pytest
import time
from .common_config import github_config, create_branch, TS
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_github"
FUNCTION_NAME = "github_create_file"

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


class TestGithubCreateFile:
    """ Tests for the github_create_file function"""
    branch = None
    create_branch_results = None
    create_file_results = None
    get_file_results = None
    get_commits_results = None
    update_file_results = None
    get_commit_results = None
    get_file2_results = None
    delete_file_results = None

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def init_create_branch(self, circuits_app):

        # create file
        TestGithubCreateFile.create_branch_results, TestGithubCreateFile.branch = create_branch(circuits_app, TS)
        assert(TestGithubCreateFile.create_branch_results.get("content", {}).get("ref"))

    @pytest.mark.livetest
    def test_create_file(self, circuits_app):
        """ Test calling with sample values for the parameters """
        self.init_create_branch(circuits_app)

        TestGithubCreateFile.create_file_setup = github_config('create_file')
        TestGithubCreateFile.create_file_setup['github_ref'] = TestGithubCreateFile.branch

        TestGithubCreateFile.create_file_results = call_function(circuits_app, 'github_create_file', TestGithubCreateFile.create_file_setup)
        assert(TestGithubCreateFile.create_file_results['success'])

    @pytest.mark.livetest
    def test_get_file(self, circuits_app):
        #if not getattr(self, 'create_file_results', None):
        #    assert(False)

        # get file
        get_file_setup = github_config('get_file')
        get_file_setup['github_ref'] = TestGithubCreateFile.branch

        TestGithubCreateFile.get_file_results = call_function(circuits_app, 'github_get_file', get_file_setup)
        assert(TestGithubCreateFile.get_file_results['success'])
        assert(TestGithubCreateFile.get_file_results['content'].get("contents") == TestGithubCreateFile.create_file_setup['github_file_contents'])

    @pytest.mark.livetest
    def test_get_commits(self, circuits_app):
        #if not getattr(self, 'create_file_results', None):
        #    assert(False)

        # get commits
        get_commits_setup = github_config('get_commits')
        get_commits_setup['github_branch'] = TestGithubCreateFile.branch

        TestGithubCreateFile.get_commits_results = call_function(circuits_app, 'github_get_commits', get_commits_setup)
        assert(TestGithubCreateFile.get_commits_results['success'])
        assert(TestGithubCreateFile.get_commits_results['content']) # at least one commit

    @pytest.mark.livetest
    def test_update_file(self, circuits_app):
        if not (getattr(self, 'create_file_results', None) and getattr(self, 'get_commits_results', None)):
            assert(False)

        # update file
        TestGithubCreateFile.update_file_setup = github_config('update_file')
        TestGithubCreateFile.update_file_setup['github_branch'] = TestGithubCreateFile.branch

        TestGithubCreateFile.update_file_results = call_function(circuits_app, 'github_update_file', TestGithubCreateFile.update_file_setup)
        assert(TestGithubCreateFile.update_file_results['success'])

    @pytest.mark.livetest
    def test_get_commit(self, circuits_app):
        get_commit_setup = github_config('get_commit')
        get_commit_setup['github_sha'] = TestGithubCreateFile.update_file_results['content']['commit']

        TestGithubCreateFile.get_commit_results = call_function(circuits_app, 'github_get_commit', get_commit_setup)
        assert(TestGithubCreateFile.get_commit_results['success'])


    @pytest.mark.livetest
    def test_get_file2(self, circuits_app):

        # get the update file
        get_file_setup2 = github_config('get_file')
        get_file_setup2['github_ref'] = TestGithubCreateFile.branch

        TestGithubCreateFile.get_file2_results = call_function(circuits_app, 'github_get_file', get_file_setup2)
        assert(TestGithubCreateFile.get_file2_results['success'])
        assert(TestGithubCreateFile.get_file2_results['content'].get("contents") == TestGithubCreateFile.update_file_setup['github_file_contents'])

    @pytest.mark.livetest
    def test_delete_file(self, circuits_app):
        if not (getattr(self, 'create_file_results', None) and getattr(self, 'get_commits_results', None)):
            assert(False)

        # update file
        delete_file_setup = github_config('delete_file')
        delete_file_setup['github_branch'] = TestGithubCreateFile.branch

        TestGithubCreateFile.delete_file_results = call_function(circuits_app, 'github_delete_file', delete_file_setup)
        assert(TestGithubCreateFile.delete_file_results['success'])

    @pytest.mark.livetest
    def test_delete_branch(self, circuits_app):
        # delete branch
        delete_branch_setup = github_config("delete_branch")
        delete_branch_setup["github_branch"] = TestGithubCreateFile.branch

        results = call_function(circuits_app, "github_delete_branch", delete_branch_setup)
        assert(results.get("success"))
