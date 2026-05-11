# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_cisco_enforcement.lib.enforcement_common import SECTION_NAME, HEADERS, callback

# Deletes a domain using the Cisco api. The apikey is refernced in the app.config under [fn_cisco_enforcement]
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'delete_domain"""

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

    @function("cisco_delete_domain")
    def _delete_domain_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to delete a domain from the shared customer’s domain list."""
        try:
            validate_fields(['cisco_domain'], kwargs)

            # Get the function parameters:
            cisco_domain = kwargs.get("cisco_domain")  # text

            self.log.info(u'Deleting {} from list'.format(cisco_domain))
            rp = ResultPayload(SECTION_NAME, **kwargs)

            url = '/'.join((self.options['url'], 'domains', '{}?customerKey={}'))
            url = url.format(cisco_domain.strip(), self.apikey)
            self.log.debug(url)

            rc = RequestsCommon(self.opts, self.options)
            content, msg = rc.execute_call_v2("delete", url, callback=callback)
            if msg:
                yield StatusMessage(msg)
            else:
                yield StatusMessage(u"Delete domain for '{}' was successful".format(cisco_domain))

            # Return the results
            results = rp.done(False if msg else True, None if msg else content, msg)
            # backward compatibility
            results['value'] = None if msg else content
            yield FunctionResult(results)
        except Exception as err:
            self.log.error(err)
            yield FunctionError()
