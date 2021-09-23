# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import logging
import re
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, INDICATOR_URL, PACKAGE_NAME

FUNCTION = "defender_list_indicators"

FILTER_FIELD_LOOKUP = {
    "type": "indicatorType",
    "value": "indicatorValue"
}

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
            log = logging.getLogger(__name__)

            yield StatusMessage("Starting 'defender_list_indicators'")
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)

            indicator_filter = kwargs.get('defender_indicator_filter')
            indicator_field = self.get_select_param(kwargs.get('defender_indicator_field'))
            log.info("defender_indicator_filter: %s", indicator_filter)
            log.info("defender_indicator_field: %s", indicator_field)

            # convert to field used by the API call
            indicator_field = FILTER_FIELD_LOOKUP.get(indicator_field, indicator_field)

            # Get the function parameters:
            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            indicator_payload, status, reason = defender_api.call(INDICATOR_URL, content_type=None)

            if status:
                yield StatusMessage("Indicators found: {}".format(len(indicator_payload['value'])))
                filtered_payload = filter_indicators(indicator_payload, indicator_field, indicator_filter)

                # convert dates to timestamps
                for indicator in filtered_payload['value']:
                    indicator['creationTimeDateTimeUtc_ts'] = convert_date(indicator['creationTimeDateTimeUtc'])
                    indicator['expirationTime_ts'] = convert_date(indicator['expirationTime'])
            else:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))
                filtered_payload = indicator_payload

            yield StatusMessage("Finished 'defender_list_indicators'")

            results = rp.done(status, filtered_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

def filter_indicators(indicator_payload, indicator_field, indicator_filter):
    """[filter results of the returned indicator using optional regex pattern]

    Args:
        indicator_payload ([dict]): [payload to parse]
        indicator_field ([text]): [field name to apply the filter]
        indicator_filter ([text]): [regex pattern to use]

    Returns:
        [dict]: [filtered list]
    """
    if not (indicator_filter and indicator_field):
        return indicator_payload

    reg = re.compile(indicator_filter)
    filtered_indicators = []
    for indicator in indicator_payload['value']:
        if reg.match(indicator[indicator_field]):
            filtered_indicators.append(indicator)

    return {"value": filtered_indicators}
