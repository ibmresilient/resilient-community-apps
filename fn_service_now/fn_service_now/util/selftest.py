# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import logging
import json
from fn_service_now.util.resilient_helper import ResilientHelper

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    This test uses configs in the app.config file to call the custom '/test_connection' endpoint
    To try and get a status_code=200, else its a failure
    """
    options = opts.get("fn_service_now", {})
    
    res_helper = ResilientHelper(options)

    try:
        
      res = res_helper.sn_GET('/test_connection')

      status_code = res.status_code

      if status_code == 200:
        return {"state": "success"}

      else:

        if res is not None and res.content is not None:
          response_result = json.loads(res.content)
          err_msg = response_result["error"]["message"]
          err_detail = response_result["error"]["detail"]

        else:
          err_msg = "Could not connect to ServiceNow"
          err_detail = "Unknown"

        reason_msg = """Could not connect to ServiceNow.
        status_code: {0}
        reason: {1}
        detail: {2}
        ---------
        Configs::
        ---------
        sn_host: {3}
        sn_username: {4}\n""".format(status_code, err_msg, err_detail, res_helper.SN_HOST, res_helper.SN_USERNAME)

        log and log.error(reason_msg)

        return {
          "state": "failure",
          "reason": reason_msg
        }

    except Exception as e:
      log and log.error(e)
      return {
        "state": "failure",
        "reason": e
      }