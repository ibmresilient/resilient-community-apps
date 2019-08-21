# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a ProofPoint TRAP query - get incident details. """

# Set up:
# Destination: a Queue named "fn_proofpoint_trap".
# Manual Action: Execute a REST query against a ProofPoint TRAP server.

import logging
import requests
import json
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_proofpoint_trap.lib.helpers import validate_opts
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_proofpoint_trap_get_incident_details"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_proofpoint_trap", {})
        validate_opts(self)
    @function("fn_proofpoint_trap_get_incident_details")
    def _fn_proofpoint_trap_get_incident_details_function(self, event, *args, **kwargs):
        """Function: Fetch Incident Details from Proofpoint TRAP"""

        # Get the function parameters:
        trap_incident_id = kwargs.get("trap_incident_id")  # number

        if trap_incident_id is None or not trap_incident_id:
            raise ValueError("Required field is missing or empty: "+"trap_incident_id")

        log = logging.getLogger(__name__)

        log.info("trap_incident_id: %s", trap_incident_id)

        yield StatusMessage("starting...")

        for yvalue in get_incident_details(self.options, trap_incident_id):
            yield yvalue



def get_config_option(options, option_name, optional=False):
    """Given option_name, check and return it if it is in appconfig.
       Raises ValueError if it is missing and mandatory
    """
    option = options.get(option_name)

    if not option and not optional:
        raise ValueError('"{0}" is mandatory and is not set in the app.config file'.format(option_name))

    return option

def get_incident_details(options, incident_id):
    try:
        inputs = {
            'trap_incident_id': incident_id,
        }

        # payload = FunctionPayload(inputs)
        results = {
            'inputs': inputs,
            'success': False,
        }

        yield StatusMessage("function inputs OK")

        # get configuration values
        base_url = get_config_option(options, 'base_url')
        api_key = get_config_option(options, 'api_key')
        cafile = options.get('cafile')
        bundle = os.path.expanduser(cafile) if cafile else False

        yield StatusMessage("configuration values OK")
        yield StatusMessage("Certificate verify {0}".format(bundle))

        headers = {'Authorization': api_key}
        url = '{0}/incidents/{1}.json'.format(base_url, incident_id)

        try:
            yield StatusMessage('Sending GET request to {0}'.format(url))

            res = requests.get(url, headers=headers, verify=bundle)

            res.raise_for_status()

            results['success'] = True
            # results['data'] = json.loads(res.text)
            results['data'] = res.json()
            results['href'] = url

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
