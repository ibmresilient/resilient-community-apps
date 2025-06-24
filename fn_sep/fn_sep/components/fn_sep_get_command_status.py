# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get command status. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from copy import deepcopy

from resilient_lib import validate_fields
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from fn_sep.lib.helpers import transform_kwargs, create_attachment, generate_scan_result_csv, generate_remediate_result_csv
from fn_sep.lib.results_processing import process_results
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_get_command_status"
RESULTS_LIMIT_DEF = 200

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_get_command_status' of package fn_sep.

    The Function takes the following parameter:
            sep_commandid, sep_order, sep_pageindex, sep_pagesize, sep_sort

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Gets the details of a command status from a command id."""
        try:
            # Validate the required inputs
            validate_fields(["sep_commandid", "sep_status_type"], fn_inputs)

            params = transform_kwargs(fn_inputs._asdict()) if fn_inputs._asdict() else {}

            # Get the function parameters:
            sep_incident_id = getattr(fn_inputs, "sep_incident_id", None)  # number
            sep_commandid = getattr(fn_inputs, "sep_commandid", None)  # text
            sep_order = getattr(fn_inputs, "sep_order", None)  # text
            sep_pageindex = getattr(fn_inputs, "sep_pageindex", None)  # number
            sep_pagesize = getattr(fn_inputs, "sep_pagesize", None)  # number
            sep_sort = getattr(fn_inputs, "sep_sort", None)  # text
            sep_status_type = getattr(fn_inputs, "sep_status_type", None)  # text
            sep_matching_endpoint_ids = getattr(fn_inputs, "sep_matching_endpoint_ids", None)  # boolean
            sep_scan_date = getattr(fn_inputs, "sep_scan_date", None)  # text

            self.LOG.info("sep_incident_id: %s", sep_incident_id)
            self.LOG.info("sep_commandid: %s", sep_commandid)
            self.LOG.info("sep_order: %s", sep_order)
            self.LOG.info("sep_pageindex: %s", sep_pageindex)
            self.LOG.info("sep_pagesize: %s", sep_pagesize)
            self.LOG.info("sep_sort: %s", sep_sort)
            self.LOG.info("sep_status_type: %s", sep_status_type)
            self.LOG.info("sep_matching_endpoint_ids: %s", sep_matching_endpoint_ids)
            self.LOG.info("sep_scan_date: %s", sep_scan_date)

            yield self.status_message("Running Symantec SEP Get Command Status query...")

            sep = Sepclient(self.options)

            results = process_results(sep.get_paginated_results(sep.get_command_status, **params),
                                      self.options,
                                      sep_status_type, sep_scan_date)

            if sep_status_type.lower() == "remediation" and results.get("total_remediation_count") > 0:
                # Artifact may be remediated in multiple locations on multiple endpoints so send
                # back remediation details as an incident attachment
                # Get csv attachment file name and content.
                (file_name, file_content) = generate_remediate_result_csv(results, sep_commandid)

                yield self.status_message(
                    f"Adding remediation data for command id {sep_commandid} as an incident attachment {file_name}")
                validate_fields(["sep_incident_id"], fn_inputs)
                # Create an attachment
                att_report = create_attachment(self.rest_client(),
                                               file_name, file_content,
                                               getattr(fn_inputs, "sep_incident_id", None))
                # Add attachment name to result
                results["att_name"] = att_report.get("name")

            elif sep_status_type.lower() == "scan" and sep_matching_endpoint_ids:
                # Return only endpoint ids for artifact matches.
                content_copy = results.get("content", [])

                if not content_copy:
                    raise ValueError("Expected remediation result 'content' is empty")

                results = {"endpoints_matching_ids": []}

                for i in range(len(content_copy)):
                    results["endpoints_matching_ids"].append(content_copy[i].get("computerId"))

                del content_copy
            elif sep_status_type.lower() == "scan" and results.get("total_match_count") > int(self.options.get("sep_results_limit", RESULTS_LIMIT_DEF)):
                # Over results limit. Send full result back as an attachment and also return an actual
                # result truncated to the results limit.
                results_limit = int(self.options.get("sep_results_limit", RESULTS_LIMIT_DEF))
                result_limit_complete = False
                total_match_count = 0
                match_types = ["HASH_MATCHES", "FULL_MATCHES", "PARTIAL_MATCHES"]

                yield self.status_message(
                    f"Adding EOC scan data for command id {sep_commandid} as an incident attachment")
                # Get csv attachment file name and content.
                file_name, file_content = generate_scan_result_csv(results, sep_commandid)

                validate_fields(["sep_incident_id"], fn_inputs)
                # Create an attachment
                att_report = create_attachment(self.rest_client(), file_name, file_content, getattr(fn_inputs, "sep_incident_id", None))

                # Truncate the result to 'results_limit'.
                content_copy = deepcopy(results.get("content"))
                for i in range(len(content_copy)):
                    if result_limit_complete:
                        results["content"] = results.get("content", [])[:i]
                        break
                    else:
                        if total_match_count <= results_limit:
                            match_count = content_copy[i].get("scan_result", {}).get("match_count")
                            if  total_match_count + match_count <= results_limit:
                                total_match_count += content_copy[i].get("scan_result", {}).get("match_count")
                            else:
                                for match_type in match_types:
                                    if content_copy[i].get("scan_result", {}).get(match_type):
                                        # Truncate matches to limit value.
                                        results["content"][i]["scan_result"][match_type] = \
                                            content_copy[i].get("scan_result", {}).get(match_type)[:results_limit - total_match_count]
                                results["content"][i]["scan_result"]["match_count"] = results_limit - total_match_count
                                result_limit_complete = True

                results["scan_eoc_hits_over_limit"] = True
                results["att_name"] = att_report.get("name")
                results["truncated_count"] = results_limit
                del content_copy
            else:
                yield self.status_message(f"Returning 'Symantec SEP Get Command Status' results for command id {sep_commandid}")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
