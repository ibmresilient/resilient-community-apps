# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import requests
import time
from datetime import datetime
from threading import current_thread
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers, check_status_code


def case_get_case_events_details(options, ids):
    url = options["esm_url"] + "/rs/esm/v2/caseGetCaseEventsDetail"

    headers = get_authenticated_headers(options["esm_url"], options["esm_username"],
                                       options["esm_password"], options["trust_cert"])
    payload = {
        "eventIds": {
            "list": [ids]
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(payload), verify=options["trust_cert"])
    check_status_code(r.status_code)

    return r.json()


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_get_case_evensts_detail"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)
#        case_get_case_events_details(self.options, "144115188075855872|1422")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_esm", {})

    @function("mcafee_esm_get_case_events_detail")
    def _mcafee_esm_get_case_events_detail_function(self, event, *args, **kwargs):
        """Function: """
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            options = self.options
            # Get the function parameters:
            mcafee_event_ids_list = kwargs.get("mcafee_event_ids_list")  # text

            log = logging.getLogger(__name__)
            if not mcafee_event_ids_list:
                raise ValueError("mcafee_event_ids_list is required")
            log.info("mcafee_event_ids_list: %s", mcafee_event_ids_list)

            # Get case event details
            event_details = case_get_case_events_details(options, mcafee_event_ids_list)
            yield StatusMessage("Got event details")

            end_time = time.time()
            results = {
                "inputs": {
                    "mcafee_event_ids_list": mcafee_event_ids_list
                },
                "metrics": {
                    "execution_time": str(end_time - start_time),
                    "function": "mcafee_esm_get_case_events_detail",
                    "thread": current_thread().name,
                    "timestamp": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                },
                "event_details": event_details
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
