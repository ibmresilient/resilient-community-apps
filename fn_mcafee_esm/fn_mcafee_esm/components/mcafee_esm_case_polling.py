# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Polling implementation"""

import logging
import time
import json
import calendar
import jinja2
from datetime import datetime
from threading import Thread
from resilient_circuits import ResilientComponent, handler
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers
from fn_mcafee_esm.components.mcafee_esm_get_list_of_cases import case_get_case_list
from fn_mcafee_esm.components.mcafee_esm_get_case_detail import case_get_case_detail
from resilient_circuits.template_functions import environment
from resilient import SimpleHTTPException
import resilient_circuits.template_functions as template_functions


log = logging.getLogger(__name__)
ESM_CASE_FIELD_NAME = "mcafee_esm_case_id"


class ESM_CasePolling(ResilientComponent):
    """Component that implements Resilient function 'mcafee_esm_edit_case"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(ESM_CasePolling, self).__init__(opts)
        self.options = opts.get("fn_mcafee_esm", {})

        # Check config file and change trust_cert to Boolean
        self.options = check_config(self.options)
        self.main()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_esm", {})

    def main(self):
        options = self.options

        if options.get("esm_polling") == "True":
            # Add ds_to_millis to global for use in filters
            ds_filter = {"ds_to_millis": ds_to_millis}
            env = environment()
            env.globals.update(ds_filter)

            # Create and start polling thread
            thread = Thread(target=self.esm_polling_thread)
            thread.start()
            log.info("Polling for cases in ESM is occurring")
        else:
            log.info("Polling for cases in ESM is not occurring")

    def esm_polling_thread(self):
        while True:
            case_list = case_get_case_list(self.options)

            headers = get_authenticated_headers(self.options["esm_url"], self.options["esm_username"],
                                                self.options["esm_password"], self.options["trust_cert"])

            # Check cases in incidents
            for case in case_list:
                # If case is not currently an incident create one
                if len(self._find_resilient_incident_for_req(case["id"])) == 0:
                    incident_payload = self.build_incident_dto(headers, case["id"])
                    self.create_incident(incident_payload)

            # Amount of time (seconds) to wait to check cases again, defaults to 10 mins if not set
            time.sleep(int(self.options.get("esm_polling_interval", 600)))

    def build_incident_dto(self, headers, case_id):
        try:
            with open(self.options["incident_template"], 'r') as template:
                log.debug("Reading template file")

                case_details = case_get_case_detail(self.options, headers, case_id)
                log.debug("Case details in dict form: {}".format(case_details))

                incident_template = template.read()

                return template_functions.render(incident_template, case_details)

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

    # Returns back list of incidents if there is one with the same case ID, else returns empty list
    def _find_resilient_incident_for_req(self, esm_case_id):
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{}'.format(ESM_CASE_FIELD_NAME),
                        'method': 'equals',
                        'value': esm_case_id
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
            query_uri = "/incidents/query?return_level=normal&field_handle={}".format(ESM_CASE_FIELD_NAME)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{}'.format(ESM_CASE_FIELD_NAME),
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
                           if r_inc["properties"].get(ESM_CASE_FIELD_NAME) == esm_case_id]

        return r_incidents


# Converts string datetime to milliseconds epoch
def ds_to_millis(val):
    """Assuming val is a string datetime, e.g. '05/17/2017 17:07:59' (GMT), convert to milliseconds epoch"""
    if not val:
        return val
    try:
        if len(val) != 19:
            raise ValueError("Invalid timestamp length %s" % val)
        ts_format = "%m/%d/%Y %H:%M:%S"
        dt = datetime.strptime(val, ts_format)
        return calendar.timegm(dt.utctimetuple()) * 1000
    except Exception as e:
        log.exception("%s Not in expected timestamp format MM/DD/YYY HH:MM:SS", val)
        return None
