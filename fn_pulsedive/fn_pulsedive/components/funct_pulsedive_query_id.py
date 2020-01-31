# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import pprint
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pulsedive_query_id"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pulsedive", {})

    def _init_pulsedive(self):
        """ validate required fields for app.config """
        validate_fields(('pulsedive_api_key', 'pulsedive_api_url'), self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pulsedive", {})
        self._init_pulsedive()

    @function("pulsedive_query_id")
    def _pulsedive_query_id_function(self, event, *args, **kwargs):
        """Function: Query Pulsedive for information on an indicator ID, threat ID, or feed ID.
        inputs:
            pulsedive_id: an integer
            pulsedive_id_type: specify "indicator", "threat", or feed
            pulsedive_id_report: specify data requested based on id and type
        return: json data
        """
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            pd_id = kwargs.get("pulsedive_id")  # number
            pulsedive_id_type = self.get_select_param(
                kwargs.get("pulsedive_id_type"))  # "Indicator", "Threat", "Feed"
            pulsedive_id_report_type = self.get_select_param(kwargs.get(
                "pulsedive_id_report_type"))  # "General", "Linked Indicators", "Properties", "Indicator Summary"

            log = logging.getLogger(__name__)
            log.info("function params: pulsedive id = %s, type = %s, report = %s" %
                     (pd_id, pulsedive_id_type, pulsedive_id_report_type))
            log.info("config params: %s" % self.options)

            yield StatusMessage("starting...")

            # form the url request for id:
            if pulsedive_id_type == "Feed":
                id_key = "fid"
            elif pulsedive_id_type == "Threat":
                id_key = "tid"
            else:  # Indicator ID (default)
                id_key = "iid"

            pulsedive_data = {id_key: pd_id}

            # form the url request for report type:
            if "Linked" in pulsedive_id_report_type:
                # for all id types: indicator, threat, feed
                pulsedive_data["get"] = "links"
            if "Properties" in pulsedive_id_report_type:
                # for indicator id only
                pulsedive_data["get"] = "properties"
            if "Summary" in pulsedive_id_report_type:
                # for threat id only. 'splitrisk' (optional) lists counts by risk.
                pulsedive_data["get"] = "links"
                pulsedive_data["summary"] = "1"
                pulsedive_data["splitrisk"] = "1"

            # convert dict to list
            dict_list = []
            for k, v in pulsedive_data.items():
                dict_list.append("{}={}".format(k, v))
            # convert list to &-separated string
            url_form = "&".join(i for i in dict_list)

            # assemble the url
            request_url = "{}/info.php?{}&key={}".format(
                self.options["pulsedive_api_url"],
                url_form,
                self.options["pulsedive_api_key"]
            )

            # log.info("request_url: {}".format(request_url))
            # make the api call
            resp = requests.get(request_url)

            # headers = {
            #     "Content-type": "application/json",
            #     "key": self.options["pulsedive_api_key"]
            # }
            # resp = requests.get("https://pulsedive.com/api/info.php?",
            #                     data=json.dumps(pulsedive_data),
            #                     headers=headers)

            log.info("response: %s", resp.json())

            # provide pretty-print format for readability in output
            pp = pprint.PrettyPrinter(indent=4)

            # prepare results to send for output
            results = {
                "url": request_url,
                "inputs": {"report_type": pulsedive_id_report_type,
                           "query_type": pulsedive_id_type,
                           "query_id": pd_id},
                "content": resp.json(),
                "pretty": pp.pformat(resp.json())
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

            yield StatusMessage("done...")
        except Exception as err:
            yield FunctionError(err)
