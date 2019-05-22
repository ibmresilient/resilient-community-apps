# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get policies. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_policies' of package fn_sep.

    The Function takes the following parameter:
        sep_policy_type, sep_domainid

    An example of a set of query parameter might look like the following:
            sep_policy_type = fw
            sep_domainid = None

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.
    {
         "inputs": {'sep_policy_type': {'name': 'fw', 'id': 201}},
         "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
                     'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1085},
         "success": True,
         "content":  {
                      "sort": null,
                      "number": 0,
                      "firstPage": true,
                      "content": [
                        {
                          "domainid": "908090000946C25D330E919313D23887",
                          "name": "Firewall policy",
                          "policytype": "fw",
                          "assignedtolocations": [
                            {
                              "defaultLocationId": "EC7E378A0946C25D39A1D3E8C5FB589B",
                              "locationIds": [
                                "EC7E378A0946C25D39A1D3E8C5FB589B"
                              ],
                              "groupId": "CAD80F000946C25D6C150831060AA326"
                            }
                          ],
                          "id": "846A39040946C25D3AA897754E2EC515",
                          "desc": "Created automatically during product installation."
                        },
                        {
                          "domainid": "908090000946C25D330E919313D23887",
                          "name": "Quarantine Firewall policy",
                          "subtype": null,
                          "enabled": true,
                          "sources": [],
                          "assignedtocloudgroups": null,
                          "policytype": "fw",
                          "assignedtolocations": null,
                          "id": "2867FBA60946C25D300A05176DC01DE0",
                          "desc": "Created automatically during product installation."
                        }
                      ],
                      "lastPage": true,
                      "totalPages": 1,
                      "size": 2,
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

    @function("fn_sep_get_policies")
    def _fn_sep_get_policies_function(self, event, *args, **kwargs):
        """Function: Get the policy summary for specified policy type; get the list of groups to which the policies are assigned"""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_policy_type = self.get_select_param(kwargs.get("sep_policy_type"))  # select, values: "av", "fw", "lu", "hi,", "hid adc", "ips", "exceptions"
            sep_domainid = kwargs.get("sep_domainid")  # text

            log = logging.getLogger(__name__)
            log.info("sep_policy_type: %s", sep_policy_type)
            log.info("sep_domainid: %s", sep_domainid)

            yield StatusMessage("Running Symantec SEP get computers query...")

            sep = Sepclient(self.options, params)

            rtn = sep.get_policies_summary(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning all 'computers' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
