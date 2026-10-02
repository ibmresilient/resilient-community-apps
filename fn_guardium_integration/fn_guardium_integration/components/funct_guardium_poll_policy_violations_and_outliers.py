# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, FunctionError
from circuits import Timer, Event, handler
from fn_guardium_integration.util.static_data import DEFAULT_INTERVAL, AUTOMATIC_INCIDENT_CREATION
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.util.poll_policy_violations_outliers import get_policy_violations_outliers

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'guardium_poll_policy_violations_and_outliers"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_integration", {})
        if AUTOMATIC_INCIDENT_CREATION:
            self.opts_data = opts
            self.running_status = False  # Not to run again if already running
            p_interval = self.options.get('poll_interval')
            poll_interval = int(p_interval) if p_interval else DEFAULT_INTERVAL

            self.resilient_rest_object = ResilientRestService(opts, self.options, log)
            self.grd_rest_object = GrdRestEndpoint(self.options, self.resilient_rest_object.client_secret,
                                                   self.resilient_rest_object.unique_id, log)
            self.last_proc_violation_data = []  # to store last processed violation data
            self.last_proc_outliers_data = []  # to store last processed outliers data

            try:
                get_policy_violations_outliers(self)
            except Exception as er_msg:
                log.error(str(er_msg))

            Timer(interval=poll_interval, event=Event.create("guardium_poll_policy_violations_and_outliers"),
                  persist=True).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @handler("guardium_poll_policy_violations_and_outliers")
    def _guardium_poll_policy_violations_and_outliers_function(self):
        """Function: A function to Poll the guardium on specific interval for infinite time for policy
        violations and policy outliers."""
        try:
            if not self.running_status:
                get_policy_violations_outliers(self)
            else:
                log.info(u"---------------------------Function is already running-------------------------------------")
                log.info(u" Removing all cached data, and re-setting the process monitoring flag.")
                self.last_proc_violation_data = []
                self.last_proc_outliers_data = []
                self.running_status = False
        except Exception as er_msg:
            yield FunctionError(str(er_msg))
