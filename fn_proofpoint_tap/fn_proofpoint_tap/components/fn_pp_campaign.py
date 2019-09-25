# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import os
from resilient_lib import RequestsCommon
from requests.auth import HTTPBasicAuth
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_proofpoint_tap.util.helpers import get_config_option
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_pp_campaign"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get('fn_proofpoint_tap', {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get('fn_proofpoint_tap', {})

    @function("fn_pp_campaign")
    def _fn_pp_campaign_function(self, event, *args, **kwargs):
        """Function: Function to retrieve Campaign data from the ProofPoint API by Campaign ID"""

        log = logging.getLogger(__name__)

        rc = RequestsCommon(opts=self.opts, function_opts=self.options)

        # Get the function parameters:
        campaign_id = kwargs.get("proofpoint_campaign_id")  # text

        log.info("proofpoint_campaign_id: %s", campaign_id)

        yield StatusMessage("starting...")

        try:
            inputs = {
                'pp_campaign_id': campaign_id,
            }

            results = {
                'inputs': inputs,
                'success': False,
            }

            if campaign_id is None:
                raise FunctionError(u"campaign_id is required")

            yield StatusMessage("function inputs OK")

            # get configuration values
            base_url = get_config_option(self.options, 'base_url')
            username = get_config_option(self.options, 'username')
            password = get_config_option(self.options, 'password')
            cafile = self.options.get('cafile')
            bundle = os.path.expanduser(cafile) if cafile else False

            yield StatusMessage("configuration values OK")
            yield StatusMessage("Certificate verify {0}".format(bundle))

            basic_auth = HTTPBasicAuth(username, password)
            url = '{0}/campaign/{1}'.format(base_url, campaign_id)  # /v2/campaign/<campaignId> Fetch detailed information for a given campaign

            yield StatusMessage('Sending GET request to {0}'.format(url))

            res = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies())

            # Debug logging
            log.debug("Response content: {}".format(res))

            results['success'] = True
            results['data'] = res
            results['href'] = url

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
