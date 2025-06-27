# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, readable_datetime, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, ALERTS_URL, EXPAND_PARAMS, PACKAGE_NAME

FUNCTION = "defender_alert_search"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_alert_search''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})
        validate_fields(["tenant_id", "client_id", "app_secret"], self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FUNCTION)
    def _defender_alert_search_function(self, event, *args, **kwargs):
        """Function: Return Defender alerts based on a set of search criteria"""
        try:
            yield StatusMessage("Starting 'defender_alert_search'")
            # Validate required fields
            validate_fields(["defender_machine_id"], kwargs)

            # Get the function parameters:
            defender_alert_severity = self.get_select_param(kwargs.get("defender_alert_severity"))  # select, values: "Informational", "Low", "Medium", "High"
            defender_alert_result_max = kwargs.get("defender_alert_result_max")  # number
            defender_machine_id = kwargs.get("defender_machine_id")  # text
            defender_alert_lastupdatetime = kwargs.get("defender_alert_lastupdatetime")  # datetimepicker
            defender_alert_creationdate = kwargs.get("defender_alert_creationdate")  # datetimepicker

            log.info(f"defender_alert_severity: {defender_alert_severity}")
            log.info(f"defender_alert_result_max: {defender_alert_result_max}")
            log.info(f"defender_machine_id: {defender_machine_id}")
            log.info(f"defender_alert_lastupdatetime: {defender_alert_lastupdatetime}")
            log.info(f"defender_alert_creationdate: {defender_alert_creationdate}")

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            params = {**EXPAND_PARAMS}
            filters = []

            if defender_alert_result_max:
                params['$top'] = defender_alert_result_max
            if defender_alert_severity:
                filters.append(f"severity+eq+'{defender_alert_severity}'")
            if defender_alert_lastupdatetime:
                filters.append(f"lastUpdateTime+ge+{readable_datetime(defender_alert_lastupdatetime)}")
            if defender_alert_creationdate:
                filters.append(f"alertCreationDate+ge+{readable_datetime(defender_alert_creationdate)}")

            if filters:
                params['$filter'] = "+and+".join(filters)

            log.debug(params)

            alert_payload, status, reason = defender_api.call(ALERTS_URL, payload=params)

            # Filter on machine id and convert dates to timestamps
            filtered_alerts = []
            if status:
                for alert in alert_payload.get('value', []):
                    # Filter on machine_id
                    if alert.get('machineId', None) == defender_machine_id:
                        filtered_alert = alert.copy()
                        filtered_alert['alertCreationTime_ts'] = convert_date(filtered_alert.get('alertCreationTime', None))
                        filtered_alert['firstEventTime_ts'] = convert_date(filtered_alert.get('firstEventTime', None))
                        filtered_alert['lastEventTime_ts'] = convert_date(filtered_alert.get('lastEventTime', None))
                        filtered_alert['lastUpdateTime_ts'] = convert_date(filtered_alert.get('lastUpdateTime', None))
                        filtered_alert['resolvedTime_ts'] = convert_date(filtered_alert.get('resolvedTime', None))
                        filtered_alerts.append(filtered_alert)
                alert_payload['value'] = filtered_alerts

                yield StatusMessage(f"Alerts found: {len(alert_payload.get('value', None))} for machine_id: {defender_machine_id}")
            else:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            yield StatusMessage("Finished 'defender_alert_search'")

            results = rp.done(status, alert_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
