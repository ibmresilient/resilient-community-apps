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
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_circuits.template_functions import environment
from resilient import SimpleHTTPException
from fn_microsoft_security_graph.util.helper import MicrosoftGraphHelper
import resilient_circuits.template_functions as template_functions


log = logging.getLogger(__name__)
MSG_FIELD_NAME = "microsoft_security_graph_alert_id"


class IntegrationComponent(ResilientComponent):
    """Component that polling MSG for alerts and creates an incident is one doesn't exist"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(IntegrationComponent, self).__init__(opts)
        self.options = opts.get("fn_microsoft_security_graph", {})

        self.Microsoft_security_graph_helper = MicrosoftGraphHelper(self.options.get("tenant_id"),
                                                                    self.options.get("client_id"),
                                                                    self.options.get("client_secret"))
        self.polling_main()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_microsoft_security_graph", {})

    @function("microsoft_security_graph_alert_search")
    def _microsoft_security_graph_alert_search_function(self, event, *args, **kwargs):
        """Function: Get the details of an alert from the Microsoft Security Graph API."""
        options = self.options
        ms_graph_helper = self.Microsoft_security_graph_helper
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            # Get the function parameters:
            microsoft_security_graph_alert_search_filter = kwargs.get(
                "microsoft_security_graph_alert_search_filter")  # text

            if microsoft_security_graph_alert_search_filter is not None:
                log.info("microsoft_security_graph_alert_search_filter: %s",
                         microsoft_security_graph_alert_search_filter)

            r = alert_search(options.get("microsoft_graph_url"), ms_graph_helper,
                             microsoft_security_graph_alert_search_filter)
            if not r:
                raise FunctionError("Problem with the access_token")

            yield StatusMessage("done...")
            end_time = time.time()
            results = {
                "Inputs": {
                    "microsoft_security_graph_alert_search_filter": microsoft_security_graph_alert_search_filter
                },
                "Run Time": str(end_time - start_time),
                "Alerts": r.json()
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)

    @function("microsoft_security_graph_get_alert_details")
    def _microsoft_security_graph_get_alert_details_function(self, event, *args, **kwargs):
        """Function: Get the details of an alert from the Microsoft Security Graph API."""
        options = self.options
        ms_graph_helper = self.Microsoft_security_graph_helper
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            # Get the function parameters:
            microsoft_security_graph_alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text

            if microsoft_security_graph_alert_id is not None:
                log.info("microsoft_security_graph_alert_id: %s", microsoft_security_graph_alert_id)
            else:
                raise FunctionError("microsoft_security_graph_alert_id is required to run this function.")

            r = get_alert_details(options.get("microsoft_graph_url"), ms_graph_helper,
                                  microsoft_security_graph_alert_id)
            if not r:
                raise FunctionError("Problem with the access_token")

            yield StatusMessage("done...")
            end_time = time.time()
            results = {
                "Inputs": {
                    "microsoft_security_graph_alert_id": microsoft_security_graph_alert_id
                },
                "Run Time": str(end_time - start_time),
                "Details": r.json()
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)

    @function("microsoft_security_graph_update_alert")
    def _microsoft_security_graph_update_alert_function(self, event, *args, **kwargs):
        """Function: Update an alert in the Microsoft Security Graph."""
        options = self.options
        ms_graph_helper = self.Microsoft_security_graph_helper
        try:
            start_time = time.time()
            yield StatusMessage("starting...")

            # Get the function parameters:
            microsoft_security_graph_alert_id = kwargs.get("microsoft_security_graph_alert_id")  # text
            microsoft_security_graph_alert_data = self.get_textarea_param(
                kwargs.get("microsoft_security_graph_alert_data"))  # textarea

            if microsoft_security_graph_alert_id is not None:
                log.info("microsoft_security_graph_alert_id: %s", microsoft_security_graph_alert_id)
            else:
                raise FunctionError("microsoft_security_graph_alert_id is required to run this function.")
            if microsoft_security_graph_alert_data is not None:
                log.info("microsoft_security_graph_alert_data: %s", microsoft_security_graph_alert_data)
            else:
                raise FunctionError("microsoft_security_graph_alert_data is required to run this function")

            r = update_alert(options.get("microsoft_graph_url"), ms_graph_helper, microsoft_security_graph_alert_id,
                             microsoft_security_graph_alert_data)
            if not r:
                raise FunctionError("Problem with the access_token")

            yield StatusMessage("done...")
            end_time = time.time()
            results = {
                "Inputs": {
                    "microsoft_security_graph_alert_id": microsoft_security_graph_alert_id,
                    "microsoft_security_graph_alert_data": microsoft_security_graph_alert_data
                },
                "Run Time": str(end_time - start_time),
                "Value": r.json()
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)

    def polling_main(self):
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
            alert_list = get_alerts(self.options, self.Microsoft_security_graph_helper)

            # Check for alerts in incidents
            for alert in alert_list:
                # If alert is not currently an incident create one
                if len(self._find_resilient_incident_for_req(alert.get("id"))) == 0:
                    incident_payload = build_incident_dto(alert, self.options.get("incident_template"))
                    self.create_incident(incident_payload)

                # Amount of time (seconds) to wait to check cases again, defaults to 10 mins if not set
            time.sleep(int(self.options.get("msg_polling_interval", 600)))

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


def get_alerts(options, ms_graph_helper):
    # Set createDateTime start filter
    alert_time_range_sec = options.get("alert_time_range_sec")
    createdDateTime_filter = ""
    if alert_time_range_sec:
        createdDateTime_start = datetime.utcnow().isoformat() + 'Z'
        createdDateTime_filter = "createdDateTime%20ge%20{}".format(createdDateTime_start)

    r = None
    for i in list(range(2)):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + ms_graph_helper.get_access_token()
        }

        r = requests.get("{}security/alerts/{}".format(options.get("microsoft_graph_url"),
                                                       create_filter(options.get("alert_filter"),
                                                                     createdDateTime_filter)), headers=headers)
        # Check if need to refresh token and run again
        if ms_graph_helper.check_status_code(r):
            break
        elif i == 1:
            raise ValueError("Problem with the access_token")

    response_json = r.json()
    return response_json.get("value")


def build_incident_dto(alert, custom_temp_file=None):
    current_path = os.path.dirname(os.path.realpath(__file__))
    default_temp_file = join(current_path, pardir, "data/templates/msg_incident_mapping.jinja")
    if custom_temp_file:
        template_file = custom_temp_file
    else:
        template_file = default_temp_file

    try:
        with open(template_file, 'r') as template:
            log.debug("Reading template file")
            incident_template = template.read()

            return template_functions.render(incident_template, alert)

    except jinja2.exceptions.TemplateSyntaxError:
        log.info("'incident_template' is not set correctly in config file.")


def alert_search(url, ms_helper, search_filter=None):
    r = None
    for i in list(range(2)):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + ms_helper.get_access_token()
        }
        start_filter = ""
        if search_filter:
            start_filter = "?$"
        r = requests.get("{}security/alerts/{}{}".format(url, start_filter,
                                                         search_filter),
                         headers=headers)
        # Check if need to refresh token and run again
        if ms_helper.check_status_code(r):
            break
        elif i == 1:
            return False
    return r


def get_alert_details(url, ms_helper, alert_id):
    r = None
    for i in list(range(2)):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + ms_helper.get_access_token()
        }
        r = requests.get("{}security/alerts/{}".format(url, alert_id), headers=headers)
        # Check if need to refresh token and run again
        if ms_helper.check_status_code(r):
            break
        elif i == 1:
            return False
    return r


def update_alert(url, ms_helper, alert_id, alert_data):
    r = None
    for i in list(range(2)):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + ms_helper.get_access_token(),
            "Prefer": "return=representation"
        }
        try:
            data = json.loads(alert_data)
        except ValueError as e:
            raise FunctionError("microsoft_security_graph_alert_data needs to be in dict format; " + e.message)

        r = requests.patch("{}/security/alerts/{}".format(url, alert_id), headers=headers,
                           json=data)
        # Check if need to refresh token and run again
        if ms_helper.check_status_code(r):
            break
        elif i == 1:
            return False
    return r


def create_filter(alert_filter, createDateTime_filter):
    query = ""

    # Add custom filter if set
    if alert_filter:
        query = "?${}".format(alert_filter)

    # Add date filter if set
    if len(createDateTime_filter) > 0:
        if "?$" in query:
            query = query + "%20and%20"
        else:
            query = "?$filter="
        query = query + createDateTime_filter

    log.debug(query)
    return query


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
