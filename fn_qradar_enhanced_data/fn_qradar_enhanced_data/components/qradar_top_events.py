# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from time import time
import logging
from re import sub, search, IGNORECASE
from fn_qradar_enhanced_data.util.qradar_constants import ARIEL_SEARCH_EVENTS, ARIEL_SEARCH_FLOWS, SOURCE_IP, GLOBAL_SETTINGS
from fn_qradar_enhanced_data.util.function_utils import make_query_string, get_servers_list
from fn_qradar_enhanced_data.util.qradar_utils import QRadarClient, QRadarServers
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_top_events"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = get_servers_list(opts)
        self.global_settings = opts.get(GLOBAL_SETTINGS, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = get_servers_list(opts)
        self.global_settings = opts.get(GLOBAL_SETTINGS, {})

    @function("qradar_top_events")
    def _qradar_top_events(self, event, *args, **kwargs):
        """Function: QRadar Top Events"""

        try:
            required_fields = ["qradar_query_type", "qradar_query"]
            validate_fields(required_fields, kwargs)
            # Get the function parameters:
            qradar_query = self.get_textarea_param(kwargs.get("qradar_query"))  # textarea
            qradar_fn_type = kwargs.get("qradar_query_type")  # text
            qradar_search_param1 = kwargs.get("qradar_search_param1")  # text
            qradar_search_param2 = kwargs.get("qradar_search_param2")  # text
            qradar_search_param3 = kwargs.get("qradar_search_param3")  # text
            qradar_search_param4 = kwargs.get("qradar_search_param4")  # text
            qradar_search_param5 = kwargs.get("qradar_search_param5")  # text
            qradar_search_param6 = kwargs.get("qradar_search_param6")  # text
            qradar_label = kwargs.get("qradar_label") # QRadar server to connect to

            log.info("qradar_query: %s", qradar_query)
            log.info("qradar_search_param1: %s", qradar_search_param1)
            log.info("qradar_search_param2: %s", qradar_search_param2)
            log.info("qradar_search_param3: %s", qradar_search_param3)
            log.info("qradar_search_param4: %s", qradar_search_param4)
            log.info("qradar_search_param5: %s", qradar_search_param5)
            log.info("qradar_search_param6: %s", qradar_search_param6)
            log.info("qradar_label: %s", qradar_label)

            options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
            qradar_verify_cert = False if options.get("verify_cert", "false").lower() == "false" else options.get("verify_cert")

            timeout = float(self.global_settings.get("search_timeout",600))  # Default timeout to 10 minutes

            log.debug("Connection to {} using {}".format(options.get("host"),
                                                         options.get("username", None) or options.get(
                                                             "qradartoken", None)))

            temp_table = "offense-{0}-events-{1}-1000-{2}".format(qradar_search_param3, qradar_fn_type,
                                                                  str(time()))

            qradar_temp_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                       "FROM {} INTO \"{}\"".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS, temp_table),
                                       qradar_query, flags=IGNORECASE)

            qradar_search_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                         "FROM \"{}\"".format(temp_table),
                                         qradar_query, flags=IGNORECASE)

            temp_query_string = make_query_string(qradar_temp_query,
                                                                 ["*",
                                                                  qradar_search_param2,
                                                                  qradar_search_param3,
                                                                  " ",
                                                                  " ",
                                                                  " "])

            search_query_string = make_query_string(qradar_search_query,
                                                                   [qradar_search_param1,
                                                                    " ",
                                                                    " ",
                                                                    qradar_search_param4 or " ",
                                                                    qradar_search_param5,
                                                                    qradar_search_param6
                                                                    ])

            log.info("Running query: " + temp_query_string)

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'qradar_top_events' that was running in workflow '{0}'".format(wf_instance_id))

            qradar_client = QRadarClient(host=options.get("host"),
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            result = qradar_client.ariel_graphql_search(temp_query_string,
                                                        search_query_string,
                                                        timeout=timeout)

            # Enrich sourceip data by getting additional props using a graphql call to QRadar
            if qradar_fn_type == SOURCE_IP:

                offense_source = qradar_client.get_offense_source(qradar_search_param3)

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
                "qrhost": options.get("host"),
                "offenseid": qradar_search_param3,
                "events": result["events"]
            }
            yield StatusMessage("Finished 'qradar_top_events' that was running in workflow '{0}'".format(wf_instance_id))
            yield FunctionResult(results)
        except Exception as e:
            log.error(str(e))
            yield FunctionError()

    def mapEventData(self, event):

        for key in event.keys():
            if key in ["eventtime", "lastpackettime", "FirstPacketTime", "sourcebytes", "sourcepackets", "destinationbytes", "destinationpackets"]:
                event[key] = int(float(event[key]))

        return event
