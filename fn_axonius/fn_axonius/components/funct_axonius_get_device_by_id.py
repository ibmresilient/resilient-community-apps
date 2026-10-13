# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""
from json import dumps
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (write_file_attachment, validate_fields)
from fn_axonius.lib.axonius_client import (AxoniusClient)

PACKAGE_NAME = "fn_axonius"
FN_NAME = "axonius_get_device_by_id"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'axonius_get_device_by_id'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get information on the Axonius device given an internal Axon ID.  
                  Optionally write the results to an incident or task attachment.
        Inputs:
            -   fn_inputs.axonius_internal_axon_id
            -   fn_inputs.axonius_write_attachment
            -   fn_inputs.axonius_incident_id
            -   fn_inputs.axonius_task_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["axonius_internal_axon_id", "axonius_write_attachment"], fn_inputs)

        axonius_client = AxoniusClient(self.rc, PACKAGE_NAME, self.options)

        results, error_msg = axonius_client.get_device_by_id(id=fn_inputs.axonius_internal_axon_id)

        if fn_inputs.axonius_write_attachment:
            # Get rest client, attachment name, and png content so we can write as an attachment
            rest_client = self.rest_client()
            if fn_inputs.axonius_attachment_name:
                attachment_name = fn_inputs.axonius_attachment_name
            else:
                attachment_name = "Axonius-Device-{}.json".format(results.get("internal_axon_id"))
            datastream = dumps(results, indent=4)

            # Write the file as an attachment
            write_file_attachment(rest_client, attachment_name, datastream, 
                                  fn_inputs.axonius_incident_id, fn_inputs.axonius_task_id)
            # If writing to an attachment only send the attachment name in the results.  The
            # JSON coming back from the endpoint is huge and scripting engine runs out of memory.
            results = { "attachment_name": attachment_name }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
