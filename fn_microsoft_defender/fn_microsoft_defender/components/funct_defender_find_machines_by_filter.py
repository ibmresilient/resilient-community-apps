# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, MACHINES_URL, PACKAGE_NAME, make_filter_url

FUNCTION = "defender_find_machines_by_filter"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_find_machines_by_filter''"""

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
        """Function: Find Defender Machine(s) by filter"""
        try:
            yield StatusMessage("Starting 'defender_find_machines_by_filter'")
            # Validate required fields
            validate_fields(["defender_filter_name", "defender_filter_value"], kwargs)

            # Get the function parameters:
            defender_filter_name = kwargs.get("defender_filter_name")  # datepicker
            defender_filter_value = kwargs.get("defender_filter_value")  # text

            log.info(f"defender_filter_name: {defender_filter_name}")
            log.info(f"defender_filter_value: {defender_filter_value}")

            # HTTP GET  https://api.securitycenter.microsoft.com/api/machines?$filter=startswith(computerDnsName,'mymachine')
            # GET /api/machines/findbyip(ip='{IP}',timestamp={TimeStamp})
            url = make_filter_url(MACHINES_URL, defender_filter_name, defender_filter_value)

            # Get the function parameters:
            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            machines_result, status, reason = defender_api.call(url)

            # convert the timestamp
            if status:
                yield StatusMessage(f"Machines found: {len(machines_result.get('value', []))}")
                for machine in machines_result.get('value', []):
                    machine['firstSeen_ts'] = convert_date(machine.get('firstSeen', None))
                    machine['lastSeen_ts'] = convert_date(machine.get('lastSeen', None))
            else:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            yield StatusMessage("Finished 'defender_find_machines_by_filter'")

            results = rp.done(status, machines_result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
