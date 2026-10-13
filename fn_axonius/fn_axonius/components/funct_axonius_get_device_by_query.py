# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""
from json import (loads, dumps)
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (IntegrationError, validate_fields, write_file_attachment)
from fn_axonius.lib.axonius_client import (AxoniusClient)
from fn_axonius.lib.configure_tab import (init_axonius_tab)

PACKAGE_NAME = "fn_axonius"
FN_NAME = "axonius_get_device_by_query"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'axonius_get_device_by_query'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        init_axonius_tab()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the devices in Axonius that match the specified Axonius query string.  
                  Return the specified list of fields. If no fields names are specified, a 
                  default list of field names is returned.
        Inputs:
            -   fn_inputs.axonius_query_string
            -   fn_inputs.axonius_saved_query_name
            -   fn_inputs.axonius_field_name_list
            -   fn_inputs.axonius_device_limit
            -   fn_inputs.axonius_write_attachment
            -   fn_inputs.axonius_attachment_name
            -   fn_inputs.axonius_incident_id
            -   fn_inputs.axonius_task_id
        """
        validate_fields(["axonius_write_attachment"], fn_inputs)

        if not fn_inputs.axonius_query_string and not fn_inputs.axonius_saved_query_name:
            raise IntegrationError("Get Device by Query requires a query string OR an saved query name as a parameter.")

        axonius_client = AxoniusClient(self.rc, PACKAGE_NAME, self.options)

        fields = loads(fn_inputs.axonius_field_name_list) if fn_inputs.axonius_field_name_list else None
        assets, error_msg = axonius_client.get_device_by_query(query=fn_inputs.axonius_query_string,
                                                               saved_query_name=fn_inputs.axonius_saved_query_name,
                                                               fields=fields,
                                                               limit=fn_inputs.axonius_device_limit)
        # Fill in the endpoint URL for creating links back to Axonius in the post script
        results = {
            "assets": assets,
            "device_count": len(assets) if assets else 0,
            "endpoint_url": axonius_client.get_endpoint_url()
        }

        # Optionally write the results to an attachment
        if fn_inputs.axonius_write_attachment and not error_msg:
            # Get rest client, attachment name, and png content so we can write as an attachment
            rest_client = self.rest_client()
            if getattr(fn_inputs, "axonius_attachment_name", None):
                attachment_name = fn_inputs.axonius_attachment_name
            else:
                query_string = fn_inputs.axonius_saved_query_name if getattr(fn_inputs, "axonius_saved_query_name", None) else getattr(fn_inputs, "axonius_query_string", None)
                attachment_name = f"Axonius-Query-{query_string}.json"
            datastream = dumps(results, indent=4)

            # Write the file as an attachment
            write_file_attachment(rest_client, attachment_name, datastream, 
                                  fn_inputs.axonius_incident_id, fn_inputs.axonius_task_id)
            # If writing to an attachment only send the attachment name in the results.  The
            # JSON coming back from the endpoint is huge and scripting engine runs out of memory.
            results["attachment_name"] = attachment_name

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
