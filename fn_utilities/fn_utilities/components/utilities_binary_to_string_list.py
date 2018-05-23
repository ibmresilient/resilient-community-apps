# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#  -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from fn_utilities.components.utilities_binary_to_string_list_floss import extract_strings

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'binary_to_string_list"""

    @function("utilities_binary_to_string_list")
    def _binary_to_string_list_function(self, event, *args, **kwargs):
        """Function: This function takes a binary file and returns a list of decoded obfuscated strings from the binary file."""
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
            data = self.get_binary_data_from_file(client, incident_id, task_id, artifact_id, attachment_id)
            yield StatusMessage("Binary file retrieved.")

            # Extract the strings from the binary file and put them in a list.
            list_results = extract_strings(data)

            yield StatusMessage("Returning list of {} decoded strings".format(len(list_results)))
            yield FunctionResult({"value": list_results})

        except Exception as err:
            yield FunctionError(err)

