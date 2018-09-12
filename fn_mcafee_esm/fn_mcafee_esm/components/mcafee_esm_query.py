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


def query_esm(options, headers, data):
    log.debug("Calling query_esm()")
    base_url = options["esm_url"]
    url = base_url + "/rs/esm/v2/qryExecuteDetail?type=EVENT&reverse=False"

    r = requests.post(url, headers=headers, data=data, verify=options["trust_cert"])
    check_status_code(r.status_code)

    # return r.json()
    result_dict = r.json()
    queryID = result_dict.get("resultID")

    # Check the query status
    qconf = {
        "resultID": queryID
    }
    qconf_json = json.dumps(qconf)

    status_dict = get_qry_status(options, headers, qconf_json)
    status = status_dict.get("percentComplete")
    while status != 100:
        time.sleep(10)
        status_dict = get_qry_status(options, headers, qconf_json)
        status = status_dict.get("percentComplete")

    total_records = status_dict.get("totalRecords")
    return qconf_json, total_records


def get_qry_status(options, headers, data):
    log.debug("Calling get_qry_status()")
    result = requests.post(options["esm_url"] + '/rs/esm/v2/qryGetStatus',
                           headers=headers, data=data, verify=options["trust_cert"])
    check_status_code(result.status_code)

    return result.json()


def get_results(options, session_header, qconf_json):
    log.debug("Calling get_results() with {}".format(qconf_json))
    result = requests.post(options["esm_url"] + '/rs/esm/v2/qryGetResults?startPos=0&numRows=100&reverse=false',
                           headers=session_header, data=qconf_json, verify=options["trust_cert"])
    check_status_code(result.status_code)

    return result.json()


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_get_list_of_cases"""

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

    @function("mcafee_esm_query")
    def _mcafee_esm_query_logs_function(self, event, *args, **kwargs):
        """Function: """
        try:
            start_time = time.time()
            yield StatusMessage("starting...")
            options = self.options
            authenticated_headers = get_authenticated_headers(options["esm_url"], options["esm_username"],
                                                              options["esm_password"], options["trust_cert"])

            # Get inputs
            mcafee_esm_qry_type = self.get_select_param(
                kwargs.get("mcafee_esm_qry_type", "EVENT"))  # select
            mcafee_esm_qry_config = self.get_textarea_param(kwargs.get("mcafee_esm_qry_config"))  # textarea

            # Log inputs
            if mcafee_esm_qry_type:
                log.info("mcafee_esm_qry_type: %s", mcafee_esm_qry_type)
            else:
                raise FunctionError("mcafee_esm_qry_type needs to be set")
            if mcafee_esm_qry_config:
                log.info("mcafee_esm_qry_config: %s", mcafee_esm_qry_config)
            else:
                raise FunctionError("mcafee_esm_qry_config needs to be set")

            # Query Logs
            qconf_json, total_records = query_esm(options, authenticated_headers, mcafee_esm_qry_config)

            query_result = None
            if total_records > 0:
                yield StatusMessage("{} records".format(str(total_records)))
                query_result = get_results(options, authenticated_headers, qconf_json)
            else:
                yield StatusMessage("No results returned")

            end_time = time.time()
            results = {
                "inputs": {
                    "mcafee_esm_qry_type": mcafee_esm_qry_type,
                    "mcafee_esm_qry_config": mcafee_esm_qry_config
                },
                "metrics": {
                    "execution_time": str(end_time - start_time),
                    "function": "mcafee_esm_query_logs",
                    "thread": current_thread().name,
                    "timestamp": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                },
                "result": query_result
            }
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
