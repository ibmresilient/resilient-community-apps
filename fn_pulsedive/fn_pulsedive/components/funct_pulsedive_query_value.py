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
    """Component that implements Resilient function 'pulsedive_query_value"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self._init_function(opts)

    def _init_function(self, opts):
        """ validate required fields for app.config """
        self.options = opts.get(CONFIG_SECTION, {})
        validate_fields(('pulsedive_api_key', 'pulsedive_api_url'), self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._init_function(opts)

    @function("pulsedive_query_value")
    def _pulsedive_query_value_function(self, event, *args, **kwargs):
        """Function: Query Pulsedive for information on an indicator/threat/feed value.
        inputs:
            incident_id: incident ID for attachment
            pulsedive_value: artifact type dns, ipadrs, or string
            pulsedive_query_type: specify "indicator", "threat", or feed
            pulsedive_feed_org: feed organization (for feed value only)
        return: json data

        """
        try:
            log = logging.getLogger(__name__)

            log.info("config params: %s", self.options)

            # Get the function parameters:
            pulsedive_value = kwargs.get("pulsedive_value")  # string
            pulsedive_query_type = self.get_select_param(
                kwargs.get("pulsedive_query_type"))  # select fld: Indicator, Threat, or Feed
            pulsedive_feed_org = kwargs.get("pulsedive_feed_org")  # string
            incident_id = kwargs.get("incident_id")     # integer
            if kwargs.get("attachment_name") is None:
                attachment_name = u"pulsedive_{}_{}.txt".format(
                    pulsedive_query_type, pulsedive_value)
            else:
                attachment_name = kwargs.get("attachment_name").replace(" ", "_")

            log.info("function params: pulsedive value = '%s', type = %s, feed org = '%s', \
                     incident = '%s', attachment = '%s'",
                     pulsedive_value, pulsedive_query_type, pulsedive_feed_org,
                     incident_id, attachment_name)

            yield StatusMessage("starting...")

            # form the url request
            api_url = "{}/info.php?".format(self.options["pulsedive_api_url"])
            pulsedive_data = {
                "key": self.options["pulsedive_api_key"]
            }

            # add type to url request:
            if pulsedive_query_type == "Feed":
                pulsedive_data["feed"] = pulsedive_value
                pulsedive_data["organization"] = pulsedive_feed_org
            elif pulsedive_query_type == "Threat":
                pulsedive_data["threat"] = pulsedive_value
            else:  # Indicator ID (default)
                pulsedive_data["indicator"] = pulsedive_value

            # make the api call
            rc = RequestsCommon(self.opts, self.options)    # initialize
            resp = rc.execute_call_v2("get",
                                      url=api_url,
                                      params=pulsedive_data
                                      )
            log.info("api response: %s", resp.json())

            # provide pretty-print format for readability in output
            pp = pprint.PrettyPrinter(indent=4)

            # prepare results to send for output
            results = {
                "url": api_url,
                "fn_inputs": {"value": pulsedive_value,
                              "query_type": pulsedive_query_type,
                              "feed_org": pulsedive_feed_org,
                              "attachment_name": attachment_name},
                "request_parameters": pulsedive_data,
                "content": resp.json(),
                "pretty": pp.pformat(resp.json())
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
