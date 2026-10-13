# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v52.0.0.0.927

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.amp_ratelimit import AmpRateLimit

PACKAGE_NAME = "fn_cisco_amp4ep"
FN_NAME = "fn_amp_computer_isolation"

ISOLATE = "isolate"
DEISOLATE = "de-isolate"
REFRESH = "refresh"

RATE_LIMITER = AmpRateLimit()

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_amp_computer_isolation'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Isolate/de-isolate a computer by connector guid or get isolation status.
        Inputs:
            -   fn_inputs.amp_conn_guid
            -   fn_inputs.amp_computer_isolation
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        if self.options.get("api_version", "").lower() == "v0":
            raise IntegrationError("Endpoint isolation endpoint is not available in API v0.")

        validate_fields(["amp_conn_guid",            # connector GUID
                         "amp_computer_isolation"],  # select, values: "isolate", "de-isolate", "refresh"
                         fn_inputs)
        amp_conn_guid = fn_inputs.amp_conn_guid
        isolation = fn_inputs.amp_computer_isolation.lower()

        self.LOG.debug("computer connector GUID: %s", amp_conn_guid)
        self.LOG.debug("isolation action: %s", isolation)

        amp = Ampclient(self.options, RATE_LIMITER)

        # determine which API method we need depending on desired action
        isolation_method = None
        if isolation == ISOLATE:
            isolation_method = "PUT"
        elif isolation == DEISOLATE:
            isolation_method = "DELETE"
        elif isolation == REFRESH:
            isolation_method = "GET"
        else:
            raise IntegrationError(f"Invalid request to isolate, de-isolate, or get status of computer with GUID {amp_conn_guid}. Request supplied: {isolation}")
        
        rtn = amp.manage_isolations(amp_conn_guid, method=isolation_method)
        
        self.LOG.debug(rtn)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"response": rtn}

        yield FunctionResult(results)

