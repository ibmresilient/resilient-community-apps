# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#  -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_utilities.lib.utilities_binary_to_string_list_util import extract_strings, get_binary_data_from_file

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'binary_to_string_list"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities", {})

    @function("utilities_binary_to_string_list")
    def _binary_to_string_list_function(self, event, *args, **kwargs):
        """Function: This function takes a binary file and returns a list of decoded
           obfuscated strings from the binary file."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)
            client = self.rest_client()

            # Get the binary data from the artifact or the attachment
            data = get_binary_data_from_file(client, incident_id, task_id, artifact_id, attachment_id)
            yield StatusMessage("Binary file retrieved.")

            # Get the floss commandline options from the app.config file.
            if "floss_options" in self.options:
                str_floss_options = self.options["floss_options"]
            else:
                # Set the defaults floss options to -q (quiet mode) and -s (shellcode) if none are
                # defined in the app.config file
                str_floss_options = "-q -s"

            # Extract the strings from the binary file and put them in a list.
            list_results = extract_strings(str_floss_options, data)

            yield StatusMessage("Returning list of {} decoded strings".format(len(list_results)))
            yield FunctionResult({"value": list_results})

        except Exception as err:
            yield FunctionError(err)
