# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME, MACHINE_ACTIONS_URL

FUNCTION = "defender_quarantine_file"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_quarantine_file''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FUNCTION)
    def _defender_quarantine_file_function(self, event, *args, **kwargs):
        """Function: Quarantine a SHA-1 File"""
        try:
            yield StatusMessage("Starting 'defender_quarantine_file'")
            # Validate required fields
            validate_fields(["defender_machine_id", "defender_description", "defender_indicator_value"], kwargs)

            # Get the function parameters:
            defender_description = kwargs.get("defender_description")  # text
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text

            log.info(f"defender_description: {defender_description}")
            log.info(f"defender_machine_id: {defender_machine_id}")
            log.info(f"defender_indicator_value: {defender_indicator_value}")

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = { "Sha1": defender_indicator_value, "Comment": defender_description}
            log.debug(payload)

            file_result, status, reason = defender_api.call(
                "/".join([MACHINES_URL, defender_machine_id, "StopAndQuarantineFile"]),
                payload=payload, oper="POST")

            if status:
                # Get the uri for the report
                file_result, status, reason = defender_api.wait_for_action(
                    "/".join([MACHINE_ACTIONS_URL, file_result['id']]))
            else:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            results = rp.done(status, file_result, reason=reason)

            yield StatusMessage("Finished 'defender_quarantine_file'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
