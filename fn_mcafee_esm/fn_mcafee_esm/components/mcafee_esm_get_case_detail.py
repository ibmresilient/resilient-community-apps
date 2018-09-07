# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
import requests
import time
import json
from datetime import datetime
from threading import current_thread
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers, check_status_code


log = logging.getLogger(__name__)


def case_get_case_detail(options, headers, id):
    url = options["esm_url"] + "/rs/esm/v2/caseGetCaseDetail"

    payload = {
        "id": id
    }

    r = requests.post(url, headers=headers, data=json.dumps(payload), verify=options["trust_cert"])
    check_status_code(r.status_code)
    log.debug(r.json())

    return r.json()


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_get_case_detail"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_esm", {})

    @function("mcafee_esm_get_case_detail")
    def _mcafee_esm_get_case_detail_function(self, event, *args, **kwargs):
        """Function: """
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            options = self.options
            authenticated_headers = get_authenticated_headers(options["esm_url"], options["esm_username"],
                                               options["esm_password"], options["trust_cert"])

            # Get the function parameters:
            mcafee_esm_case_id = kwargs.get("mcafee_esm_case_id")  # number

            log = logging.getLogger(__name__)
            if not mcafee_esm_case_id:
                raise ValueError("mcafee_case_id is required")
            log.info("mcafee_esm_case_id: %s", mcafee_esm_case_id)

            # Get case details
            details = case_get_case_detail(options, authenticated_headers, mcafee_esm_case_id)

            end_time = time.time()
            results = {
                "inputs": {
                    "mcafee_esm_case_id": mcafee_esm_case_id
                },
                "metrics": {
                    "execution_time": str(end_time - start_time),
                    "function": "mcafee_esm_get_case_detail",
                    "thread": current_thread().name,
                    "timestamp": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                },
                "details": details
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
