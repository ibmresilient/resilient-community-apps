# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_pagerduty.lib.resilient_common import validateFields, clean_html
from fn_pagerduty.lib.errors import IntegrationError
from .pd_common import create_note

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pagerduty_create_note"""

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


    @function("pagerduty_create_note")
    def _pagerduty_create_note_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # validate the function parameters:
            validateFields([u'pd_incident_id', u'pd_description'], kwargs)

            incident_id = kwargs.get(u'pd_incident_id')  # text
            description = clean_html(kwargs.get(u'pd_description'))  # text

            yield StatusMessage("starting...")
            resp = create_note(self.log, self.options, incident_id, description, self.create_note_callback)
            yield StatusMessage("pagerduty note created")

            # Produce a FunctionResult with the results - if not error, the response is not used
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(err)



    def create_note_callback(self, resp):
        """ handle results such as this
            {"error":{"message":"Invalid Input Provided","code":2001,"errors":["Content cannot be empty."]}}
        """
        result = resp.json()
        if 'error' in result and result['error']['code'] == 2001:
            msg = ": ".join((result['error']['message'], str(result['error']['errors'])))
            self.log.warning(msg)
            StatusMessage(msg)
            return {}
        else:
            raise IntegrationError(resp.text)
