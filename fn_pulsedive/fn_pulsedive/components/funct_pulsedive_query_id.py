# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from io import BytesIO
import pprint
from resilient_circuits import (
    ResilientComponent, function, handler,
    StatusMessage, FunctionResult, FunctionError
)
from resilient_lib import validate_fields, RequestsCommon, write_file_attachment

CONFIG_SECTION = "fn_pulsedive"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pulsedive_query_id"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self._init_function(opts)

    def _init_function(self, opts):
        """ validate required fields for app.config """
        self.options = opts.get(CONFIG_SECTION, {})
        validate_fields(('pulsedive_api_key', 'pulsedive_api_url'), self.options)

    def _get_summary_count(self, key_name, resp_json):
        """ get counts from key stats to output to notes summary """
        summary_count = len(resp_json[key_name]) if key_name in resp_json.keys() else 0
        return summary_count

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._init_function(opts)

    @function("pulsedive_query_id")
    def _pulsedive_query_id_function(self, event, *args, **kwargs):
        """Function: Query Pulsedive for information on an indicator ID, threat ID, or feed ID.
        inputs:
            incident_id: incident ID for attachment
            pulsedive_id: an integer
            pulsedive_query_type: specify "indicator", "threat", or feed
            pulsedive_id_report: specify report requested based on id and type
        return: json data
        """
        try:
            log = logging.getLogger(__name__)

            log.info("config params: %s", self.options)

            # Get the function parameters:
            pulsedive_id = kwargs.get("pulsedive_id")  # number
            pulsedive_query_type = self.get_select_param(
                kwargs.get("pulsedive_query_type"))  # Indicator, Threat, or Feed
            pulsedive_id_report_type = self.get_select_param(kwargs.get(
                "pulsedive_id_report_type"))  # By ID, Links, Properties, Summary
            incident_id = kwargs.get("incident_id")     # integer
            if kwargs.get("attachment_name") is None:
                attachment_name = u"pulsedive_{}_{}.txt".format(
                    pulsedive_query_type, pulsedive_id)
            else:
                attachment_name = kwargs.get("attachment_name").replace(" ", "_")

            log.info("function params: pulsedive id = %s, type = %s, report = %s, \
                     incident='%s', attachment='%s'",
                     pulsedive_id, pulsedive_query_type, pulsedive_id_report_type,
                     incident_id, attachment_name)

            yield StatusMessage("starting...")

            # form the url request
            api_url = "{}/info.php?".format(self.options["pulsedive_api_url"])
            pulsedive_data = {
                "key": self.options["pulsedive_api_key"]
            }

            # add id to url request:
            if pulsedive_query_type == "Feed":
                pulsedive_data["fid"] = pulsedive_id
                # id_key = "fid"
            elif pulsedive_query_type == "Threat":
                pulsedive_data["tid"] = pulsedive_id
                # id_key = "tid"
            else:  # Indicator ID (default)
                pulsedive_data["iid"] = pulsedive_id
                # id_key = "iid"
            # pulsedive_data[id_key] = pulsedive_id

            # add report type to url request:
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

            # make the api call
            rc = RequestsCommon(self.opts, self.options)    # initialize
            resp = rc.execute_call_v2("get",
                                      url=api_url,
                                      params=pulsedive_data
                                      )
            log.info("api response: %s", resp.json())

            # get summary counts. Cull reports for stats we might be interested in
            # depending on query type (Indicator/Threat/Feed) and report type
            summary_count = {}
            key_list = []
            if pulsedive_id_report_type == "By ID":
                if pulsedive_query_type == "Indicator":
                    key_list = ["threats", "feeds"]
                if pulsedive_query_type == "Threat":
                    key_list = ["othernames", "news"]
            elif "Linked" in pulsedive_id_report_type:
                if pulsedive_query_type == "Indicator":
                    key_list = [x for x in resp.json().keys()]
                else:
                    key_list = ["results"]
            elif "Properties" in pulsedive_id_report_type:
                # this report only applies to Indicator ID
                if pulsedive_query_type == "Indicator":
                    key_list = [x for x in resp.json().keys()]
            elif "Summary" in pulsedive_id_report_type:
                key_list = ["results"]
            for x in key_list:
                summary_count[x] = self._get_summary_count(x, resp.json())

    # provide pretty-print format for readability in output
            pp = pprint.PrettyPrinter(indent=4)

            # prepare results to send for output
            results = {
                "url": api_url,
                "fn_inputs": {"report_type": pulsedive_id_report_type,
                              "query_type": pulsedive_query_type,
                              "query_id": pulsedive_id,
                              "attachment_name": attachment_name},
                "request_parameters": pulsedive_data,
                "content": resp.json(),
                "pretty": pp.pformat(resp.json()),
                "counts": summary_count
            }

            # Get the rest client so we can add the attachment to the incident
            client = self.rest_client()
            # Convert string to bytes and encode
            content = "content: {}".format(results["pretty"])
            datastream = BytesIO(content.encode("utf-8"))
            # Write the file as attachment: failures will raise an exception
            write_file_attachment(client, attachment_name, datastream=datastream,
                                  incident_id=incident_id, task_id=None)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

            yield StatusMessage("done...")
        except Exception as err:
            yield FunctionError(err)
