# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""
import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

HEADERS = {'content-type': 'application/json'}
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

    @function("cisco_delete_domain")
    def _delete_domain_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to delete a domain from the shared customer’s domain list."""
        try:
            # Get the function parameters:
            cisco_domain = kwargs.get("cisco_domain")  # text
            apikey = self.options.get('api_token')
            log = logging.getLogger(__name__)
            log.info("cisco_domain: %s", cisco_domain)

            log.info('Deleting {} from list'.format(cisco_domain))

            url = '/'.join((self.options['url'], 'domains', '{}?customerKey={}'))
            url = url.format(cisco_domain.strip(), apikey)
            log.debug(url)

            response = requests.delete(url)

            if not response or response.status_code >= 300:
                yield FunctionError('api call failure: '+ str(response.status_code))
            else:
                results = {
                    "value": response.content.decode('latin1')
                }
                log.debug(response.content)

                # Produce a FunctionResult with the results
                yield FunctionResult(results)
        except Exception:
            yield FunctionError()
