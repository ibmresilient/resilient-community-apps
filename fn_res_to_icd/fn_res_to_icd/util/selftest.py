# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_res_to_icd
"""
import logging
import requests
from resilient_lib.components.resilient_common import validate_fields

log = logging.getLogger(__name__)
log.setlevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    try:
        options = opts.get("fn_res_to_icd", {})
        icd_email = options.get("icd_email")
        icd_pass = options.get("icd_pass")
        icd_url = options.get('icd_url')
        log.info(icd_email)
        params = {"_lid": icd_email, "_lpwd": icd_pass}
        validate_fields(['icd_email','icd_pass','icd_url'], options)
        log.info('executing api call with credentials')
        response = requests.post(icd_url, params=params, verify=False)
        log.info(response.status_code)
        return {"state": "success"}
    except Exception as err:
        log.error(err)
        return {"state": "failure"}  