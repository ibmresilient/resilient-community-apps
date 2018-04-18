# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
import requests
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

HEADERS = {'content-type': 'application/json'}
# This adds an event using the Cisco Event api. The inputs can be found with a description of the api here https://docs.umbrella.com/developer/enforcement-api/events2/
# The apikey is refernced in the app.config under [fn_cisco_enforcement]

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'get_domains"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_enforcement", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_enforcement", {})

    @function("cisco_get_domains")
    def _get_domains_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to gather the lists of domains already added to the shared customer’s domain list"""
        try:
            # Get the function parameters:

            log = logging.getLogger(__name__)
            apikey = self.options.get('api_token')
            isnextpage = True
            resultlist = []
            page = 1

            url = '/'.join((self.options['url'], 'domains?customerKey={}'))
            url = url.format(apikey)
            log.debug(url)

            while (isnextpage):
                log.info('Get page {}'.format(page))
                response = requests.get(url, headers=HEADERS)

                if not response or response.status_code >= 300 or not response.content:
                    log.info(response)
                    yield FunctionError('api call failure: ' + str(response.status_code))
                else:
                    jsonversion = json.loads(response.content)

                    if not jsonversion.get('data', None):
                        log.info(jsonversion)
                        yield FunctionError('api result incomplete')
                    else:
                        resultlist.extend(jsonversion['data'])
                        page += 1
                        if (jsonversion['meta']['next'] == False):
                            isnextpage = False
                        url = jsonversion['meta']['next']

            log.info('Returning results')
            results = {
                "value": resultlist
            }
            log.debug(results)
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
