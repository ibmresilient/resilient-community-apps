# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME, MACHINE_ACTIONS_URL

FUNCTION = 'defender_app_execution'
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_app_execution''"""

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
    def _defender_app_execution_function(self, event, *args, **kwargs):
        """Function: Perform app restriction actions on a Microsoft Defender machine"""
        try:
            yield StatusMessage("Starting 'defender_app_execution'")

            # Get the function parameters:
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            defender_restriction_type = self.get_select_param(kwargs.get("defender_restriction_type"))  # select, values: "restrictCodeExecution", "unrestrictCodeExecution"
            action_description = kwargs.get("defender_description")  # text
            # Validate required fields
            validate_fields(["defender_machine_id", "defender_restriction_type", "defender_description"], kwargs)

            log.info(f"defender_machine_id: {defender_machine_id}")
            log.info(f"defender_restriction_type: {defender_restriction_type}")
            log.info(f"defender_description: {action_description}")

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = {"Comment": action_description}
            log.debug(payload)

            app_result, status, reason = defender_api.call(
                "/".join([MACHINES_URL, defender_machine_id, defender_restriction_type]),
                payload=payload, oper="POST")

            if status:
                # Get the uri for the report
                app_result, status, reason = defender_api.wait_for_action(
                    "/".join([MACHINE_ACTIONS_URL, app_result['id']]))

            if not status:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            results = rp.done(status, app_result, reason=reason)

            yield StatusMessage("Finished 'defender_app_execution'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
