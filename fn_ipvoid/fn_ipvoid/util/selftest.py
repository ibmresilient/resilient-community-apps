# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_ipvoid
"""

import logging
import requests

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

BASE_URL = 'https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key={}&stats'

def get_config_option(option_name, opts, optional=False):
  """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
  option = opts.get(option_name)

  if not option and optional is False:
    err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this function".format(option_name)
    raise ValueError(err)
  else:
    return option

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_ipvoid", {})
    api_token = get_config_option("ipvoid_api_key", options)
    url = BASE_URL.format(api_token)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            log.info('elapsed_time:  %s', res.json()['elapsed_time'])
            log.info('credits_remained:  %s', res.json()['credits_remained'])
            log.info('credits_expiration:  %s', res.json()['credits_expiration'])
            log.info('estimated_queries:  %s', res.json()['estimated_queries'])
            log.info('estimated_queries:  %s', res.json()['estimated_queries'])
            return {"state": "success"}

        else:
            return {
            "state": "failure",
            "reason": res.json()["error"]
            }

    except Exception as e:
        log and log.error(e)
        return {
            "state": "failure",
            "reason": e
        }