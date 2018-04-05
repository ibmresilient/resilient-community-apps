# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
# Copyright IBM Corp. - Confidential Information
import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

# Deletes a domain using the Cisco api. The apikey is refernced in the app.config under [fn_cisco_enforcement]
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'delete_domain"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_enforcement", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_enforcement", {})

    @function("delete_domain")
    def _delete_domain_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to delete a domain from the shared customer’s domain list."""
        try:
            # Get the function parameters:
            cisco_domin = kwargs.get("cisco_domin")  # text
            apikey = self.options.get('apikey')
            log = logging.getLogger(__name__)
            log.info("cisco_domin: %s", cisco_domin)

            log.info('Deleting {} from list'.format(cisco_domin))
            deleteapi = 'https://s-platform.api.opendns.com/1.0/domains/{}?customerKey={}'.format(cisco_domin,apikey)
            respose = requests.delete(deleteapi)
            results = {
                "value": respose.content
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()