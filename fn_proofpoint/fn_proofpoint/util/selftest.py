# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_proofpoint_campaign
"""

import logging
import os
import requests
from requests.auth import HTTPBasicAuth

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def get_config_option(option_name, opts, optional=False):
    """Given option_name, check if it is in appconfig.
       Raises ValueError if it is missing and mandatory.
    """
    option = opts.get(option_name)

    if not option and not optional:
        err = '"{0}" is mandatory and not set in the app.config file.'.format(option_name)
        raise ValueError(err)
    else:
        return option


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get('fn_proofpoint', {})

    base_url = get_config_option('base_url', options)
    username = get_config_option('username', options)
    password = get_config_option('password', options)
    cafile = options.get('cafile')
    bundle = os.path.expanduser(cafile) if cafile else False

    basic_auth = HTTPBasicAuth(username, password)
    url = '{0}/bad'.format(base_url)

    try:
        res = requests.get(
            url,
            auth=basic_auth,
            verify=bundle
        )

        res.raise_for_status()

        if res.status_code == 200:
            return {'state': 'success'}

        return {
            'state': 'failure',
            'reason': 'status code {0}'.format(res.status_code)
        }

    except Exception as ex:
        log.error(ex)
        return {
            'state': 'failure',
            'reason': ex
        }
