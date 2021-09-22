# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, ALERTS_URL, ALERTS_EXPAND_PARAMS, PACKAGE_NAME

FUNCTION = "defender_update_alert"


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
            validate_fields(["tenant_id", "client_id", "app_secret"], self.options)
            validate_fields(["defender_alert_id", "defender_description"], kwargs)

            # Get the function parameters:
            defender_alert_status = self.get_select_param(kwargs.get("defender_alert_status"))  # select, values: "New", "InProgress", "Resolved"
            defender_alert_assigned_to = kwargs.get("defender_alert_assigned_to")  # text
            defender_description = kwargs.get("defender_description")  # text
            defender_alert_determination = self.get_select_param(kwargs.get("defender_alert_determination"))  # select, values: "Apt", "Malware", "NotAvailable", "SecurityPersonnel", "SecurityTesting", "UnwantedSoftware", "Other"
            defender_alert_classification = self.get_select_param(kwargs.get("defender_alert_classification"))  # select, values: "FalsePositive", "TruePositive", "Unknown"
            defender_alert_id = kwargs.get("defender_alert_id")  # text

            log = logging.getLogger(__name__)
            log.info("defender_alert_status: %s", defender_alert_status)
            log.info("defender_alert_assigned_to: %s", defender_alert_assigned_to)
            log.info("defender_description: %s", defender_description)
            log.info("defender_alert_determination: %s", defender_alert_determination)
            log.info("defender_alert_classification: %s", defender_alert_classification)
            log.info("defender_alert_id: %s", defender_alert_id)

            defender_api = DefenderAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts,
                                       self.options)

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            payload = {
                "comment": defender_description
            }
            if defender_alert_status:
                payload['status'] = defender_alert_status
            if defender_alert_assigned_to:
                payload['assignedTo'] = defender_alert_assigned_to
            if defender_alert_determination:
                payload['determination'] = defender_alert_determination
            if defender_alert_classification:
                payload['classification'] = defender_alert_classification
            log.debug(payload)

            # build the url
            url = "/".join([ALERTS_URL, defender_alert_id])
            alert_payload, status, reason = defender_api.call(url, payload=payload, oper="PATCH")

            if not status:
                yield StatusMessage(u"{} failure. Status: {} Reason: {}".format(FUNCTION, status, reason))

            yield StatusMessage("Finished 'defender_update_alert'")

            results = rp.done(status, alert_payload, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
