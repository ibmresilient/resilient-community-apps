# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation"""

import logging
import json
import os
import requests
from requests.auth import HTTPBasicAuth
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_proofpoint.util.helpers import get_config_option
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_pp_campaign"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get('fn_proofpoint', {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get('fn_proofpoint', {})

    @function("fn_pp_campaign")
    def _fn_pp_campaign_function(self, event, *args, **kwargs):
        """Function: Function to retrieve Campaign data from the ProofPoint API by Campaign ID"""

        log = logging.getLogger(__name__)

        # Get the function parameters:
        campaign_id = kwargs.get("campaign_id")  # text

        log.info("campaign_id: %s", campaign_id)

        yield StatusMessage("starting...")

        try:
            inputs = {
                'pp_campaign_id': campaign_id,
            }

            # payload = FunctionPayload(inputs)
            results = {
                'inputs': inputs,
                'success': False,
            }

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
            url = '{0}/campaign/{1}'.format(base_url, campaign_id)

            try:
                yield StatusMessage('Sending GET request to {0}'.format(url))

                res = requests.get(url, auth=basic_auth, verify=bundle)

                # Debug logging
                log.debug("Response status_code: {}".format(res.status_code))
                log.debug("Response content: {}".format(res.content))

                res.raise_for_status()

                if res.status_code == 200:
                    results['success'] = True
                    # results['data'] = json.loads(res.text)
                    results['data'] = json.dumps(json.loads(res.text), indent=4)
                    results['href'] = url
                else:
                    raise ValueError('request to {0} failed with code {1}'.format(url, res.status_code))

            except requests.exceptions.Timeout:
                raise ValueError('request to {0} timed out'.format(url))

            except requests.exceptions.TooManyRedirects:
                raise ValueError('URL redirection loop?', url)

            except requests.exceptions.HTTPError as err:
                if err.response.content is not None:
                    try:
                        custom_error_content = json.loads(err.response.content)
                    except JSONDecodeError:
                        raise ValueError(err)                    # raise ValueError(custom_error_content)
                    yield FunctionResult(custom_error_content)
                raise ValueError(err)

            except requests.exceptions.RequestException as ex:
                raise ValueError(ex)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
