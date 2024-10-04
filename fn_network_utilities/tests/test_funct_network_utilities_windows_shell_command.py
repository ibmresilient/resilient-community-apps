# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_network_utilities"
FUNCTION_NAME = "network_utilities_windows_shell_command"

# Read the default configuration-data section from the package
config_data = """[fn_network_utilities]
remote_powershell_extensions=ps1
# remote auth transport one of [ntlm, basic]
remote_auth_transport=ntlm
# remote computers
missing_parens=foo
incorrect_pswd_creds=(foo@192.168.1.186)
correct_host=(ms:foo@192.168.1.186)
# remote shell commands
remote_command=[remote path to script]
# local shell_command default commands (unix)
nslookup=nslookup "{{shell_param1}}"
dig=dig "{{shell_param1}}"
traceroute=(tracepath '{{shell_param1}}')
traceroute_windows=[traceroute.ps1]
whois=whois "{{shell_param1}}"
# remote shell cmd
bad_suffix=[bad_suffix.ps2]
missing_brackets=missing_brackets
good_remote=[good_remote.ps1]
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_network_utilities_windows_shell_command_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("network_utilities_windows_shell_command", function_params)

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
        event = circuits.watcher.wait("network_utilities_windows_shell_command_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestNetworkUtilitiesWindowsShellCommand:
    """ Tests for the network_utilities_windows_shell_command function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("shell_command, shell_param1, expected_results", [
        ('nslookup', "text", {"value": "xyz"}),
        ('dig', "text", {"value": "xyz"})
    ])
    def test_local_success(self, circuits_app, shell_command, shell_param1, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "shell_command": shell_command,
            "shell_param1": shell_param1
        }
        # results = call_shell_command_function(circuits_app, function_params)
        # assert(expected_results == results)

    @pytest.mark.parametrize("shell_remote, shell_command, shell_param1", [
        (True, 'nslookup:', None),
        (True, 'nf_cmd:na_host', None),
        (True, 'missing_parens:na_host', None),
        (True, 'incorrect_pswd_creds:na_host', None),
        (True, 'nf_cmd:correct_host', None),
        (True, 'nslookup:correct_host', None),
        (True, 'bad_suffix:correct_host', None),
        (True, 'missing_brackets:correct_host', None)
    ])
    def test_remote_failures(self, circuits_app, shell_remote, shell_command, shell_param1):
        with pytest.raises(Exception):
            function_params = {
                "shell_remote": shell_remote,
                "shell_command": shell_command,
                "shell_param1": shell_param1
            }
            results = call_network_utilities_windows_shell_command_function(circuits_app, function_params)

    @pytest.mark.parametrize("shell_remote, shell_command, shell_param1", [
        (False, 'good_remote', None),
        (False, 'remote_command', None),
        (False, 'correct_host', None)
    ])
    def test_local_failures(self, circuits_app, shell_remote, shell_command, shell_param1):
        with pytest.raises(Exception):
            function_params = {
                "shell_remote": shell_remote,
                "shell_command": shell_command,
                "shell_param1": shell_param1
            }
            results = call_network_utilities_windows_shell_command_function(circuits_app, function_params)