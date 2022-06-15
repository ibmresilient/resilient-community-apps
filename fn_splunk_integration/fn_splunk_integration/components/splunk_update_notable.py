# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME
from fn_splunk_integration.util.function_utils import get_servers_list, function_basics
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "splunk_update_notable"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'splunk_update_notable"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = get_servers_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Update notable events according to the status of the corresponding incident.
        Inputs:
            event_id:   the notable event id in the splunk_notable_event_id field
            comment:    add a note to the notable event
            status:     Notable event status. Integer: 2=active, 5= closed
        """
        try:
            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["event_id"], fn_inputs)

            splunk, splunk_verify_cert = function_basics(fn_inputs, self.servers_list, utils=True)

            splunk_result = splunk.update_notable(event_id=fn_inputs.event_id,
                                                       comment=fn_inputs.comment,
                                                       status=fn_inputs.notable_event_status,
                                                       cafile=splunk_verify_cert)

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the return value
            yield FunctionResult(splunk_result.get('content', {}))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
