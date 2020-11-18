# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import readable_datetime, validate_fields, RequestsCommon, ResultPayload
from fn_cisco_enforcement.lib.enforcement_common import SECTION_NAME, HEADERS, callback

# This adds an event using the Cisco Event api. The inputs can be found with a description of the api here https://docs.umbrella.com/developer/enforcement-api/events2/
# The apikey is refernced in the app.config under [fn_cisco_enforcement]

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'get_domains"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_NAME, {})
        self.log = logging.getLogger(__name__)

        self._init()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_NAME, {})

        self._init()

    def _init(self):
        validate_fields(['api_token'], self.options)

        """get the api token for cisco access"""
        self.apikey = self.options.get('api_token')

    @function("cisco_get_domains")
    def _get_domains_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to gather the lists of domains already added to the shared customer’s domain list"""
        try:
            rp = ResultPayload(SECTION_NAME, **kwargs)

            # Get the function parameters:
            isnextpage = True
            page = 1

            url = '/'.join((self.options['url'], 'domains?customerKey={}'))
            url = url.format(self.apikey)
            self.log.debug(url)

            rc = RequestsCommon(self.opts, self.options)

            content = []
            while (isnextpage):
                self.log.info('Get page {}'.format(page))
                json_resp, msg = rc.execute_call_v2("get", url, headers=HEADERS, callback=callback)

                if msg:
                    self.log.error(msg)
                    yield FunctionError(u'Cisco Enforcement unexpected error: {}'.format(msg))
                elif not json_resp.get('data', None):
                    self.log.error(json_resp)
                    yield FunctionError('Cisco Enforcement result incomplete')
                else:
                    content.extend(json_resp['data'])
                    page += 1
                    if json_resp['meta']['next'] == False:
                        isnextpage = False
                    url = json_resp['meta']['next']

            # add a field to display date field in UTC format
            if content:
                yield StatusMessage("Get Domains found: {} was successful".format(len(content)))
                for result in content:
                    result['lastSeenAt_datetime'] = readable_datetime(result['lastSeenAt'], milliseconds=False)

            # add a field to allow the lastSeenAt field to be readable
            results = rp.done(False if msg else True, content, msg)
            results['value'] = content

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            self.log.error(err)
            yield FunctionError()
