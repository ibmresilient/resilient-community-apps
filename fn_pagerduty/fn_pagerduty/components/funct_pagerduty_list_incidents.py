# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""AppFunction implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, clean_html, IntegrationError
from .pd_common import list_incidents


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pagerduty_list_incidents"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.res_options = opts.get("resilient", {})
        self.options = opts.get("pagerduty", {})
        validate_fields(['api_token'], self.options)
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.res_options = opts.get("resilient", {})
        self.options = opts.get("pagerduty", {})
        validate_fields(['api_token'], self.options)

    @function("pagerduty_list_incidents")
    def _pagerduty_list_incidents_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # validate the function parameters:
            validate_fields([u'pd_incident_id'], kwargs)


            yield StatusMessage("starting...")
            resp = list_incidents(self.options)
            yield StatusMessage("pagerduty incidents listed")

            # Produce a FunctionResult with the results - if not error, the response is not used
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(err)

    def list_incident__callback(self, resp):
        """ handle results such as this
            {"error":{"message":"Invalid Input Provided","code":2001,"errors":["Content cannot be empty."]}}
        """
        result = resp.json()
        if 'error' in result and result['error']['code'] == 2001:
            msg = ": ".join((result['error']['message'],
                            str(result['error']['errors'])))
            self.log.warning(msg)
            StatusMessage(msg)
            return {}

        raise IntegrationError(resp.text)
