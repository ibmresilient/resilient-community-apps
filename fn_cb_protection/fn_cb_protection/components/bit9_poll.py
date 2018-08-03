# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import os
import logging
import datetime
import calendar
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_circuits.template_functions import render_json, environment
from pkg_resources import Requirement, resource_filename
from fn_cb_protection.util.bit9_client import CbProtectClient


BIT9_POLL_CHANNEL = "bit9_escalation"
REQUEST_ID_FIELDNAME = "cb_protect_request_id"


class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (BIT9_POLL_CHANNEL,)


class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (BIT9_POLL_CHANNEL,)


class ProcessApprovalRequest(Event):
    """A Circuits event to process an approval request"""
    channels = (BIT9_POLL_CHANNEL,)

    def __init__(self, request=None):
        super(ProcessApprovalRequest, self).__init__()
        self.request = request


def timestamp_to_millis(val):
    """Assuming val is a string datetime, e.g. '2017-05-17T17:07:59.114Z' (UTC), convert to milliseconds epoch"""
    if not val:
        return val
    try:
        if len(val) <= 20:
            raise ValueError(u"Invalid timestamp length %s" % val)
        ts = val.replace("Z", "")[:23]
        ts_format = "%Y-%m-%dT%H:%M:%S.%f"
        dt = datetime.datetime.strptime(ts, ts_format)
        return calendar.timegm(dt.utctimetuple()) * 1000
    except Exception as e:
        logging.getLogger(__name__).exception(u"%s Not in expected timestamp format YYYY-MM-DDTHH:MM:SS.mmmZ", val)
        return None


class Bit9PollComponent(ResilientComponent):
    """
    Event-driven polling for CarbonBlack Protection approval requests
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = BIT9_POLL_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(Bit9PollComponent, self).__init__(opts)
        self.log = logging.getLogger(__name__)
        self._load_options(opts)

        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({"timestamp_to_millis": timestamp_to_millis})
        env.filters.update({"timestamp_to_millis": timestamp_to_millis})

        # Set up a one-off timer for polling the first time
        self.log.info(u"CbProtect escalation initialized, polling interval %s seconds", self.escalation_interval)
        Timer(min((self.escalation_interval, 5)), Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        self.log.debug("CbProtect poll timer")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        self.log.debug("CbProtect poll completed")
        Timer(self.escalation_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.options = opts["fn_cb_protection"]

        self.bit9_client = CbProtectClient(self.options)

        # Timer interval (seconds).  Default 10 minutes.
        self.escalation_interval = int(self.options.get("escalation_interval", 600))
        if self.escalation_interval == 0:
            self.log.warn(u"CbProtect escalation interval is not configured.  Automated escalation is disabled.")
            return

        # Conditions for which incidents are escalated
        # By default this is "all unresolved approval requests"
        self.escalation_query = self.options.get("escalation_query", "resolution:0")

    def _escalate(self):
        """Query the CbProtect server for approval requests, and raise them to Resilient"""
        self.log.info(u"Getting list of open approval requests")

        # This just queries for all requests that match the escalation conditions.
        # For cases with many thousands of open requests, a more scalable approach could
        # use "paged" queries, i.e. send a "limit" and then process each page of results.

        results = self.bit9_client.query_approval_request(self.escalation_query)

        # Query results should be a list
        if not isinstance(results, list):
            self.log.warn(u"Query produced unexpected value: %s", results)
            return

        self.log.info("%d results", len(results))
        self.log.debug(results)

        if len(results) > 0:
            # Some (many!) of these approval requests will already have been escalated to Resilient.
            # For efficiency, find them and filter them out from this batch.
            # Then we're left only with "un-escalated" incidents.
            req_ids = [result["id"] for result in results]
            query_uri = "/incidents/query?return_level=normal&field_handle={}".format(REQUEST_ID_FIELDNAME)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{}'.format(REQUEST_ID_FIELDNAME),
                            'method': 'in',
                            'value': req_ids
                        },
                        {
                            'field_name': 'plan_status',
                            'method': 'equals',
                            'value': 'A'
                        }
                    ]
                }]
            }
            r_incidents = self.rest_client().post(query_uri, query)
        else:
            r_incidents = []

        escalated_ids = [r_inc["properties"].get(REQUEST_ID_FIELDNAME) for r_inc in r_incidents]

        unescalated_requests = [result for result in results if str(result["id"]) not in escalated_ids]

        # Process each approval-request in the batch
        for req in unescalated_requests:
            self.fire(ProcessApprovalRequest(request=req))

        self.log.info(u"Processed all approval requests")
        self.fire(PollCompleted())

    def _find_resilient_incident_for_req(self, req_id):
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{}'.format(REQUEST_ID_FIELDNAME),
                        'method': 'equals',
                        'value': req_id
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
        r_incidents = self.rest_client().post(query_uri, query)
        if len(r_incidents) > 0:
            return r_incidents[0]
        return None

    @handler("ProcessApprovalRequest")
    def _process_approval_request(self, event):
        # Process one approval request
        log = self.log
        request = event.request
        request_id = request["id"]

        # special "test the process by escalating a single request" mode
        test_single_request = self.options.get("test_single_request")
        if test_single_request:
            if str(request_id) not in str(test_single_request).split(","):
                log.info(u"Skipping request %s, test", request_id)
                return

        # Find the Resilient incident corresponding to this CbProtect approval request (if available)
        resilient_incident = self._find_resilient_incident_for_req(request_id)
        if resilient_incident:
            log.info(u"Skipping request %s, already escalated", request_id)
            return

        log.info(u"Processing request %s", request_id)
        try:
            # Create a new Resilient incident from this approval request
            # using a JSON (JINJA2) template file
            template_file_path = self.options.get("template_file")
            if template_file_path and not os.path.exists(template_file_path):
                log.warn(u"Template file '%s' not found.", template_file_path)
                template_file_path = None
            if not template_file_path:
                # Use the template file installed by this package
                template_file_path = resource_filename(Requirement("fn-cb-protection"),
                                                       "fn_cb_protection/data/template.jinja")
                if not os.path.exists(template_file_path):
                    raise Exception(u"Template file '{}' not found".format(template_file_path))

            log.info(u"Template file: %s", template_file_path)
            with open(template_file_path, "r") as definition:
                escalate_template = definition.read().decode('utf-8')

            # Render the template.  Be sure to set the CbProtect ID in the result!
            new_resilient_inc = render_json(escalate_template, request)
            new_resilient_inc["properties"][REQUEST_ID_FIELDNAME] = request_id

            log.debug(new_resilient_inc)
            inc = self.rest_client().post("/incidents", new_resilient_inc)
            rs_inc_id = inc["id"]
            message = u"Created incident {} for CbProtect {}".format(rs_inc_id, request_id)
            log.info(message)

        except Exception as exc:
            log.exception(exc)
            raise
