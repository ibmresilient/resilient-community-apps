# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging

from circuits import Timer, Event, handler as circuit_handler
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, str_to_bool

from fn_guardium_insights_integration.util.business_methods import retrieve_anomalies_create_incident


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'Poll Analytic Events"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_insights_integration", {})
        self.log = logging.getLogger(__name__)
        # Validating app.config params
        validate_fields(["insights_host", "rest_service_port", "insights_encoded_token", "analytics_poll_time"],
                        self.options)
        if str_to_bool(self.options.get("enable_firewall_auth")) is True:
            validate_fields(["bso_ip", "bso_user", "bso_password"], self.options)

        # Retrieve app config params
        poll_sec = int(self.options.get("analytics_poll_time"))

        # Generate an event
        Timer(interval=poll_sec, event=Event.create("poll_guardium_insights_analytics_events"), persist=True).register(
            self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_insights_integration", {})

    @circuit_handler("poll_guardium_insights_analytics_events")
    def _poll_guardium_insights_analytic_events(self):
        rest_client = self.rest_client()
        retrieve_anomalies_create_incident(rest_client, self.options, self.log)
