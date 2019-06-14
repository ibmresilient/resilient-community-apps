# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_res_to_icd
"""
import logging
import requests

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    try:
        options = opts.get("fn_res_to_icd", {})
        icd_email = options.get("icd_email")
        icd_pass = options.get("icd_pass")
        LOG.info(icd_email)
        LOG.info(icd_pass)
        params = {"_lid": icd_email, "_lpwd": icd_pass}
        LOG.info('executing api call with credentials')
        response = requests.post("https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2/oslc/ping/", params=params, verify=False)
        LOG.info(response.status_code)
        return {"state": "success"}
    except Exception as err:
        LOG.error(err)
        return {"state": "failure"}


  