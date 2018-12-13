# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_apility
"""

import logging
import requests

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


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
    options = opts.get("fn_apility", {})
    base_url = get_config_option("url", options)
    api_token = get_config_option("api_token", options)

    HEADERS = {'content-type': 'application/json', 'X-Auth-Token': api_token}
    url = base_url+"badip/1.2.3.4"

    try:
      res = requests.get(url, headers=HEADERS)

      res.raise_for_status()
      
      if res.status_code == 200:
        return {"state": "success"}

      else:
        return {
          "state": "failure",
          "reason": "Status Code {0}".format(res.status_code)
        }

    except Exception as e:
      log and log.error(e)
      return {
        "state": "failure",
        "reason": e
      }