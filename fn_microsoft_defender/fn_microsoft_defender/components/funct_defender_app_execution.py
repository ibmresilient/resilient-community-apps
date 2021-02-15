# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information


"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME

FUNCTION = 'defender_app_execution'

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
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)

            # Get the function parameters:
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            defender_restriction_type = self.get_select_param(kwargs.get("defender_restriction_type"))  # select, values: "restrictCodeExecution", "unrestrictCodeExecution"
            action_description = kwargs.get("defender_description")  # text
            validate_fields(["defender_machine_id",
                             "defender_restriction_type",
                             "defender_description"], kwargs)

            log = logging.getLogger(__name__)
            log.info(u"defender_machine_id: %s", defender_machine_id)
            log.info(u"defender_restriction_type: %s", defender_restriction_type)
            log.info(u"defender_description: %s", action_description)


            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = {
                "Comment": action_description
            }
            log.debug(payload)

            # build the url
            url = "/".join([MACHINES_URL, defender_machine_id, defender_restriction_type])
            app_result, status, reason = defender_api.call(url, payload=payload, oper="POST")

            if not status:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            results = rp.done(status, app_result, reason=reason)

            yield StatusMessage("Finished 'defender_app_execution'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
