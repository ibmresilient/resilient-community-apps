# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get computers. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from time import time
from datetime import datetime

from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from fn_sep.lib.helpers import get_endpoints_status, get_endpoints_status_details
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError

FN_NAME = "fn_sep_get_computers"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_get_computers' of package fn_sep.

    The Function takes the following parameter:
            sep_computername, sep_domain, sep_lastupdate, sep_order, sep_os, sep_pageindex, sep_pagesize, sep_sort

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on endpoints and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            # Get the function parameters:
            sep_computername = getattr(fn_inputs, "sep_computername", None)  # text
            sep_status = getattr(fn_inputs, "sep_status", None)  # boolean
            sep_status_details = getattr(fn_inputs, "sep_status_details", None)  # boolean
            sep_domain = getattr(fn_inputs, "sep_domain", None)  # text
            sep_lastupdate = getattr(fn_inputs, "sep_lastupdate", None)  # text
            sep_order = getattr(fn_inputs, "sep_order", None)  # text
            sep_os = getattr(fn_inputs, "sep_os", None)  # text
            sep_pageindex = getattr(fn_inputs, "sep_pageindex", None)  # number
            sep_pagesize = getattr(fn_inputs, "sep_pagesize", None)  # number
            sep_sort = getattr(fn_inputs, "sep_sort", None)  # text
            sep_matching_endpoint_ids = getattr(fn_inputs, "sep_matching_endpoint_ids", None)  # boolean

            self.LOG.info("sep_computername: %s", sep_computername)
            self.LOG.info("sep_status: %s", sep_status)
            self.LOG.info("sep_status_details: %s", sep_status_details)
            self.LOG.info("sep_domain: %s", sep_domain)
            self.LOG.info("sep_lastupdate: %s", sep_lastupdate)
            self.LOG.info("sep_order: %s", sep_order)
            self.LOG.info("sep_os: %s", sep_os)
            self.LOG.info("sep_pageindex: %s", sep_pageindex)
            self.LOG.info("sep_pagesize: %s", sep_pagesize)
            self.LOG.info("sep_sort: %s", sep_sort)
            self.LOG.info("sep_matching_endpoint_ids: %s", sep_matching_endpoint_ids)

            yield self.status_message("Running Symantec SEP Get Computers query...")

            sep = Sepclient(self.options)

            rtn = sep.get_computers(computername=sep_computername,
                                    domain=sep_domain,
                                    lastupdate=sep_lastupdate,
                                    order=sep_order,
                                    os=sep_os,
                                    pageindex=sep_pageindex,
                                    pagesize=sep_pagesize,
                                    sort=sep_sort,
                                    status=sep_status,
                                    status_details=sep_status_details,
                                    matching_endpoint_ids=sep_matching_endpoint_ids)
            now = time()

            if "content" in rtn and rtn.get("content", []):
                # Add a human readable date stamp dict entry for timestamps for each computer.
                for i in range(len(rtn.get("content", []))):
                    for f in ["lastScanTime", "lastUpdateTime", "lastVirusTime"]:
                        try:
                            secs = int(rtn.get("content", [])[i][f]) / 1000
                            timediff = now - secs
                            ts_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                            # New keys will be "readableLastScanTime", "readableLastUpdateTime", "readableLastVirusTime"
                            rtn["content"][i]["readable"+f[0].capitalize()+f[1:]] = ts_readable
                            rtn["content"][i]["timediff" + f[0].capitalize() + f[1:]] = timediff
                        except ValueError:
                            yield FunctionError('A timestamp value was incorrectly specified.')

            if sep_matching_endpoint_ids:
                # Return only endpoint ids since post-processing may timeout processing large number of ids.
                content_copy = rtn.get("content", [])

                if not content_copy:
                    raise ValueError("Expected remediation result 'content' is empty")

                rtn["endpoints_matching_ids"] = []

                for i in range(len(content_copy)):
                    rtn["endpoints_matching_ids"].append(content_copy[i].get("uniqueId"))

                del content_copy
            elif sep_status:
                rtn, _non_compliant_endpoints = get_endpoints_status(rtn)
            elif sep_status_details:
                rtn = get_endpoints_status_details(rtn)

            yield self.status_message("Returning 'Get Computers' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(rtn)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
