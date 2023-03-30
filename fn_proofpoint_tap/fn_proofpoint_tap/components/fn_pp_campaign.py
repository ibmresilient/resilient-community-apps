# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import os
from resilient_lib import RequestsCommon, validate_fields
from resilient_lib.components.integration_errors import IntegrationError
from requests.auth import HTTPBasicAuth
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_proofpoint_tap.util.proofpoint_common import custom_response_err_msg, PROOFPOINT_TAP_404_ERROR
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

        try:
            # Get the function parameters:
            campaign_id = kwargs.get("proofpoint_campaign_id")  # text

            log.info("proofpoint_campaign_id: %s", campaign_id)

            yield StatusMessage("Starting...")

            inputs = {
                'pp_campaign_id': campaign_id,
            }

            results = {
                'inputs': inputs,
                'success': False,
            }

            if campaign_id is None:
                raise FunctionError(u"campaign_id is required")

            yield StatusMessage("Function inputs OK")

            # Get configuration values
            validate_fields(['base_url', 'username', 'password'], self.options)

            base_url = self.options.get('base_url')
            username = self.options.get('username')
            password = self.options.get('password')
            cafile = self.options.get('cafile')
            bundle = os.path.expanduser(cafile) if cafile else False

            yield StatusMessage("Configuration values OK")
            yield StatusMessage(u"Certificate verify {0}".format(bundle))

            basic_auth = HTTPBasicAuth(username, password)
            url = '{0}/campaign/{1}'.format(base_url, campaign_id)  # /v2/campaign/<campaignId> Fetch detailed information for a given campaign
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            try:
                yield StatusMessage('Sending GET request to {0}'.format(url))
                res = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies(),
                                         callback=custom_response_err_msg)
                campaign = res.json()
                log.debug(u"Get Campaign Response content: {}".format(campaign))

                results['data'] = campaign
                results['success'] = True

                yield StatusMessage("Done...")
                # Produce a FunctionResult with the results
                yield FunctionResult(results)

            except IntegrationError as err:
                msg = err.value
                # If endpoint returns 404 workflow is not terminated - a Note with error msg is created instead
                if PROOFPOINT_TAP_404_ERROR in msg:
                    # clean the error value, remove \' and \\n
                    msg = msg.split("\'")[1].strip("\\n")
                    results['note_err_text'] = msg
                    results['success'] = False

                    yield StatusMessage("404 Client Error...")
                    # Produce a FunctionResult with the results
                    yield FunctionResult(results)
                else:
                    raise FunctionError(err)

        except Exception as err:
            yield FunctionError(err)
