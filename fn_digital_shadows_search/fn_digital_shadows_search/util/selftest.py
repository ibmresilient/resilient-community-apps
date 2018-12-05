# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_digital_shadows_search
"""

import logging
import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
import json

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
    options = opts.get("fn_digital_shadows_search", {})

    api_key = get_config_option("ds_api_key", options)
    api_secret = get_config_option("ds_api_secret", options)
    base_url = get_config_option("ds_base_url", options)

    headers = {'content-type': 'application/json; charset=utf-8', 'Accept': 'application/json'}
    basic_auth = HTTPBasicAuth(api_key, api_secret)

    url = "{0}{1}".format(base_url, "/search/find")
    
    try:
      res = requests.post(
        url,
        json.dumps({"query": "8.8.8.8"}),
        auth=basic_auth,
        headers=headers,
        verify=True)

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
