# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""
import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_enforcement.lib.resilient_common import validate_fields

HEADERS = {'content-type': 'application/json'}
# Deletes a domain using the Cisco api. The apikey is refernced in the app.config under [fn_cisco_enforcement]
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'delete_domain"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_enforcement", {})
        self.log = logging.getLogger(__name__)

        self._init()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_enforcement", {})

        self._init()

    def _init(self):
        validate_fields(['api_token'], self.options)

        """get the api token for cisco access"""
        self.apikey = self.options.get('api_token')

    @function("cisco_delete_domain")
    def _delete_domain_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to delete a domain from the shared customer’s domain list."""
        try:
            validate_fields(['cisco_domain'], kwargs)

            # Get the function parameters:
            cisco_domain = kwargs.get("cisco_domain")  # text

            self.log.info(u'Deleting {} from list'.format(cisco_domain))

            url = '/'.join((self.options['url'], 'domains', '{}?customerKey={}'))
            url = url.format(cisco_domain.strip(), self.apikey)
            self.log.debug(url)

            response = requests.delete(url)

            if response.status_code >= 300:
                resp = response.json()
                if response.status_code == 404:
                    response.content and self.log.warning(response.content)
                    yield StatusMessage(u"Cisco Enforcement issue: {}: {}".format(response.status_code, resp['message']))
                else:
                    response.content and self.log.error(response.content)
                    yield StatusMessage(u"Cisco Enforcement failure: {}: {}".format(response.status_code, resp['message']))
            else:
                results = {
                    "value": response.content.decode('latin1')
                }
                yield StatusMessage("Delete domain was successful")
                self.log.debug(response.content)

                # Produce a FunctionResult with the results
                yield FunctionResult(results)
        except Exception as err:
            self.log.error(err)
            yield FunctionError()
