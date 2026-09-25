# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, FILES_URL_BY_MACHINE, PACKAGE_NAME

FUNCTION = "defender_find_machines_by_file"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_find_machines_by_file''"""

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
    def _defender_find_machines_by_file_function(self, event, *args, **kwargs):
        """Function: Find machines which match a given file hash"""
        try:
            yield StatusMessage("Starting 'defender_find_machines_by_file'")
            # Validate required fields
            validate_fields(["defender_indicator_value"], kwargs)

            # Get the function parameters:
            defender_indicator_value = kwargs.get("defender_indicator_value")  # text

            log.info(f"defender_indicator_value: {defender_indicator_value}")

            # Get the function parameters:
            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            machines_result, status, reason = defender_api.call(
                FILES_URL_BY_MACHINE.format(defender_indicator_value), content_type=None)

            # Convert dates to timestamps
            if status:
                yield StatusMessage(f"Machines found: {len(machines_result.get('value', []))}")
                for machine in machines_result.get('value', []):
                    machine['firstSeen_ts'] = convert_date(machine.get('firstSeen', None))
                    machine['lastSeen_ts'] = convert_date(machine.get('lastSeen', None))
            else:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            results = rp.done(status, machines_result, reason=reason)

            yield StatusMessage("Finished 'defender_find_machines_by_file'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
