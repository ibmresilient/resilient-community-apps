# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_sep
"""
import logging
import requests
import datetime
import os

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def timestamp_minutes_ago(minutes):
    """
    Return ISO 8601 Timestamp of X minutes ago
    :param minutes:
    :return:
    """
    now = datetime.datetime.now()
    past = now - datetime.timedelta(minutes=minutes)
    return past.isoformat()

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
    Simple test to verify ProofPoint Trap connectivity.
    """
    options = opts.get("fn_proofpoint_trap", {})
    base_url = get_config_option('base_url', options)
    api_key = get_config_option('api_key', options)
    headers = {'Authorization': api_key}

    cafile = options.get('cafile')
    bundle = os.path.expanduser(cafile) if cafile else False

    lastupdate = 60

    url = '{0}/incidents'.format(base_url)

    params = {
        "created_after": timestamp_minutes_ago(lastupdate)
    }

    try:
        res = requests.get(
            url,
            headers=headers,
            params=params,
            verify=bundle
        )
        res = requests.get(url, headers=headers, params=params, verify=bundle)
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