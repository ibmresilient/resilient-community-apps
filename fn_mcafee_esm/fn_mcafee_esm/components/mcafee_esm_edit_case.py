# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
import json
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_esm.util.helper import check_config, get_authentached_headers, check_status_code, merge_two_dicts
from fn_mcafee_esm.components.mcafee_esm_get_case_detail import case_get_case_detail


def case_edit_case_details(options, dict_payload, case_id):
    case_details = case_get_case_detail(options, case_id)
    case_assigned_dict = dict(caseDetail={})
    case_assigned_dict["caseDetail"]["assignedTo"] = case_details.get("assignedTo")
    case_assigned_dict["caseDetail"]["orgId"] = case_details.get("orgId")

    dict_payload["caseDetail"] = merge_two_dicts(case_details, dict_payload["caseDetail"])

    url = options["esm_url"] + "/rs/esm/v2/caseEditCase"

    headers = get_authentached_headers(options["esm_url"], options["esm_username"],
                                       options["esm_password"], options["trust_cert"])

    r = requests.post(url, headers=headers, data=json.dumps(dict_payload), verify=options["trust_cert"])
    check_status_code(r.status_code)


def combine_case_details(case_details, **kwargs):
    case_details_dict = json.loads(case_details)
    merge_dict = dict(caseDetail={})
    merge_dict["caseDetail"]["id"] = kwargs.get("mcafee_esm_case_id")
    if kwargs.get("mcafee_esm_case_severity"):
        merge_dict["caseDetail"]["severity"] = kwargs.get("mcafee_esm_case_severity")
    if kwargs.get("mcafee_esm_case_summary"):
        merge_dict["caseDetail"]["summary"] = kwargs.get("mcafee_esm_case_summary")
    if kwargs.get("mcafee_esm_case_status"):
        merge_dict["caseDetail"].update({"statusId": {"value": kwargs.get("mcafee_esm_case_status")}})

    if case_details_dict.get("caseDetail") is None:
        raise ValueError("caseDetail key was not set in json input.")

    return merge_two_dicts(case_details_dict, merge_dict)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_edit_case"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)
#        case_edit_case_details(self.options, json.loads('{"something": "2"}'), 1)
#        case_edit_case_details(self.options, '{"caseDetail": {"summary": "This is a new summary","id": 1,"severity": 2}}')
#        case_edit_case_details(self.options, '{"caseDetail": {"severity" : 1,"summary" : "test3", "assignedTo" : 1, "orgId" : 1, "openTime" : "08/10/2018 19:18:43","id" : 1,"statusId" : {"value" : 1}} }')


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
            mcafee_esm_case_severity = kwargs.get("mcafee_esm_case_severity")  # number
            mcafee_esm_case_summary = kwargs.get("mcafee_esm_case_summary")  # textarea
            mcafee_esm_case_status = kwargs.get("mcafee_esm_case_status")  # number

            log = logging.getLogger(__name__)
            if not mcafee_esm_case_id:
                raise ValueError("mcafee_case_id is required")
            log.info("mcafee_case_id: %s", mcafee_esm_case_id)

            if mcafee_esm_edit_case_json:
                log.info("mcafee_esm_edit_case_json: %s", mcafee_esm_edit_case_json)
            if mcafee_esm_case_severity:
                log.info("mcafee_esm_case_severity: %s", mcafee_esm_case_severity)
            if mcafee_esm_case_summary:
                log.info("mcafee_esm_case_summary: %s", mcafee_esm_case_summary)
            if mcafee_esm_case_status:
                log.info("mcafee_esm_case_status: %s", mcafee_esm_case_status)

            # Combine details to edit case
            edit_case_dict = combine_case_details(mcafee_esm_edit_case_json, **kwargs)

            # Edit Case, nothing is returned
            case_edit_case_details(options, edit_case_dict, mcafee_esm_case_id)
            yield StatusMessage("Case edited")

            end_time = time.time()
            results = {
                "Run Time": str(end_time - start_time),
                "inputs": {
                    "mcafee_esm_edit_case_json": mcafee_esm_edit_case_json,
                    "mcafee_esm_case_id": mcafee_esm_case_id,
                    "mcafee_esm_case_severity": mcafee_esm_case_severity,
                    "mcafee_esm_case_summary": mcafee_esm_case_summary,
                    "mcafee_esm_case_status": mcafee_esm_case_status
                }
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
