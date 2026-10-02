# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, ALERTS_URL, PACKAGE_NAME

FUNCTION = "defender_update_alert"
log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'defender_update_alert''"""

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
    def _defender_update_alert_function(self, event, *args, **kwargs):
        """Function: Update a Defender Alert"""
        try:
            yield StatusMessage("Starting 'defender_update_alert'")
            # Validate required fields
            validate_fields(["defender_alert_id", "defender_description"], kwargs)

            # Get the function parameters:
            defender_alert_status = self.get_select_param(kwargs.get("defender_alert_status"))  # select, values: "New", "InProgress", "Resolved"
            defender_alert_assigned_to = kwargs.get("defender_alert_assigned_to")  # text
            defender_description = kwargs.get("defender_description")  # text
            defender_alert_determination = self.get_select_param(kwargs.get("defender_alert_determination"))  # select, values: "Apt", "Malware", "NotAvailable", "SecurityPersonnel", "SecurityTesting", "UnwantedSoftware", "Other"
            defender_alert_classification = self.get_select_param(kwargs.get("defender_alert_classification"))  # select, values: "FalsePositive", "TruePositive", "Unknown"
            defender_alert_id = kwargs.get("defender_alert_id")  # text

            log.info(f"defender_alert_status: {defender_alert_status}")
            log.info(f"defender_alert_assigned_to: {defender_alert_assigned_to}")
            log.info(f"defender_description: {defender_description}")
            log.info(f"defender_alert_determination: {defender_alert_determination}")
            log.info(f"defender_alert_classification: {defender_alert_classification}")
            log.info(f"defender_alert_id: {defender_alert_id}")

            defender_api = DefenderAPI(self.options.get('tenant_id', None),
                                       self.options.get('client_id', None),
                                       self.options.get('app_secret', None),
                                       self.opts, self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = {}

            if defender_description:
                payload['comment'] = defender_description
            if defender_alert_status:
                payload['status'] = defender_alert_status
            if defender_alert_assigned_to:
                payload['assignedTo'] = defender_alert_assigned_to
            if defender_alert_determination:
                payload['determination'] = defender_alert_determination
            if defender_alert_classification:
                payload['classification'] = defender_alert_classification
            log.debug(payload)

            alert_payload, status, reason = defender_api.call(
                "/".join([ALERTS_URL, defender_alert_id]), payload=payload, oper="PATCH")

            if not status:
                err_msg = f"{FUNCTION} failure. Status: {status} Reason: {reason}"
                yield StatusMessage(err_msg)
                raise IntegrationError(err_msg)

            yield StatusMessage("Finished 'defender_update_alert'")

            results = rp.done(status, alert_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
