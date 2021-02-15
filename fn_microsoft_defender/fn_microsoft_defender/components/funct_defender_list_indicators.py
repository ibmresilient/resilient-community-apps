# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, INDICATOR_URL, PACKAGE_NAME

FUNCTION = "defender_list_indicators"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_list_indicators'"""

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
    def _defender_list_indicators_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            yield StatusMessage("Starting 'defender_list_indicators'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)

            # Get the function parameters:
            log = logging.getLogger(__name__)
            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            indicator_payload, status, reason = defender_api.call(INDICATOR_URL, content_type=None)

            # convert dates to timestamps
            if status:
                yield StatusMessage("Indicators found: {}".format(len(indicator_payload['value'])))
                for indicator in indicator_payload['value']:
                    indicator['creationTimeDateTimeUtc_ts'] = convert_date(indicator['creationTimeDateTimeUtc'])
                    indicator['expirationTime_ts'] = convert_date(indicator['expirationTime'])
            else:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_list_indicators'")

            results = rp.done(status, indicator_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
