# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_pagerduty.lib.resilient_common import validateFields, clean_html, build_incident_url, build_resilient_url, unescape
from .pd_common import create_incident


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pagerduty_create_incident"""

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
        self.options = opts.get("pagerduty", {})
        validateFields(['api_token', 'from_email'], self.options)
        self.res_options = opts.get("resilient", {})

    @function("pagerduty_create_incident")
    def _pagerduty_create_incident_function(self, event, *args, **kwargs):
        """Function: create an incident"""
        try:
            # validate required fields
            validateFields(['incidentID', 'pd_title', 'pd_service', 'pd_escalation_policy'], kwargs)

            createDict = self._buildIncidentPayload(kwargs, self.options, self.res_options)
            #
            yield StatusMessage("starting...")
            resp = create_incident(self.log, createDict)
            yield StatusMessage("pagerduty incident created")

            # Produce a FunctionResult with the results
            yield FunctionResult({"pd": resp})
        except Exception as err:
            yield FunctionError(err)


    def _buildIncidentPayload(self, kwargs, pd_options, res_options):
        # Get the function parameters:
        incidentID = kwargs.get("incidentID")

        url = build_incident_url(build_resilient_url(self.res_options.get('host'), self.res_options.get('port')), incidentID)

        payloadDict = pd_options.copy()
        payloadDict['incidentID'] = incidentID
        payloadDict['title'] = unescape(kwargs.get("pd_title"))
        desc = self.get_textarea_param(kwargs.get("pd_description"))
        if desc:
            desc = clean_html(desc)
        else:
            desc = ''

        payloadDict['description'] = '\n'.join((url, desc))
        payloadDict['service'] = kwargs.get("pd_service")
        payloadDict['escalation_policy'] = kwargs.get("pd_escalation_policy")
        payloadDict['priority'] = kwargs.get("pd_priority")
        payloadDict['incident_key'] = kwargs.get("pd_incident_key")

        return payloadDict
