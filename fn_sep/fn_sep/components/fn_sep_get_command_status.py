# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get command status. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import copy
import json
import logging
import time
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.sep_client import Sepclient
from fn_sep.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs, create_attachment, generate_scan_result_csv, \
    generate_remediate_result_csv
from fn_sep.lib.results_processing import process_results

LOG = logging.getLogger(__name__)
RESULTS_LIMIT_DEF = 200

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_command_status' of
    package fn_sep.

    The Function takes the following parameter:
            sep_commandid, sep_order, sep_pageindex, sep_pagesize, sep_sort

    An example of a set of query parameter might look like the following:
            sep_commandid = '7D3670DDF5A64A99B3721BF8A375B302'
            sep_order = None
            sep_pageindex = None
            sep_pagesize = None
            sep_sort = None
            sep_status_type = 'quarantine'

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        'inputs': {u'sep_status_type': u'quarantine', u'sep_commandid': u'7D3670DDF5A64A99B3721BF8A375B302'},
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-04-26 15:25:55', 'package_version': '1.0.0',
                      'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1256},
        'success': True,
        'content': {u'sort': [{u'direction': u'ASC', u'property': u'Begintime', u'ascending': True}],
                    u'command_state': 'Completed', u'number': 0, u'firstPage': True, ': 0,
                    u'content': [{u'computerName': u'Ep1', u'subStateId u'binaryFileId': None,
                                  u'lastUpdateTime': u'2019-04-26T11:05:27Z', u'domainName': u'Default',
                                  u'hardwareKey': u'DC7D24D6465566D2941F35BC8D17801E', u'subStateDesc': u'',
                                  u'stateId': 3, u'computerId': u'89AD1BBB0946C25D25E6C0984E971D8A',
                                  u'computerIp': u'192.168.194.94', u'beginTime': u'2019-04-26T11:05:27Z',
                                  u'currentLoginUserName': u'Administrator', u'resultInXML': u'',
                                  'command_status_id': 3}
                                 ],
                     u'lastPage': True, u'totalPages': 1, u'numberOfElements': 1, u'totalElements': 1, u'size': 20
                    },
        'raw': '{"sort": [{"direction": "ASC", "property": "Begintime", "ascending": true}],
                "command_state": "Completed", "number": 0, "firstPage": true,
                "content": [{"computerName": "Ep2", "subStateId": 0, "binaryFileId": null,
                "lastUpdateTime": "2019-04-26T11:05:27Z", "domainName": "Default",
                "hardwareKey": "DC7D24D6465566D2941F35BC8D17801E", "subStateDesc": "",
                "stateId": 3, "computerId": "89AD1BBB0946C25D25E6C0984E971D8A",
                "computerIp": "192.168.194.94", "beginTime": "2019-04-26T11:05:27Z",
                "currentLoginUserName": "Administrator", "resultInXML": "", "command_status_id": 3}],
                "lastPage": true, "totalPages": 1, "numberOfElements": 1, "totalElements": 1, "size": 20}',
        'reason': None,
        'version': '1.0'
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_sep_get_command_status")
    def _fn_sep_get_command_status_function(self, event, *args, **kwargs):
        """Function: Gets the details of a command status from a command id."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_incident_id = kwargs.get("sep_incident_id")  # number
            sep_commandid = kwargs.get("sep_commandid")  # text
            sep_order = kwargs.get("sep_order")  # text
            sep_pageindex = kwargs.get("sep_pageindex")  # number
            sep_pagesize = kwargs.get("sep_pagesize")  # number
            sep_sort = kwargs.get("sep_sort")  # text
            sep_status_type = kwargs.get("sep_status_type")  # text
            sep_matching_endpoint_ids = kwargs.get("sep_matching_endpoint_ids")  # boolean
            sep_scan_date = kwargs.get("sep_scan_date")  # text

            LOG.info("sep_incident_id: %s", sep_incident_id)
            LOG.info("sep_commandid: %s", sep_commandid)
            LOG.info("sep_order: %s", sep_order)
            LOG.info("sep_pageindex: %s", sep_pageindex)
            LOG.info("sep_pagesize: %s", sep_pagesize)
            LOG.info("sep_sort: %s", sep_sort)
            LOG.info("sep_status_type: %s", sep_status_type)
            LOG.info("sep_matching_endpoint_ids: %s", sep_matching_endpoint_ids)
            LOG.info("sep_scan_date: %s", sep_scan_date)

            validate_fields(["sep_commandid", "sep_status_type"], kwargs)

            yield StatusMessage("Running Symantec SEP Get Command Status query...")

            sep = Sepclient(self.options, params)

            rtn = process_results(sep.get_paginated_results(sep.get_command_status, **params), self.options,
                                  sep_status_type, sep_scan_date)
            if sep_status_type.lower() == "remediation" and rtn["total_remediation_count"] > 0:
                # Artifact may be remediated in multiple locations on multiple endpoints so send
                # back remediation details as an incident attachment
                # Get csv attachment file name and content.
                (file_name, file_content) = generate_remediate_result_csv(rtn, sep_commandid)

                yield StatusMessage(
                    "Adding remediation data for command id {} as an incident attachment {}".format(sep_commandid,
                                                                                                    file_name))
                # Create an attachment
                att_report = create_attachment(self.rest_client(), file_name, file_content, params["incident_id"])
                # Add attachment name to result
                rtn["att_name"] = att_report["name"]

            elif sep_status_type.lower() == "scan" and sep_matching_endpoint_ids:
                # Return only endpoint ids for artifact matches.
                content_copy = copy.deepcopy(rtn["content"])
                rtn = {"endpoints_matching_ids": []}
                for i in range(len(content_copy)):
                    rtn["endpoints_matching_ids"].append(content_copy[i]["computerId"])
                del content_copy
            elif sep_status_type.lower() == "scan" and rtn["total_match_count"] > int(
                    self.options.get("sep_results_limit", RESULTS_LIMIT_DEF)):
                # Over results limit. Send full result back as an attachment and also return an actual
                # result truncated to the results limit.
                results_limit = int(self.options.get("sep_results_limit", RESULTS_LIMIT_DEF))
                result_limit_complete = False
                total_match_count = 0
                match_types = ["HASH_MATCHES", "FULL_MATCHES", "PARTIAL_MATCHES"]

                yield StatusMessage(
                    "Adding EOC scan data for command id {} as an incident attachment".format(sep_commandid))
                # Get csv attachment file name and content.
                (file_name, file_content) = generate_scan_result_csv(rtn, sep_commandid)

                # Create an attachment
                att_report = create_attachment(self.rest_client(), file_name, file_content, params["incident_id"])

                # Truncate the result to 'results_limit'.
                content_copy = copy.deepcopy(rtn["content"])
                for i in range(len(content_copy)):
                    if result_limit_complete:
                        rtn["content"] = rtn["content"][:i]
                        break
                    else:
                        if total_match_count <= results_limit:
                            match_count = content_copy[i]["scan_result"]["match_count"]
                            if  total_match_count + match_count <= results_limit:
                                total_match_count += content_copy[i]["scan_result"]["match_count"]
                            else:
                                for match_type in match_types:
                                    if content_copy[i]["scan_result"][match_type]:
                                        # Truncate matches to limit value.
                                        rtn["content"][i]["scan_result"][match_type] = \
                                            content_copy[i]["scan_result"][match_type][:results_limit - total_match_count]
                                rtn["content"][i]["scan_result"]["match_count"] = results_limit - total_match_count
                                result_limit_complete = True

                rtn["scan_eoc_hits_over_limit"] = True
                rtn["att_name"] = att_report["name"]
                rtn["truncated_count"] = results_limit
                del content_copy
            else:
                yield StatusMessage("Returning 'Symantec SEP Get Command Status' results for command id {}"
                                    .format(sep_commandid))
            results = rp.done(True, rtn)

            LOG.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
