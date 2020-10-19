# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
import time
from datetime import datetime
from threading import current_thread
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers, check_status_code


log = logging.getLogger(__name__)


def case_get_case_list(rc, options):
    url = options["esm_url"] + "/rs/esm/v2/caseGetCaseList"

    headers = get_authenticated_headers(rc, options["esm_url"], options["esm_username"],
                                        options["esm_password"], options["trust_cert"])

    r = rc.execute_call_v2('post', url, headers=headers, verify=options["trust_cert"], proxies=rc.get_proxies())
    check_status_code(r.status_code)

    return r.json()


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_get_list_of_cases"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_mcafee_esm", {})

    @function("mcafee_esm_get_list_of_cases")
    def _mcafee_esm_get_list_of_cases_function(self, event, *args, **kwargs):
        """Function: Calls the caseGetCaseList endpoint and returns a list of all cases that are open and
        assigned to the logged in user."""
        try:
            start_time = time.time()

            yield StatusMessage("starting...")

            options = self.options

            # Instantiate RequestsCommon object
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            # Call caseGetCaseList
            case_list = case_get_case_list(rc, options)
            if len(case_list) == 0:
                yield StatusMessage("No cases returned")
            else:
                yield StatusMessage("Case list returned")

            end_time = time.time()
            results = {
                "metrics": {
                    "execution_time": str(end_time - start_time),
                    "function": "mcafee_esm_get_list_or_cases",
                    "thread": current_thread().name,
                    "timestamp": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                },
                "case_list": case_list
            }
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
