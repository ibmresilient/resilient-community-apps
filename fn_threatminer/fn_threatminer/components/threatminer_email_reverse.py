# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import hashlib
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_threatminer.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_email_reverse"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_threatminer", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_threatminer", {})

    @function("threatminer_email_reverse")
    def _threatminer_email_reverse_function(self, event, *args, **kwargs):
        """Function: Search Threatminer API to find data associated with an email address"""
        try:
            # Get the function parameters:
            email_address = kwargs.get("email_address")  # text

            log = logging.getLogger(__name__)
            log.info(u"email_address: %s", email_address)

            yield StatusMessage("starting...")

            m = hashlib.sha1()
            m.update(email_address.encode('utf-8'))

            email_hash = m.hexdigest()

            url = self.options.get('url', None)
            if not url:
                raise ValueError('missing url from [fn_threatminer] in app_config')

            response = requests.get('{}/email.php?q={}'.format(url, email_hash))

            if response.status_code == 200:
                yield StatusMessage('Results returned for {}'.format(email_address))
            elif response.status_code == 404:
                yield StatusMessage('No Results Returned for {}'.format(email_address))
            else:
                yield StatusMessage('Unexpected return code of {}'.format(response.status_code))

            email_findings = response.text

            yield StatusMessage("done...")

            results = {
                "findings": email_findings
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)