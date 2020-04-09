# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import hashlib
from fn_threatminer.lib.threatminer_common import ThreatMiner, PACKAGE
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_email_reverse"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE, {})
        self.threatminer = ThreatMiner(opts, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE, {})
        self.threatminer = ThreatMiner(opts, self.options)

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

            data, msg = self.threatminer.get(u'/email.php?q={}'.format(email_hash))

            yield StatusMessage(u"{} for {}".format(msg, email_address))

            yield StatusMessage("done...")

            results = {
                "findings": data
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
