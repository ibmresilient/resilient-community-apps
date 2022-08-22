# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information

"""AppFunction implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINE_RECOMMENDATIONS_URL, PACKAGE_NAME

FN_NAME = "defender_machine_vulnerabilities"

class FunctionComponent(ResilientComponent):
    """Component that implements function 'defender_machine_recommendations'"""

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

    @function(FN_NAME)
    def _defender_machine_vulnerabilities(self, event, *args, **kwargs):
        """Function: Perform either an 'isolate' or 'unisolate' operation on a MS defender machine"""
        try:
            yield StatusMessage("Starting '{}'".format(FN_NAME))
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_machine_id"], kwargs)

            # Get the function parameters:
            defender_machine_id = kwargs.get("defender_machine_id")  # text

            log = logging.getLogger(__name__)
            log.info("defender_machine_id: %s", defender_machine_id)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            recommendation_payload, status, reason = defender_api.call(MACHINE_RECOMMENDATIONS_URL.format(defender_machine_id),
                                                                  content_type=None)

            yield StatusMessage("Finished '{}'".format(FN_NAME))

            results = rp.done(status, recommendation_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
