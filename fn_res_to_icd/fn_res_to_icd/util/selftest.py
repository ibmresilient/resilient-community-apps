# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_res_to_icd
"""

import logging
import requests
import pprint

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
   """
   Placeholder for selftest function. An example use would be to test package api connectivity.
   Suggested return values are be unimplemented, success, or failure.
   """
   try:
      options = opts.get("fn_res_to_icd", {})
      icd_email=options.get("icd_email")
      icd_pass=options.get("icd_pass")
      log.info(icd_email)
      log.info(icd_pass)
      params = {"_lid": icd_email , "_lpwd": icd_pass }
      log.info('executing api call with credentials')
      response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/oslc/ping/", params=params,verify=False)
      log.info(response.status_code)
      return {"state": "success"}
   except Exception as err:
      log.error(err)
      return {"state": "failure"}


  