# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_symantec_dlp_update_incident"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_symantec_dlp", {})


    @function("fn_symantec_dlp_update_incident")
    def _fn_symantec_dlp_update_incident_function(self, event, *args, **kwargs):
        """Function: """
        try:
            res_payload = ResultPayload("fn_symantec_dlp_update", **kwargs)

            # Get the function parameters:
            sdlp_update_payload = self.get_textarea_param(kwargs.get("sdlp_update_payload"))  # textarea

            validate_fields(['sdlp_update_payload'], kwargs)

            log = logging.getLogger(__name__)
            log.info("sdlp_update_payload: %s", sdlp_update_payload)

            # TODO: Should we put try catch logic to give a custom error or let the function fail if it can't parse
            updatepayload = json.loads(sdlp_update_payload)

            yield StatusMessage("Loaded and validated sdlp_update_payload successfully, now sending update request to DLP")

            soap_client = DLPSoapClient(app_configs=self.options)

            # If the user provides a status as a part of the payload, that status needs to exist on DLP
            # otherwise the call will complete without setting this status and could give the impression it worked
            # so if there is a status provided, call DLP to get a list of accepted Status values and ensure the given one is in this list
            if updatepayload.get('status'):
                log.info("A status property was provided with the update payload. This will be checked against the DLP Instance to ensure its a valid Status")
                available_status_values = soap_client.incident_status()
                if updatepayload['status'] not in available_status_values:
                    raise ValueError(u"Encountered Validation Error; the provided Status value was not found on the DLP Instance. These status values are active on DLP Instance : %s", available_status_values)

            # TODO: current resp is unused, should be renamed and used if we decide to use it or removed
            resp = soap_client.update_incident_raw(**updatepayload)
            # Currently, there is nothing to return on the response that isin't an input
            # If we reach this line, we can assume we have made a succesful update as the update function has handling to ensure SUCCESS is returned
            results = res_payload.done(success=True, content={})

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
