# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import requests
import logging
import jinja2
import time
import json
import calendar
from datetime import datetime
from threading import Thread
from os.path import join, pardir, os
from resilient_circuits import ResilientComponent, handler
from resilient_circuits.template_functions import environment
from resilient import SimpleHTTPException
from fn_microsoft_security_graph.util.helper import MicrosoftGraphHelper
import resilient_circuits.template_functions as template_functions


log = logging.getLogger(__name__)
MSG_FIELD_NAME = "microsoft_security_graph_alert_id"


class MicrosoftSecurityGraphAlertsPolling(ResilientComponent):
    """Component that polling MSG for alerts and creates an incident is one doesn't exist"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(MicrosoftSecurityGraphAlertsPolling, self).__init__(opts)
        self.options = opts.get("fn_microsoft_security_graph", {})

        if "Microsoft_security_graph_helper" not in self.options:
            self.options["Microsoft_security_graph_helper"] = MicrosoftGraphHelper(self.options.get("tenant_id"),
                                                                                   self.options.get("client_id"),
                                                                                   self.options.get("client_secret"))
        self.main()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_microsoft_security_graph", {})

    def main(self):
        options = self.options

        if int(options.get("msg_polling_interval", 0)) > 0:
            # Add ds_to_millis to global for use in filters
            ds_filter = {"ds_to_millis": ds_to_millis}
            env = environment()
            env.globals.update(ds_filter)

            # Create and start polling thread
            thread = Thread(target=self.msg_polling_thread)
            thread.daemon = True
            thread.start()
            log.info("Polling for alerts in Microsoft Security Graph is occurring.")
        else:
            log.info("Polling for alerts in Microsoft Security Graph is not occurring.")

    def msg_polling_thread(self):
        while True:
            alert_list = self._get_alerts()

            # Check for alerts in incidents
            for alert in alert_list:
                # If case is not currently an incident create one
                if len(self._find_resilient_incident_for_req(alert.get("id"))) == 0:
                    incident_payload = self.build_incident_dto(alert)
                    self.create_incident(incident_payload)

                # Amount of time (seconds) to wait to check cases again, defaults to 10 mins if not set
            time.sleep(int(self.options.get("msg_polling_interval", 600)))

    def build_incident_dto(self, alert):
        current_path = os.path.dirname(os.path.realpath(__file__))
        default_temp_file = join(current_path, pardir, "data/templates/msg_incident_mapping.jinja")
        template_file = self.options.get("incident_template", default_temp_file)

        try:
            with open(template_file, 'r') as template:
                log.debug("Reading template file")
                incident_template = template.read()

                return template_functions.render(incident_template, alert)

        except jinja2.exceptions.TemplateSyntaxError:
            log.info("'incident_template' is not set correctly in config file.")

    def create_incident(self, payload):
        try:
            resilient_client = self.rest_client()

            uri = "/incidents"
            payload_dict = json.loads(payload)
            log.info("Creating incident with payload: {}".format(payload))
            log.debug("Payload: {}".format(payload_dict))

            response = resilient_client.post(uri=uri, payload=payload_dict)
            return response

        except SimpleHTTPException:
            log.info("Something went wrong when attempting to create the Incident")

    def _get_alerts(self):
        options = self.options
        ms_graph_helper = options.get("Microsoft_security_graph_helper")
        r = None
        for i in list(range(2)):
            headers = {
                "Content-type": "application/json",
                "Authorization": "Bearer " + ms_graph_helper.get_access_token()
            }
            start_filter = ""
            if options.get("alert_filter"):
                start_filter = "?$filter="
            r = requests.get("{}security/alerts/{}{}".format(options.get("microsoft_graph_url"), start_filter,
                                                             options.get("alert_filter")), headers=headers)
            # Check if need to refresh token and run again
            if ms_graph_helper.check_status_code(r):
                break
            elif i == 1:
                raise ValueError("Problem with the access_token")

        response_json = r.json()
        return response_json.get("value")

    # Returns back list of incidents if there is one with the same case ID, else returns empty list
    def _find_resilient_incident_for_req(self, field_value):
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
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
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = "/incidents/query?return_level=normal&field_handle={}".format(MSG_FIELD_NAME)
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
            r_incidents_tmp = self.rest_client().post(query_uri, query)
            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           if r_inc["properties"].get(MSG_FIELD_NAME) == field_value]

        return r_incidents


# Converts string datetime to milliseconds epoch
def ds_to_millis(val):
    """Assuming val is a string datetime, e.g. '2017-05-17T17:07:59.114Z' (UTC), convert to milliseconds epoch"""
    if not val:
        return val
    try:
        ts = val[:23]
        ts_format = "%Y-%m-%dT%H:%M:%S.%f"
        dt = datetime.strptime(ts, ts_format)
        return calendar.timegm(dt.utctimetuple()) * 1000
    except Exception as e:
        log.exception("%s Not in expected timestamp format YYYY-MM-DDTHH:MM:SS.mmmZ", val)
        return None
