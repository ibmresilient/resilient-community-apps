# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import time
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_esm.util.helper import check_config, get_authentached_headers, check_status_code


def case_get_case_detail(options, id):
    url = options["esm_url"] + "/rs/esm/v2/caseGetCaseDetail"

    headers = get_authentached_headers(options["esm_url"], options["esm_username"],
                                       options["esm_password"], options["trust_cert"])
    payload = {
        "id": id
    }

    r = requests.post(url, headers=headers, data=json.dumps(payload), verify=options["trust_cert"])
    check_status_code(r.status_code)

    return r.json()


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_get_case_detail"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)
        case_get_case_detail(self.options, 4)

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
            # Get the function parameters:
            mcafee_esm_case_id = kwargs.get("mcafee_esm_case_id")  # number

            log = logging.getLogger(__name__)
            if not mcafee_esm_case_id:
                raise ValueError("mcafee_case_id is required")
            log.info("mcafee_case_id: %s", mcafee_esm_case_id)

            # Get case details
            details = case_get_case_detail(options, mcafee_esm_case_id)

            end_time = time.time()
            results = {
                "inputs": {
                    "mcafee_esm_case_id": mcafee_esm_case_id
                },
                "Run Time": str(end_time - start_time),
                "details": details
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
