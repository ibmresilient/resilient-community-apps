# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
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
            pulsedive_id_report: specify data requested
        return: json data
        """
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            pd_id = kwargs.get("pulsedive_id")  # number
            pulsedive_id_type = self.get_select_param(kwargs.get("pulsedive_id_type"))  # select, values: "Indicator", "Threat", "Feed"
            pulsedive_id_report_type = self.get_select_param(kwargs.get("pulsedive_id_report_type"))  # select, values: "General", "Linked Indicators", "Properties (using Indicator ID only)", "Indicator Summary (using Threat ID only)"

            log = logging.getLogger(__name__)
            log.info("pulsedive_id: {}".format(pd_id))
            log.info("pulsedive_id_type: {} ".format(pulsedive_id_type))
            log.info("pulsedive_id_report_type: {}".format(pulsedive_id_report_type))

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            log.info("api.config options: {}".format(self.options))

            # form the url request:
            if pulsedive_id_type == "Indicator":
                id_key = "iid"
            elif pulsedive_id_type == "Threat":
                id_key = "tid"
            else:   # Feed
                id_key = "fid"

            pulsedive_data = {
                id_key: pd_id
            }

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

            log.info("pulsedive_data: {}".format(pulsedive_data))

            # convert dict to list
            dict_list = []
            for k, v in pulsedive_data.items():
                dict_list.append("{}={}".format(k, v))
            # convert list to &-separated string
            url_form = "&".join(i for i in dict_list)

            # assemble the url
            request_url = "{}/info.php?{}&pretty=1&key={}".format(
                self.options["pulsedive_api_url"],
                url_form,
                self.options["pulsedive_api_key"]
            )

            log.info("request_url: {}".format(request_url))
            resp = requests.get(request_url)

            # headers = {
            #     "Content-type": "application/json",
            #     "key": self.options["pulsedive_api_key"]
            # }
            # resp = requests.get("https://pulsedive.com/api/info.php?",
            #                     data=json.dumps(pulsedive_data),
            #                     headers=headers)

            log.info("response: %s", resp.json())

            # Send back the results
            results = {
                "content": resp.json(),
                "url": request_url,
                "inputs": {"report_type": pulsedive_id_report_type,
                           "query type": pulsedive_id_type,
                           "query id": pd_id}
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

            yield StatusMessage("done...")
        except Exception as err:
            yield FunctionError(err)
