# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_pagerduty.lib.resilient_common import validateFields, clean_html
from .pd_common import update_incident



class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pagerduty_transition_incident
        Transitioning an incident can be used to update specific fields (such as priority) or
        Change the status to acknowledged or resolved
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.res_options = opts.get("resilient", {})
        self.options = opts.get("pagerduty", {})
        validateFields(['api_token', 'from_email'], self.options)
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.res_options = opts.get("resilient", {})
        self.options = opts.get("pagerduty", {})
        validateFields(['api_token', 'from_email'], self.options)

    @function("pagerduty_transition_incident")
    def _pagerduty_transition_incident_function(self, event, *args, **kwargs):
        """Function: transition an indident"""
        try:
            validateFields(['pd_incident_id'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("pd_incident_id")  # text
            status = self.get_select_param(kwargs.get("pd_status"))  # select, values: "acknowledge", "resolve", "esclate"
            priority = kwargs.get("pd_priority")  # text
            resolution = clean_html(kwargs.get("pd_description"))  # text

            yield StatusMessage("starting...")
            resp = update_incident(self.log, self.options, incident_id, status, priority, resolution, self.callback)
            yield StatusMessage("pagerduty incident updated")

            # Produce a FunctionResult with the results
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(err)

    def callback(self, resp):
        """" handle the failure here """
        StatusMessage("Update failed. The PagerDuty Incident may have already been resolved.")