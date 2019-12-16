# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_shell_command''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_shell_command")
    def _utilities_shell_command_function(self, event, *args, **kwargs):
        """Function: This function allows your workflows to execute shell-scripts locally or remotely, and return the result into the workflow. The results include the `stdout` and `stderr` streams, the return code, and information about the execution time. If the output of the shell script is JSON, it is returned as structured data. Results can then be added to the incident as file attachments, artifacts, data tables, or any other uses.

These functions can be run on any platform. If you install and run the resilient-circuits framework on Windows, this allows you to configure this function to run PowerShell scripts."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_shell_command' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            shell_command = kwargs.get("shell_command")  # text
            shell_param1 = kwargs.get("shell_param1")  # text
            shell_remote = kwargs.get("shell_remote")  # boolean
            shell_param2 = kwargs.get("shell_param2")  # text
            shell_param3 = kwargs.get("shell_param3")  # text

            log = logging.getLogger(__name__)
            log.info("shell_command: %s", shell_command)
            log.info("shell_param1: %s", shell_param1)
            log.info("shell_remote: %s", shell_remote)
            log.info("shell_param2: %s", shell_param2)
            log.info("shell_param3: %s", shell_param3)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_shell_command' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
