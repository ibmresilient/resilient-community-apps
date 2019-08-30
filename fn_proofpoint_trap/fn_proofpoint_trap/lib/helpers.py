# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Helper functions for Resilient circuits Functions supporting ProofPoint TRAP """

import requests
import json
import datetime
import logging
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

from resilient_circuits.actions_component import ResilientComponent

CONFIG_DATA_SECTION = "fn_proofpoint_trap"
log = logging.getLogger(__name__)
mandatory_config_params = ["base_url", "api_key", "polling_interval", "startup_interval", "state", "host_categories"]

def timestamp_minutes_ago(minutes):
    """
    Return ISO 8601 Timestamp of X minutes ago
    :param minutes:
    :return:
    """
    now = datetime.datetime.now()
    past = now - datetime.timedelta(minutes=minutes)
    return past.isoformat()

def transform_kwargs(kwargs):
    """"Update kwargs dictionary.
    This function will perform following actions:
        - Copy kwargs to a new 'params' dict which will be used to call the apis.
        - Strip whitespaces from beginning and end of parametrs in 'kwargs' and 'params' taking into
          account lists or dicts.
        - Remove "trap_" from beginning of parameters in 'params'.
        - Convert any case insensitive "None" values to None in 'params'.
    :param kwargs: Dictionary of Resilient Function parameters.

     """
    params = {}

    # Remove  "sep_" from the kwargs key names.
    for (k, v) in kwargs.copy().items():
        v = kwargs.pop(k)

        if isinstance(k, list):
            k = [ResilientComponent.get_select_param(val) for val in v]
        elif isinstance(v, dict):
            v = v.get("name")
        kwargs[k] = v.rstrip().lstrip() if isinstance(v, str)  else v
        params[k.split('_', 1)[1]] = v.rstrip().lstrip() if isinstance(v, str) \
                                                                and v.lower().startswith("trap_") else v

    # If any entry has "None" string change to None value for params.
    for k, v in params.items():
        if isinstance(v, str) and v.lower() == 'none':
            params[k] = None

    return params

def get_incident_list(options, lastupdate, bundle):
    """
    Grab incident list from TRAP
    :param options: - Configuration Options pulled from app.config
    :param lastupdate: - Minutes since last update
    :param bundle: - Pass bundle options or False
    :return:
    """
    base_url = options['base_url']
    api_key = options['api_key']
    headers = {'Authorization': api_key }
    # TODO: Possibly break out into different STATEs
    params = {}
    url = '{0}/incidents'.format(base_url)
    if type(lastupdate) is int:
        params['created_after'] = timestamp_minutes_ago(lastupdate)
    else:
        if lastupdate is None:
            # first run, fetch all
            log.info("First Run in progress - this may take a while.")

    try:
        res = requests.get(url, headers=headers, params=params, verify=bundle)

        res.raise_for_status()

        data = res.json()
        return data

    except requests.exceptions.Timeout:
        return {'error': 'request to {0} timed out'.format(url)}

    except requests.exceptions.TooManyRedirects:
        return {'error': 'URL redirection loop?'}

    except requests.exceptions.HTTPError as err:
        if err.response.content is not None:
            try:
                custom_error_content = json.loads(err.response.content)
            except JSONDecodeError:
                return {'error': '{}'.format(err)}
            return custom_error_content
        return {'error': 'HTTP error {}'.format(err)}

    except requests.exceptions.RequestException as ex:
        return {'error': 'request exception {}'.format(ex)}

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    for param in mandatory_config_params:
        param_value = func.options.get(param, None)

        if param_value is None:
            raise Exception("Mandatory config setting '{}' not set.".format(param))
        if not param_value:
            raise ValueError("Invalid value for config setting '{}'.".format(param))