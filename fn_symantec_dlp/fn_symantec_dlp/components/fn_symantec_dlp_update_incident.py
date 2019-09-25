# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json 

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
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
            # Get the wf_instance_id of the workflow this Function was called in

            res_payload = ResultPayload("fn_symantec_dlp_update", **kwargs)
            # Get the function parameters:
            sdlp_update_payload = self.get_textarea_param(kwargs.get("sdlp_update_payload"))  # textarea

            log = logging.getLogger(__name__)
            log.info("sdlp_update_payload: %s", sdlp_update_payload)

            if sdlp_update_payload is None:
                raise ValueError("Encountered error: sdlp_update_payload may not be None")

            updatepayload = json.loads(sdlp_update_payload)

            soap_client = DLPSoapClient(app_configs=self.options)

            
            resp = soap_client.update_incident_raw(**updatepayload)
            # Currently, there is nothing to return on the response that isin't an input
            # If we reach this line, we can assume we have made a succesful update as the update function has handling to ensure SUCCESS is returned
            results = res_payload.done(success=True, content={})

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
