# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-falcon-sandbox
"""

import logging
import requests
from fn_falcon_sandbox.util.submit_helper import falcon_sandbox_request_header

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
   options = opts.get("fn_falcon_sandbox", {})
   API_KEY = str(get_config_option("falcon_sandbox_api_key", options))
   API_HOST = get_config_option("falcon_sandbox_api_host", options)

   headers = falcon_sandbox_request_header(API_KEY)
   url = "{}/key/current".format(API_HOST)
   try:
      res = requests.get(url, headers=headers)
      if res.status_code == 200:
         log.info(str(res))
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