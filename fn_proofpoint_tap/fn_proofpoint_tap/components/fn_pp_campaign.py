# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import os
from requests.exceptions import HTTPError
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib import RequestsCommon, validate_fields
from requests.auth import HTTPBasicAuth
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

log = logging.getLogger(__name__)


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
            validate_fields(['base_url', 'username', 'password'], self.options)

            base_url = self.options.get('base_url')
            username = self.options.get('username')
            password = self.options.get('password')
            cafile = self.options.get('cafile')
            bundle = os.path.expanduser(cafile) if cafile else False

            yield StatusMessage("configuration values OK")
            yield StatusMessage("Certificate verify {0}".format(bundle))

            basic_auth = HTTPBasicAuth(username, password)
            url = '{0}/campaign/{1}'.format(base_url, campaign_id)  # /v2/campaign/<campaignId> Fetch detailed information for a given campaign

            yield StatusMessage('Sending GET request to {0}'.format(url))

            res = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies(),
                                     callback=self.custom_response_err_msg)

            # Debug logging
            log.debug("Response content: {}".format(res.content))

            results['success'] = True
            results['data'] = res.json()
            results['href'] = url

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)

    def custom_response_err_msg(self, response):
        """
        Custom handler for response handling.
        :param response:
        :return: response
        """
        try:
            # Raise error is bad status code is returned
            response.raise_for_status()

            # Return requests.Response object
            return response

        except Exception as err:
            msg = str(err)

            if isinstance(err, HTTPError) and response.status_code == 404:
                msg = response.content + " please make sure you are invoking the appropriate Rule for chosen Artifact"

            log and log.error(msg)
            raise IntegrationError(msg)
