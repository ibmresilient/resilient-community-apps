# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, INDICATOR_URL, PACKAGE_NAME

FUNCTION = "defender_delete_indicator"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_delete_indicator''"""

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
    def _defender_delete_indicator_function(self, event, *args, **kwargs):
        """Function: Delete an indicator from Defender ATP"""
        try:
            yield StatusMessage("Starting 'defender_delete_indicator'")
            # Validate required fields
            validate_fields(["defender_indicator_id"], kwargs)

            # Get the function parameters:
            defender_indicator_id = kwargs.get("defender_indicator_id")  # text

            log.info(f"defender_indicator_id: {defender_indicator_id}")

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            indicator_payload, status, reason = defender_api.call(
                "/".join([INDICATOR_URL, defender_indicator_id]), oper="DELETE")

            if not status:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            yield StatusMessage("Finished 'defender_list_indicators'")

            results = rp.done(status, indicator_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
