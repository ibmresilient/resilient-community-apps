# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""AppFunction implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, FunctionResult, StatusMessage
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, FILES_URL, PACKAGE_NAME

FN_NAME = "defender_get_file_information"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements function 'defender_get_file_information'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _defender_find_machines_by_file_function(self, event, *args, **kwargs):
        """
        Function: Get additional information about a Defender SHA1 or SHA256 file reference.
        Inputs:
            -   fn_inputs.defender_file_hash
        """
        try:
            yield StatusMessage(f"Starting '{FN_NAME}'")
            # Validate required fields
            validate_fields(["defender_file_hash"], kwargs)

            # Get the function parameters:
            defender_file_hash = kwargs.get("defender_file_hash")  # text

            log.info(f"defender_file_hash: {defender_file_hash}")

            # Get the function parameters:
            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                        self.options.get('client_id', None),
                                        self.options.get('app_secret', None),
                                        self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            file_result, status, reason = defender_api.call(
                FILES_URL.format(defender_file_hash), content_type=None)

            if not status:
                err_msg = f"{FN_NAME} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            results = rp.done(status, file_result, reason=reason)

            yield StatusMessage(f"Finished '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
