# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME, MACHINE_ACTIONS_URL

FUNCTION = "defender_machine_isolation"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_machine_isolation''"""

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
    def _defender_machine_isolation_function(self, event, *args, **kwargs):
        """Function: Perform either an 'isolate' or 'unisolate' operation on a MS defender machine"""
        try:
            yield StatusMessage("Starting 'defender_machine_isolation'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_machine_id",
                             "defender_description",
                             "defender_isolation_action"], kwargs)

            # Get the function parameters:
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            action_description = kwargs.get("defender_description")  # text
            defender_isolation_type = self.get_select_param(kwargs.get("defender_isolation_type"))  # select, values: "Full", "Selective"
            defender_isolation_action = self.get_select_param(kwargs.get("defender_isolation_action"))  # select, values: "isolate", "unisolate"

            log = logging.getLogger(__name__)
            log.info("defender_machine_id: %s", defender_machine_id)
            log.info("defender_isolation_type: %s", defender_isolation_type)
            log.info("defender_isolation_action: %s", defender_isolation_action)
            log.info("action_description: %s", action_description)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = {
                "Comment": action_description
            }
            if defender_isolation_action == 'isolate':
                payload["IsolationType"] = defender_isolation_type

            log.debug(payload)

            # build the url
            url = "/".join([MACHINES_URL, defender_machine_id, defender_isolation_action])
            isolate_result, status, reason = defender_api.call(url, payload=payload, oper="POST")

            if status:
                # get the uri for the report
                url = "/".join([MACHINE_ACTIONS_URL, isolate_result['id']])
                isolate_result, status, reason = defender_api.wait_for_action(url)

            if not status:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_machine_isolation'")

            results = rp.done(status, isolate_result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
