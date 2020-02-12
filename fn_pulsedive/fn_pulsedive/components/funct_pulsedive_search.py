# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from io import BytesIO
from resilient_circuits import \
    (ResilientComponent, function, handler,
     StatusMessage, FunctionResult, FunctionError)
from resilient_lib import validate_fields, RequestsCommon, write_file_attachment

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

    def _get_indicator_mapping(self, **kwargs):
        """
        Retrieve function inputs and create url parameters to search Indicators
        :param kwargs:
            value: filter by string. Can be comma-separated list. Blank returns all.
                field type: text
            type: filter by type of indicator. Defaults to all.
                field type: multiselect: "Artifact", "Domain", "IP", "IPv6", "URL"
            risk: filter by risk level. Ignore "Retired" as per PD dev suggestion. Defaults to all.
                field type: multiselect: "Unknown", "None", "Low", "Medium", "High", "Critical"
            attribute: filter by attributes, eg protocols or ports. Can be comma-separated list.
                field type: text
            property: filter by properties, eg content type. Can be comma-separated list.
                field type: text
            threat: filter by threat name. Can be comma-separated list.
                field type: text
            feed: filter by feed name. Can be comma-separated list.
                field type: text
            limit: option to limit number of indicators returned.
                field type: select, values: "100 results", "1000 results", "10000 results"
            pretty: option to pretty-print results (will be written to attachment)
                field type: select, values: "Yes", "No"
            lastseen: option to set scope of data
                field type: select, values: "day", "week", "month"
            (don't use this filter:
                export: option to export the Indicator search results to CSV
                Just add the link automatically)
            TODO:
            latest = usage unclear. Ignore for now.
        :return: dict of parameters
        """

        # convert the # of returns
        temp_limit = self.get_select_param(kwargs.get("pulsedive_limit"))
        limit_options = {"100 results": "hundred",
                         "1000 results": "thousand",
                         "10000 results": "tenthousand"}

        # convert time frame of returns
        temp_time = self.get_select_param(kwargs.get("pulsedive_lastseen"))
        time_options = {"Last 24 hours": "day", "Last week": "week", "Last month": "month"}

        # map action input fields to Pulsedive Indicator filters
        params_map = {
            "value[]": kwargs.get("pulsedive_search_value"),
            "type[]": self.get_select_param(kwargs.get("pulsedive_indicator_type")),
            "risk[]": self.get_select_param(kwargs.get("pulsedive_risk")),
            "attribute[]": kwargs.get("pulsedive_attribute"),
            "property[]": kwargs.get("pulsedive_property"),
            "threat[]": kwargs.get("pulsedive_threat"),
            "feed[]": kwargs.get("pulsedive_feed"),
            "limit": limit_options.get(temp_limit, "hundred"),
            "pretty": self.get_select_param(kwargs.get("pulsedive_pretty")),
            "lastseen": time_options.get(temp_time, ""),
            # "export": self.get_select_param(kwargs.get("pulsedive_export"))
        }
        return params_map

    def _get_threat_mapping(self, **kwargs):
        """
        Retrieve function inputs and create url parameters to search Threats
        :param kwargs:
            value: filter by string. Can be comma-separated list. Blank returns all.
                field type: text
            category: filter by 1 or more categories. Defaults to all categories.
                field type: multiselect, values: "General", "Abuse", "APT", "Attack", "Botnet",
                    "Crime", "Exploit Kit", "Fraud", "Group", "Malware", "Proxy", "PUP",
                    "RAT", "Reconnaissance", "Spam", "Phishing", "Terrorism", "Vulnerability"
            attribute: filter by attributes, eg protocol ir ports. Can be comma-separated list.
                field type: text
            property: filter by properties, eg content type. Can be comma-separated list.
                field type: text
            risk: filter by risk level. Ignore "Retired" as per PD dev suggestion. Defaults to all.
                field type: multiselect: "Unknown", "None", "Low", "Medium", "High", "Critical"
            splitrisk: option to split out indicator counts by risk
                field type: select, values: "Yes", "No"
            pretty: option to pretty-print results (will be written to attachment)
                field type: select, values: "Yes", "No"
            TODO:
            latest = usage unclear. Ignore for now.
        :return: dict of parameters
        """

        # map action input fields to Pulsedive Indicator filters
        params_map = {
            "search": "threat",
            "value[]": kwargs.get("pulsedive_search_value"),
            "category[]": self.get_select_param(kwargs.get("pulsedive_category")),
            "attribute[]": kwargs.get("pulsedive_attribute"),
            "property[]": kwargs.get("pulsedive_property"),
            "risk[]": self.get_select_param(kwargs.get("pulsedive_risk")),
            "splitrisk": self.get_select_param(kwargs.get("pulsedive_splitrisk")),
            "pretty": self.get_select_param(kwargs.get("pulsedive_pretty"))
        }
        return params_map

    def _get_feed_mapping(self, **kwargs):
        """
        Retrieve function inputs and create url parameters to search Feeds
        :param kwargs:
            value: filter by string. Can be comma-separated list. Blank returns all.
                field type: text
            category: filter by 1 or more categories. Defaults to all categories.
                field type: multiselect, values: "General", "Abuse", "APT", "Attack", "Botnet",
                    "Crime", "Exploit Kit", "Fraud", "Group", "Malware", "Proxy", "PUP",
                    "RAT", "Reconnaissance", "Spam", "Phishing", "Terrorism", "Vulnerability"
            splitrisk: option to split out indicator counts by risk
                field type: select, values: "Yes", "No"
            pretty: option to pretty-print results (will be written to attachment)
                field type: select, values: "Yes", "No"
        :return: dict of parameters
        """

        # map action input fields to Pulsedive Indicator filters
        params_map = {
            "search": "feed",
            "value[]": kwargs.get("pulsedive_search_value"),
            "category[]": self.get_select_param(kwargs.get("pulsedive_category")),
            "splitrisk": self.get_select_param(kwargs.get("pulsedive_splitrisk")),
            "pretty": self.get_select_param(kwargs.get("pulsedive_pretty"))
        }
        return params_map


    @function("pulsedive_search")
    def _pulsedive_search_function(self, event, **kwargs):
        """
        Function: Search Pulsedive for Indicators, Threats, or Feeds, using type-related filters.
        This function gets input values from the action rule activity fields and
        sends them to Pulsedive's Search endpoint https://pulsedive.com/api/?q=search.
        Results: a summary will be written to an incident note and
                 full details will be written to an incident attachment.
                 An option to export Indicator (only) search to CSV is provided in a link in Note.
        """
        try:
            log = logging.getLogger(__name__)

            log.info("config params: %s", self.options)

            # Get the function parameters:
            log.info("function params: %s", kwargs)

            incident_id = kwargs.get("incident_id")   # number

            # what type of search is requested
            pulsedive_search_type = self.get_select_param(
                kwargs.get("pulsedive_search_type"))  # select: "Indicator", "Threat", "Feed"

            # map action input filters to Pulsedive query filters
            if pulsedive_search_type == "Indicator":
                mapping = self._get_indicator_mapping(**kwargs)
            elif pulsedive_search_type == "Threat":
                mapping = self._get_threat_mapping(**kwargs)
            else:
                mapping = self._get_feed_mapping(**kwargs)

            # eliminate empty/null vars
            pulsedive_data = {}
            for k, v in mapping.items():
                if v is not None and v != "":
                    pulsedive_data[k] = v
            pulsedive_data["key"] = self.options["pulsedive_api_key"]
            log.info("%s parameters: %s", pulsedive_search_type, pulsedive_data)

            # set attachment name if user doesn't specify one
            if kwargs.get("attachment_name") is None:
                attachment_name = u"pulsedive_search_{}.txt".format(pulsedive_search_type)
            else:
                attachment_name = kwargs.get("attachment_name").replace(" ", "_")
            log.info("%s attachment name: %s", attachment_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # form the url request
            api_url = "{}/search.php?".format(self.options["pulsedive_api_url"])

            # make the api call
            rc = RequestsCommon(self.opts, self.options)    # initialize
            resp = rc.execute_call_v2("get",
                                      url=api_url,
                                      params=pulsedive_data
                                      )

            # prepare results to send for output
            results = {
                "search_type": pulsedive_search_type,
                "request_parameters": pulsedive_data,
                "request_url": resp.request.url,
                "attachment_name": attachment_name,
                "json": resp.json()
            }

            # Get the rest client so we can add the attachment to the incident
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

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

            yield StatusMessage("done...")
        except Exception as err:
            yield FunctionError(err)
