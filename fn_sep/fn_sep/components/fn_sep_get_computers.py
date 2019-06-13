# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get computers. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import copy
import json
import logging
import time

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs, get_endpoints_status, get_endpoints_status_details
from datetime import datetime

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_computers' of
    package fn_sep.

    The Function takes the following parameter:
            sep_computername, sep_domain, sep_lastupdate, sep_order, sep_os, sep_pageindex, sep_pagesize, sep_sort,

    An example of a set of query parameter might look like the following:
            sep_computername = None
            sep_status = None
            sep_status_details = None
            sep_domain = None
            sep_lastupdate = None
            sep_order = None
            sep_os = None
            sep_pageindex = None
            sep_pagesize = None
            sep_sort = None

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        "inputs": {"sep_computername": null, "sep_domain": null, "sep_lastupdate": null, "sep_order: null,
                       "sep_os": null, "sep_pageindex": null, "sep_pagesize": null, "sep_sort": null},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
        "host": 'myhost', 'version': '1.0', 'execution_time_ms': 1085},
        "success': True,
        "content" {
                  "sort": [
                    {
                      "direction": "ASC",
                      "property": "COMPUTER_NAME",
                      "ascending": true
                    }
                  ],
                  "number": 0,
                  "firstPage": true,
                  "content": [
                    {
                      ...
                      ...
                      "group": {
                        "domain": {
                          "id": "908090000946C25D330E919313D23887",
                          "name": "Default"
                        },
                        "name": "My Company",
                        "fullPathName": null,
                        "externalReferenceId": null,
                        "source": null,
                        "id": "CAD80F000946C25D6C150831060AA326"
                      },
                      "lastScanTime": 1550825941000,

                      "domainOrWorkgroup": "WORKGROUP",
                      ...
                      "infected": 0,
                      ...
                      ...
                      "idsChecksum": null,
                      "operatingSystem": "Windows Server 2012 ",
                      ...
                      "ipAddresses": [
                        "192.168.194.9ß3",
                        "FE80:0000:0000:0000:FC67:074E:CD22:0188"
                      ],
                      ...
                      ...
                      "computerName": "Ep1",
                      ...
                      ...
                      "uniqueId": "D31AA16E0946C25D40C83823C500518B",
                      ...
                      ...
                      "description": "",
                      ...
                      ...
                      "onlineStatus": 1,
                      ...
                      ...
                      "hardwareKey": "1771D79454E53469DF4B290C06C104C9",
                      ...
                    },
                    {
                        ...
                        ...
                    }
                  ],
                  "lastPage": true,
                  "totalPages": 1,
                  "size": 20,
                  "totalElements": 2,
                  "numberOfElements": 2
        },
        "raw": '<<a string representation of content.>>',
        "reason": None, 'version': '1.0'
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

    @function("fn_sep_get_computers")
    def _fn_sep_get_computers_function(self, event, *args, **kwargs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_computername = kwargs.get("sep_computername")  # text
            sep_status = kwargs.get("sep_status")  # boolean
            sep_status_details = kwargs.get("sep_status_details")  # boolean
            sep_domain = kwargs.get("sep_domain")  # text
            sep_lastupdate = kwargs.get("sep_lastupdate")  # text
            sep_order = kwargs.get("sep_order")  # text
            sep_os = kwargs.get("sep_os")  # text
            sep_pageindex = kwargs.get("sep_pageindex")  # number
            sep_pagesize = kwargs.get("sep_pagesize")  # number
            sep_sort = kwargs.get("sep_sort")  # text
            sep_matching_endpoint_ids = kwargs.get("sep_matching_endpoint_ids")  # boolean

            log = logging.getLogger(__name__)

            log.info("sep_computername: %s", sep_computername)
            log.info("sep_status: %s", sep_status)
            log.info("sep_status_details: %s", sep_status_details)
            log.info("sep_domain: %s", sep_domain)
            log.info("sep_lastupdate: %s", sep_lastupdate)
            log.info("sep_order: %s", sep_order)
            log.info("sep_os: %s", sep_os)
            log.info("sep_pageindex: %s", sep_pageindex)
            log.info("sep_pagesize: %s", sep_pagesize)
            log.info("sep_sort: %s", sep_sort)
            log.info("sep_matching_endpoint_ids: %s", sep_matching_endpoint_ids)

            yield StatusMessage("Running Symantec SEP Get Computers query...")

            sep = Sepclient(self.options, params)

            rtn = sep.get_computers(**params)
            now = time.time()

            if "content" in rtn and rtn["content"]:
                # Add a human readable date stamp dict entry for timestamps for each computer.
                for i in range(len(rtn["content"])):
                    for f in ["lastScanTime", "lastUpdateTime", "lastVirusTime"]:
                        try:
                            secs = int(rtn["content"][i][f]) / 1000
                            timediff = now - secs
                            ts_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                            # New keys will be "readableLastScanTime", "readableLastUpdateTime", "readableLastVirusTime"
                            rtn["content"][i]["readable"+f[0].capitalize()+f[1:]] = ts_readable
                            rtn["content"][i]["timediff" + f[0].capitalize() + f[1:]] = timediff
                        except ValueError:
                            yield FunctionError('A timestamp value was incorrectly specified.')

            if sep_matching_endpoint_ids:
                # Return only endpoint ids since post-processing may timeout processing large numer of ids.
                content_copy = copy.deepcopy(rtn["content"])
                rtn = {"endpoints_matching_ids": []}
                for i in range(len(content_copy)):
                    rtn["endpoints_matching_ids"].append(content_copy[i]["uniqueId"])
                del content_copy
            elif sep_status:
                rtn = get_endpoints_status(rtn)
            elif sep_status_details:
                rtn = get_endpoints_status_details(rtn)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Get Computers' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
