# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from time import sleep
from json import loads
from calendar import timegm
from threading import Thread
from datetime import datetime
from logging import getLogger
from resilient import SimpleHTTPException
from jinja2.exceptions import TemplateSyntaxError
from os.path import join, pardir, dirname, realpath
from resilient_circuits.template_functions import environment
from resilient_circuits import ResilientComponent, FunctionError
import resilient_circuits.template_functions as template_functions
from fn_microsoft_security_graph.lib.ms_graph_helper import connect_MSGraph

LOG = getLogger(__name__)
MSG_FIELD_NAME = "microsoft_security_graph_alert_id"

class PollerComponent(ResilientComponent):
    """
    Poller to o query alerts from the Microsoft Security Graph API and create incidents in the
    SOAR platform if they do not already exist
    """

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.options = opts.get("fn_microsoft_security_graph", {})
        # Connect to micosoft security graph
        self.ms_graph_helper = connect_MSGraph(opts)

        if int(self.options.get("msg_polling_interval", 0)):
            # Add ds_to_millis to global for use in Jinja templates
            environment().globals.update({"ds_to_millis": ds_to_millis})

            # Create and start polling thread
            thread = Thread(target=self.msg_polling_thread)
            thread.daemon = True
            thread.start()
            LOG.info("Polling for alerts in Microsoft Security Graph is occurring.")
        else:
            LOG.info("Polling for alerts in Microsoft Security Graph is not occurring.")

    def msg_polling_thread(self):
        while True:
            LOG.debug("Polling for alerts")
            alert_list = get_alerts(self.options, self.ms_graph_helper)
            # Amount of time (seconds) to wait to check alerts again, defaults to 10 mins if not set
            wait_time = int(self.options.get("msg_polling_interval"))

            # Check for alerts in incidents
            for alert in alert_list:
                # If alert is not currently an incident create one
                if len(self._find_resilient_incident_for_req(alert.get("id"))) == 0:
                    incident_payload = build_incident_dto(alert, self.options.get("incident_template"))
                    self.create_incident(incident_payload)

            # Wait to check alerts again
            sleep(wait_time)

    def create_incident(self, payload):
        # Creates an incident in SOAR
        try:
            payload_dict = loads(payload)
            LOG.info("Creating incident with payload: {}".format(payload))
            LOG.debug("Payload: {}".format(payload_dict))

            return self.rest_client().post(uri="/incidents", payload=payload_dict)

        except SimpleHTTPException as err:
            LOG.info("Something went wrong when attempting to create the Incident %s", err)

    # Returns back list of incidents if there is one with the same case ID, else returns empty list
    def _find_resilient_incident_for_req(self, field_value):
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{}'.format(MSG_FIELD_NAME),
                        'method': 'equals',
                        'value': field_value
                    },
                    {
                        'field_name': 'plan_status',
                        'method': 'equals',
                        'value': 'A'
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }
        try:
            return self.rest_client().post("/incidents/query?return_level=partial", query)
        except SimpleHTTPException:
            # Some versions of SOAR 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{}'.format(MSG_FIELD_NAME),
                            'method': 'has_a_value'
                        },
                        {
                            'field_name': 'plan_status',
                            'method': 'equals',
                            'value': 'A'
                        }
                    ]
                }]
            }
            r_incidents_tmp = self.rest_client().post(
                "/incidents/query?return_level=normal&field_handle={}".format(MSG_FIELD_NAME),
                query)
            return [r_inc for r_inc in r_incidents_tmp
                           if r_inc["properties"].get(MSG_FIELD_NAME) == field_value]

# Converts string datetime to milliseconds epoch
def ds_to_millis(val):
    """Assuming val is a string datetime, e.g. '2017-05-17T17:07:59.114Z' (UTC), convert to milliseconds epoch"""
    if not val:
        return val
    try:
        dt = datetime.strptime(val[:23].replace('Z',''), "%Y-%m-%dT%H:%M:%S.%f")
        return timegm(dt.utctimetuple()) * 1000
    except Exception as e:
        LOG.exception("%s Not in expected timestamp format YYYY-MM-DDTHH:MM:SS.mmmZ", val)

def get_alerts(options, ms_graph_helper):
    # Set createDateTime start filter
    alert_time_range_sec = options.get("alert_time_range_sec")
    createdDateTime_filter = ""
    if alert_time_range_sec:
        createdDateTime_start = datetime.utcnow().isoformat() + 'Z'
        createdDateTime_filter = "createdDateTime%20ge%20{}".format(createdDateTime_start)

    url = "{}/security/alerts{}".format(options.get("microsoft_graph_url"), create_query(options.get("alert_query"),
                                                                                         createdDateTime_filter))

    response = ms_graph_helper.ms_graph_session.get(url)
    if not response:
        raise FunctionError("Request failed, please check the LOG.")

    response_json = response.json()
    return response_json.get("value")

def build_incident_dto(alert, template_file=None):
    if not template_file:
        template_file = join(dirname(realpath(__file__)), pardir, "data/templates/msg_incident_mapping.jinja")

    try:
        with open(template_file, 'r') as template:
            LOG.debug("Reading template file")
            return template_functions.render(template.read(), alert)

    except TemplateSyntaxError:
        LOG.info("'incident_template' is not set correctly in config file.")

def create_query(alert_query, createDateTime_filter):
    query = ""

    # Add custom query if set
    if alert_query:
        query = "?${}".format(alert_query)

    # Add date filter if set
    if len(createDateTime_filter) > 0:
        # Query is currently empty
        if query == "":
            query = "?$filter={}".format(createDateTime_filter)
        # Query already has a filter section in it and the date filter should just be added to the end of that section
        elif "$filter=" in query:
            query_sections = query.split('&$')
            for i in range(len(query_sections)):
                if "filter" in query_sections[i]:
                    query_sections[i] = "{}%20and%20{}".format(query_sections[i], createDateTime_filter)
                    break
            query = '&$'.join(query_sections)

        # Query has other sections but not a filter section, add filter to the end
        else:
            query = "&$filter={}".format(createDateTime_filter)

    LOG.debug("Query: []".format(query))
    return query
