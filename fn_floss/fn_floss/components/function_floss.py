# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#  -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""
    fn_floss reads a binary file and returns a list
    of decoded obfuscated strings from the file. The input can be a binary
    file associated with an artifact or an attachment associated with an
    incident or task.

    This function uses a Python library called Floss to extract the
    strings from the binary file. You can find Floss on github here:
    https://github.com/fireeye/flare-floss
    Floss installation instructions can be found here:
    https://github.com/fireeye/flare-floss/blob/master/doc/installation.md

    Note that Floss requires Python library vivisect which can be found here:
    https://github.com/williballenthin/vivisect

    The user can define the commandline options to Floss in the app.config
    file.  The default options are -q (quiet mode), -s (shellcode), and
    -n 5 (minimum string length of 5).  To learn about all possible
    input parameters for Floss read here:
    https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_floss.lib.floss_util import extract_strings, get_binary_data_from_file


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_floss"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_floss", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_floss", {})

    @function("fn_floss")
    def _fn_floss_function(self, event, *args, **kwargs):
        """Function: This function takes a binary file from an attachment or artifact and returns a list of the decoded obfuscated strings extracted from the binary file."""
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
                # Set the defaults floss options to -q (quiet mode), -s (shellcode) and -n minimum
                # string length 5...if none are defined in the app.config file
                str_floss_options = '-q,-s,-n 5'

            # Extract the strings from the binary file and put them in a list.
            list_results = []
            list_results = extract_strings(str_floss_options, data)
            log.debug(str(list_results))

            yield StatusMessage("Returning list of {} decoded strings".format(len(list_results)))
            yield FunctionResult({"value": list_results})

        except Exception as err:
            log.error(str(err))
            yield FunctionError(err)
