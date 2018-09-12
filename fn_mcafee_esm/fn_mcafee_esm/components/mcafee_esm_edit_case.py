# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation"""

import logging
import time
import json
import requests
from datetime import datetime
from threading import current_thread
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers, check_status_code, merge_two_dicts
from fn_mcafee_esm.components.mcafee_esm_get_case_detail import case_get_case_detail


def case_edit_case_details(options, dict_payload, case_id):
    headers = get_authenticated_headers(options["esm_url"], options["esm_username"],
                                       options["esm_password"], options["trust_cert"])

    case_details = case_get_case_detail(options, headers, case_id)
    case_assigned_dict = dict(caseDetail={})
    case_assigned_dict["caseDetail"]["assignedTo"] = case_details.get("assignedTo")
    case_assigned_dict["caseDetail"]["orgId"] = case_details.get("orgId")

    dict_payload["caseDetail"] = merge_two_dicts(case_details, dict_payload["caseDetail"])

    url = options["esm_url"] + "/rs/esm/v2/caseEditCase"

    r = requests.post(url, headers=headers, data=json.dumps(dict_payload), verify=options["trust_cert"])
    check_status_code(r.status_code)


def combine_case_details(case_details, id):
    case_details_dict = json.loads(case_details)
    merge_dict = dict(caseDetail={})
    merge_dict["caseDetail"]["id"] = id

    if case_details_dict.get("caseDetail") is None:
        raise ValueError("caseDetail key was not set in json input.")

    return merge_two_dicts(case_details_dict["caseDetail"], merge_dict["caseDetail"])


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_edit_case"""

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

    @function("mcafee_esm_edit_case")
    def _mcafee_esm_edit_case_function(self, event, *args, **kwargs):
        """Function: """
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            options = self.options
            # Get the function parameters:
            mcafee_esm_case_id = kwargs.get("mcafee_esm_case_id")  # number
            mcafee_esm_edit_case_json = self.get_textarea_param(
                kwargs.get("mcafee_esm_edit_case_json", '{"caseDetail": {}}'))  # textarea

            log = logging.getLogger(__name__)
            if not mcafee_esm_case_id:
                raise ValueError("mcafee_case_id is required")
            log.info("mcafee_case_id: %s", mcafee_esm_case_id)

            if mcafee_esm_edit_case_json:
                log.info("mcafee_esm_edit_case_json: %s", mcafee_esm_edit_case_json)

            # Combine details to edit case
            edit_case_dict = dict(caseDetail={})
            edit_case_dict["caseDetail"] = combine_case_details(mcafee_esm_edit_case_json, mcafee_esm_case_id)

            # Edit Case, nothing is returned
            case_edit_case_details(options, edit_case_dict, mcafee_esm_case_id)
            yield StatusMessage("Case edited")

            end_time = time.time()
            results = {
                "metrics": {
                    "execution_time": str(end_time - start_time),
                    "function": "mcafee_esm_edit_case",
                    "thread": current_thread().name,
                    "timestamp": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                },
                "inputs": {
                    "mcafee_esm_edit_case_json": mcafee_esm_edit_case_json,
                    "mcafee_esm_case_id": mcafee_esm_case_id
                }
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
