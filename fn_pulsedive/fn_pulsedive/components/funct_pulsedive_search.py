# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import urllib.parse
import logging
from io import BytesIO
import pprint
from resilient_circuits import \
    (ResilientComponent, function, handler,
     StatusMessage, FunctionResult, FunctionError)
from resilient_lib import validate_fields, RequestsCommon, write_file_attachment, ResultPayload

CONFIG_SECTION = "fn_pulsedive"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'pulsedive_search"""

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

    @function("pulsedive_search")
    def _pulsedive_search_function(self, event, *args, **kwargs):
        """Function: Search Pulsedive for Indicators, Threats, or Feeds, using type-related filters."""
        try:
            log = logging.getLogger(__name__)

            log.info("config params: %s", self.options)

            # Get the function parameters:
            log.info("CAROL kwargs: %s", kwargs)
            incident_id = kwargs.get("incident_id")  # number
            pulsedive_search_value = kwargs.get("pulsedive_search_value").lower()
            pulsedive_search_type = self.get_select_param(kwargs.get("pulsedive_search_type"))  # select, values: "Indicator", "Threat", "Feed"
            pulsedive_indicator_type = self.get_select_param(kwargs.get("pulsedive_indicator_type"))  # multiselect, values: "Artifact", "Domain", "IP", "IPv6", "URL"
            pulsedive_risk = self.get_select_param(kwargs.get("pulsedive_risk"))  # multiselect, values: "Unknown", "None", "Low", "Medium", "High", "Critical", "Retired"
            # pulsedive_lastseen = self.get_select_param(kwargs.get("pulsedive_lastseen"))  # select, values: "day", "week", "month"
            temp_time = self.get_select_param(kwargs.get("pulsedive_lastseen"))
            if temp_time == "Last 24 hours":
                pulsedive_lastseen = "day"
            elif temp_time == "Last week":
                pulsedive_lastseen = "week"
            elif temp_time == "Last month":
                pulsedive_lastseen = "month"
            else:
                pulsedive_lastseen = ""     # all time

            # pulsedive_latest = self.get_select_param(kwargs.get("pulsedive_latest"))  # select, values: "latest", "historical"
            pulsedive_threat = kwargs.get("pulsedive_threat")  # text
            pulsedive_feed = kwargs.get("pulsedive_feed")  # text
            # pulsedive_limit = self.get_select_param(kwargs.get("pulsedive_limit"))  # select, values: "100 results", "1000 results", "10000 results"
            temp_limit = self.get_select_param(kwargs.get("pulsedive_limit"))
            if temp_limit == "100 results":
                pulsedive_limit = "hundred"
            elif temp_limit == "1000 results":
                pulsedive_limit = "thousand"
            elif temp_limit == "10000 results":
                pulsedive_limit = "tenthousand"

            pulsedive_category = self.get_select_param(kwargs.get("pulsedive_category"))  # multiselect, values: "General", "Abuse", "APT", "Attack", "Botnet", "Crime", "Exploit Kit", "Fraud", "Group", "Malware", "Proxy", "PUP", "RAT", "Reconnaissance", "Spam", "Phishing", "Terrorism", "Vulnerability"

            if kwargs.get("attachment_name") is None:
                attachment_name = u"pulsedive_search_{}.txt".format(pulsedive_search_type)
            else:
                attachment_name = kwargs.get("attachment_name").replace(" ", "_")

            log.info("incident_id: %s", incident_id)
            log.info("pulsedive_search_value: %s", pulsedive_search_value)
            log.info("pulsedive_search_type: %s", pulsedive_search_type)
            log.info("pulsedive_indicator_type: %s", pulsedive_indicator_type)
            log.info("pulsedive_risk: %s", pulsedive_risk)
            log.info("pulsedive_lastseen: %s", pulsedive_lastseen)
            # log.info("pulsedive_latest: %s", pulsedive_latest)
            log.info("pulsedive_threat: %s", pulsedive_threat)
            log.info("pulsedive_feed: %s", pulsedive_feed)
            log.info("pulsedive_limit: %s", pulsedive_limit)
            log.info("pulsedive_category: %s", pulsedive_category)
            log.info('attachment_name: %s', attachment_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # form the url request
            api_url = "{}/search.php?".format(self.options["pulsedive_api_url"])
            pulsedive_data = {}
            # add filters according to search type - Indicator, Threat, or Fee
            log.info("CAROL: search type: %s", pulsedive_search_type)
            if pulsedive_search_type == "Indicator":
                pulsedive_data["value"] = pulsedive_search_value
                pulsedive_data["type"] = ",".join(pulsedive_indicator_type)
                pulsedive_data["risk"] = ",".join(pulsedive_risk)
                pulsedive_data["threat"] = ",".join(pulsedive_threat)
                pulsedive_data["feed"] = ",".join(pulsedive_feed)
                pulsedive_data["limit"] = pulsedive_limit
                pulsedive_data["lastseen"] = pulsedive_lastseen
                # pulsedive_data["latest"] = pulsedive_latest
                # pulsedive_data["export"] = 1  # export to csv, for Indicator search only. Doesn't work.
            elif pulsedive_search_type == "Threat":
                pulsedive_data = {
                    "search": pulsedive_search_type.lower(),
                    "value": pulsedive_search_value.lower(),
                    "category[]": map(lambda x: x.lower(), pulsedive_category),
                    "risk[]": map(lambda x: x.lower(), pulsedive_risk)
                }
                # pulsedive_data["search"] = pulsedive_search_type
                # pulsedive_data["value"] = pulsedive_search_value
                # pulsedive_data["category[]"] = pulsedive_category
                # pulsedive_data["risk[]"] = pulsedive_risk
                # pulsedive_data["category"] = pulsedive_category
                # pulsedive_data["risk"] = pulsedive_risk
                # pulsedive_data["category"] = ",".join(pulsedive_category)
                # pulsedive_data["risk"] = ",".join(pulsedive_risk)

            else:   # Feed
                pulsedive_data["search"] = pulsedive_search_type
                pulsedive_data["value"] = pulsedive_search_value
                pulsedive_data["category"] = ",".join(pulsedive_category)

            pulsedive_data["key"] = self.options["pulsedive_api_key"]
            pulsedive_data["splitrisk"] = "1"

            log.info("CAROL data: %s", pulsedive_data)
            # make the api call
            rc = RequestsCommon(self.opts, self.options)    # initialize
            resp = rc.execute_call_v2("get",
                                      url=api_url,
                                      params=pulsedive_data
                                      # params=urllib.parse.urlencode(pulsedive_data, doseq=True)
                                      )
            log.info("api response: %s", resp.json())
            log.info("CAROL CODE %s", resp.status_code)
            log.info("CAROL content %s", resp.content)
            log.info("CAROL request %s", resp.request)
            log.info("request url: %s", resp.request.url)

            # get record counts to put in note summary
            summary_count = len(resp.json()["results"])

            # provide pretty-print format for readability in output
            pp = pprint.PrettyPrinter(indent=4)

            # prepare results to send for output
            results = {
                "url": api_url,
                # "request_url": resp.request.url,
                "fn_inputs": {"search_type": pulsedive_search_type,
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
