# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from io import BytesIO
from resilient_circuits import (
    ResilientComponent, function, handler,
    StatusMessage, FunctionResult, FunctionError
)
from resilient_lib import validate_fields, RequestsCommon, ResultPayload, write_file_attachment

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

    def _get_mapping(self, query_type, **kwargs):
        """
        Retrieve function inputs and create url parameters to query Indicator by id
        :param kwargs:
            iid/tid/fid: filter by Pulsedive ID of an Indicator, Threat, or Feed
                field type: integer
            get: type of report to retrieve
                field type: select. Values: By ID, Linked Indicators, Properties, Indicator Summary
            pretty: option to pretty-print results (will be written to attachment)
                field type: select. Values: "Yes", "No"
            TODO:
            schema = usage unclear. Ignore for now.
        :return: dict of parameters
        """
        # add id to url request:
        if query_type == "Feed":
            query_key = "fid"
        elif query_type == "Threat":
            query_key = "tid"
        else:  # Indicator ID (default)
            query_key = "iid"

        # add report type and params to url request:
        rpt_type = self.get_select_param(kwargs.get("pulsedive_id_report_type"))
        summary = report_type = split = ""
        if "Linked" in rpt_type:
            report_type = "links"
        if "Properties" in rpt_type:
            report_type = "properties"
        if "Summary" in rpt_type:
            report_type = "links"
            summary = "1"
            split = "1"

        params_map = {
            query_key: kwargs.get("pulsedive_id"),
            "get": report_type,
            "summary": summary,
            "splitrisk": split,
            "pretty": self.get_select_param(kwargs.get("pulsedive_pretty"))
        }
        return params_map


    @function("pulsedive_query_id")
    def _pulsedive_query_id_function(self, event, *args, **kwargs):
        """Function: Query Pulsedive for information on an indicator ID, threat ID, or feed ID.
        This function gets input values from the action rule activity fields and
        sends them to Pulsedive's Query endpoint https://pulsedive.com/api/info.php
        Results: a summary will be written to an incident note and
                 full details will be written to an incident attachment.
        """
        try:
            log = logging.getLogger(__name__)

            log.info("config params: %s", self.options)

            # get query type: Indicator, Threat, or Feed
            pulsedive_id = kwargs.get("pulsedive_id")
            pulsedive_query_type = self.get_select_param(kwargs.get("pulsedive_query_type"))
            pulsedive_id_report_type = self.get_select_param(kwargs.get(
                "pulsedive_id_report_type"))

            # === get url parameters based on report type
            mapping = self._get_mapping(pulsedive_query_type, **kwargs)

            # eliminate empty/null vars
            pulsedive_data = {}
            for k, v in mapping.items():
                if v is not None and v != "":
                    pulsedive_data[k] = v
            # add key
            pulsedive_data["key"] = self.options["pulsedive_api_key"]
            log.info("%s parameters: %s", pulsedive_query_type, pulsedive_data)

            # === set incident parameters
            incident_id = kwargs.get("incident_id")     # integer
            if kwargs.get("attachment_name") is None:
                attachment_name = u"pulsedive_{}_id{}_{}.txt".format(
                    pulsedive_query_type, pulsedive_id, pulsedive_id_report_type)
            else:
                attachment_name = kwargs.get("attachment_name").replace(" ", "_")

            log.info("function params: pulsedive id = %s, type = %s, report = %s,\
                     incident='%s', attachment='%s'",
                     pulsedive_id, pulsedive_query_type, pulsedive_id_report_type,
                     incident_id, attachment_name)

            yield StatusMessage("starting...")

            # form the url request
            api_url = "{}/info.php?".format(self.options["pulsedive_api_url"])

            # === make the api call
            rp = ResultPayload(CONFIG_SECTION, **kwargs)
            rc = RequestsCommon(self.opts, self.options)    # initialize
            resp = rc.execute_call_v2("get",
                                      url=api_url,
                                      params=pulsedive_data
                                      )

            # === Get the rest client so we can add the attachment to the incident
            client = self.rest_client()

            # prepare datastream to output to attachment
            if pulsedive_data["pretty"] == "Yes":
                # Pulsedive returns pp format if requested. Convert to bytestream for file handling.
                datastream = BytesIO(resp.content)
            else:
                # Convert dict to string first, then convert to bytestream for file handling.
                ds = "{}".format(resp.json())
                datastream = BytesIO(ds.encode("utf-8"))

            # Write the file as attachment: failures will raise an exception
            write_file_attachment(client, attachment_name, datastream=datastream,
                                  incident_id=incident_id, task_id=None)

            # === prepare results
            resp_json = rp.done(True, resp.json())
            results = {
                "resp_json": resp_json,
                "att_name": attachment_name
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

            yield StatusMessage("done...")
        except Exception as err:
            yield FunctionError(err)
