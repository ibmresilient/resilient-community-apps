# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import time
import logging
import re
import fn_qradar_enhanced_data.util.qradar_constants as qradar_constants
from fn_qradar_enhanced_data.util import function_utils
from fn_qradar_enhanced_data.util.qradar_utils import QRadarClient
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_top_events"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_qradar_integration", {})
        required_fields = ["host", "verify_cert"]
        validate_fields(required_fields, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_qradar_integration", {})

    @function("qradar_top_events")
    def _qradar_top_events(self, event, *args, **kwargs):
        """Function: QRadar Top Events"""

        log = logging.getLogger(__name__)

        try:
            required_fields = ["qradar_query_type", "qradar_query"]
            validate_fields(required_fields, kwargs)
            # Get the function parameters:
            qradar_query = self.get_textarea_param(kwargs.get("qradar_query"))  # textarea
            qradar_fn_type = kwargs.get("qradar_query_type")  # text
            qradar_query_param1 = kwargs.get("qradar_query_param1")  # text
            qradar_query_param2 = kwargs.get("qradar_query_param2")  # text
            qradar_query_param3 = kwargs.get("qradar_query_param3")  # text
            qradar_query_param4 = kwargs.get("qradar_query_param4")  # text
            qradar_query_param5 = kwargs.get("qradar_query_param5")  # text
            qradar_query_param6 = kwargs.get("qradar_query_param6")  # text

            log.info("qradar_query: %s", qradar_query)
            log.info("qradar_query_param1: %s", qradar_query_param1)
            log.info("qradar_query_param2: %s", qradar_query_param2)
            log.info("qradar_query_param3: %s", qradar_query_param3)
            log.info("qradar_query_param4: %s", qradar_query_param4)
            log.info("qradar_query_param5: %s", qradar_query_param5)
            log.info("qradar_query_param6: %s", qradar_query_param6)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            timeout = float(self.options.get("search_timeout",600))  # Default timeout to 10 minutes

            log.debug("Connection to {} using {}".format(self.options["host"],
                                                         self.options.get("username", None) or self.options.get(
                                                             "qradartoken", None)))

            temp_table = "offense-{0}-events-{1}-1000-{2}".format(qradar_query_param3, qradar_fn_type,
                                                                  str(time.time()))

            qradar_temp_query = re.sub("FROM\s+{}".format(qradar_constants.ARIEL_SEARCH_EVENTS if re.search(qradar_constants.ARIEL_SEARCH_EVENTS,qradar_query, flags=re.IGNORECASE) else qradar_constants.ARIEL_SEARCH_FLOWS),
                                       "FROM {} INTO \"{}\"".format(qradar_constants.ARIEL_SEARCH_EVENTS if re.search(qradar_constants.ARIEL_SEARCH_EVENTS,qradar_query, flags=re.IGNORECASE) else qradar_constants.ARIEL_SEARCH_FLOWS, temp_table),
                                       qradar_query, flags=re.IGNORECASE)

            qradar_search_query = re.sub("FROM\s+{}".format(qradar_constants.ARIEL_SEARCH_EVENTS if re.search(qradar_constants.ARIEL_SEARCH_EVENTS,qradar_query, flags=re.IGNORECASE) else qradar_constants.ARIEL_SEARCH_FLOWS),
                                         "FROM \"{}\"".format(temp_table),
                                         qradar_query, flags=re.IGNORECASE)


            temp_query_string = function_utils.make_query_string(qradar_temp_query,
                                                                 ["*",
                                                                  qradar_query_param2,
                                                                  qradar_query_param3,
                                                                  " ",
                                                                  " ",
                                                                  " "])

            search_query_string = function_utils.make_query_string(qradar_search_query,
                                                                   [qradar_query_param1,
                                                                    " ",
                                                                    " ",
                                                                    qradar_query_param4 or " ",
                                                                    qradar_query_param5,
                                                                    qradar_query_param6
                                                                    ])

            log.info("Running query: " + temp_query_string)

            yield StatusMessage("starting...")

            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options.get("username", None),
                                         password=self.options.get("qradarpassword", None),
                                         token=self.options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=self.options)

            result = qradar_client.ariel_graphql_search(temp_query_string,
                                                        search_query_string,
                                                        timeout=timeout)

            # Enrich sourceip data by getting additional props using a graphql call to QRadar
            if qradar_fn_type == qradar_constants.SOURCE_IP:

                offense_source = qradar_client.get_offense_source(qradar_query_param3)

                for event in result["events"]:
                    domain = list(filter(lambda x: x["sourceIp"]==event["sourceip"], offense_source["content"]))
                    event["domainid"] = domain[0]["domainId"] if len(domain)>0 else 0  # Assign sourceip domain
                    data = qradar_client.get_sourceip_data(event)
                    event["vulnerabilityCount"] = data["content"]["vulnerabilityCount"] if data["content"] else 0
                    event["macAddress"] = data["content"]["interfaces"][0]["macAddress"] if data["content"] and len(data["content"]["interfaces"])>0 and "macAddress" in data["content"]["interfaces"][0] else ""
                    event["network"] = data["content"]["interfaces"][0]["currentIpAddress"]["network"]["networkName"] if data["content"] and len(data["content"]["interfaces"])>0 and data["content"]["interfaces"][0]["currentIpAddress"] and data["content"]["interfaces"][0]["currentIpAddress"]["network"] else ""
                    event["domain"] = data["content"]["domain"]["name"] if data["content"] and  data["content"]["domain"]["name"] else "Default Domain"

            result["events"] = list(map(lambda x: self.mapEventData(x), result["events"]))

            results = {
                "qrhost": self.options["host"],
                "offenseid": qradar_query_param3,
                "events": result["events"]
            }
            yield StatusMessage("done...")
            yield FunctionResult(results)
        except Exception as e:
            log.error(str(e))
            yield FunctionError()

    def mapEventData(self, event):

        for key in event.keys():
            if key in ["eventtime", "lastpackettime", "FirstPacketTime", "sourcebytes", "sourcepackets", "destinationbytes", "destinationpackets"]:
                event[key] = int(float(event[key]))

        return event


