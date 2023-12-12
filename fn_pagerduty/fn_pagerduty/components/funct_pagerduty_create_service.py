# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, clean_html, build_incident_url, build_resilient_url, unescape
from .pd_common import create_service


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pagerduty_create_service"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.res_options = opts.get("resilient", {})
        self.options = opts.get("pagerduty", {})
        validate_fields(['api_token', 'from_email'], self.options)
        self.log = logging.getLogger(__name__)


    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("pagerduty", {})
        validate_fields(['api_token', 'from_email'], self.options)
        self.res_options = opts.get("resilient", {})

    @function("pagerduty_create_service")
    def _pagerduty_create_service_function(self, event, *args, **kwargs):
        """Function: create a Service"""
        try:
            # validate required fields
            validate_fields(['pd_title', 'pd_escalation_policy'], kwargs)

            createDict = self._buildServicePayload(kwargs, self.options, self.res_options)
            
            yield StatusMessage("Starting Create Service...")
            resp = create_service(createDict)
            yield StatusMessage("Pagerduty Service Created")

            # Produce a FunctionResult with the results
            yield FunctionResult({"pd": resp})
        except Exception as err:
            yield FunctionError(str(err))


    def _buildServicePayload(self, kwargs, pd_options, res_options):
        # Get the function parameters:
        
        payloadDict = pd_options.copy()
        payloadDict['title'] = kwargs.get("pd_title")
        payloadDict['description'] = kwargs.get("pd_description")
        payloadDict['escalation_policy'] = kwargs.get("pd_escalation_policy")

        return payloadDict
