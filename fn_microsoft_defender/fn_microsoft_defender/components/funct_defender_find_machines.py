# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, readable_datetime, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, MACHINES_URL, PACKAGE_NAME

FUNCTION = "defender_find_machines"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_find_machines''"""

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
    def _defender_find_machines_function(self, event, *args, **kwargs):
        """Function: Find Defender Machine(s) by IP address"""
        try:
            yield StatusMessage("Starting 'defender_find_machines'")
            # Validate required fields
            validate_fields(["defender_indicator_value", "defender_lookback_timeframe"], kwargs)

            # Get the function parameters:
            defender_lookback_timeframe = kwargs.get("defender_lookback_timeframe")  # datepicker
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text

            log.info(f"defender_lookback_timeframe: {defender_lookback_timeframe}")
            log.info(f"defender_indicator_value: {defender_indicator_value}")

            # GET /api/machines/findbyip(ip='{IP}',timestamp={TimeStamp})
            timestamp_str = readable_datetime(defender_lookback_timeframe)
            query = f"findbyip(ip='{defender_indicator_value}',timestamp={timestamp_str})"

            # Get the function parameters:
            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            machines_result, status, reason = defender_api.call(
                "/".join([MACHINES_URL, query]), content_type=None)

            # convert the timestamp
            if status:
                yield StatusMessage(f"Machines found: {len(machines_result.get('value', []))}")
                for machine in machines_result.get('value', []):
                    machine['firstSeen_ts'] = convert_date(machine.get('firstSeen', None))
            else:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            yield StatusMessage("Finished 'defender_find_machines'")

            results = rp.done(status, machines_result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
