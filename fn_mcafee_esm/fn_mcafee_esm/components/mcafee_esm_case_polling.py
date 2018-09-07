# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Polling implementation"""

import logging
import time
import json
import calendar
from datetime import datetime
from threading import Thread
from resilient_circuits import ResilientComponent, handler
from fn_mcafee_esm.util.helper import check_config, get_authenticated_headers
from fn_mcafee_esm.components.mcafee_esm_get_list_of_cases import case_get_case_list
from fn_mcafee_esm.components.mcafee_esm_get_case_detail import case_get_case_detail
from resilient_circuits.template_functions import environment
import resilient_circuits.template_functions as template_functions


log = logging.getLogger(__name__)


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
            resilient_client = self.rest_client()
            case_list = case_get_case_list(self.options)

            open_incidents = resilient_client.get("/incidents/open")

            headers = get_authenticated_headers(self.options["esm_url"], self.options["esm_username"],
                                                self.options["esm_password"], self.options["trust_cert"])

            # Check cases in incidents
            for case in case_list:
                # If case is not currently an incident create one
                if not is_case_incident(case, open_incidents):
                    incident_payload = self.build_incident_dto(headers, case["id"])
                    self.create_incident(incident_payload)

            # Amount of time (seconds) to wait to check cases again, defaults to 5 mins if not set
            time.sleep(int(self.options.get("esm_polling_interval", 300)))

    def build_incident_dto(self, headers, case_id):
        try:
            with open(self.options["incident_template"], 'r') as template:
                log.debug("Reading template file")

                case_details = case_get_case_detail(self.options, headers, case_id)
                log.debug("Case details in dict form: {}".format(case_details))

                incident_template = template.read()

                return template_functions.render(incident_template, case_details)

        except Exception:
            raise Exception("'incident_template' is not set correctly in config file.")

    def create_incident(self, payload):
        resilient_client = self.rest_client()

        uri = "/incidents"
        payload_dict = json.loads(payload)
        log.info("Creating incident with payload: {}".format(payload))
        log.debug("Payload: {}".format(payload_dict))

        response = resilient_client.post(uri=uri, payload=payload_dict)
        return response


def is_case_incident(case, incident_list):
    exists = filter(lambda incident: str(incident["name"]).startswith(str(case["id"])), incident_list)
    if len(exists) > 0:
        return True
    else:
        return False


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
