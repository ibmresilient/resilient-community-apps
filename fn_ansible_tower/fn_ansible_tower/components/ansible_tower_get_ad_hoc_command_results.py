# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
from fn_ansible_tower.lib.common import SECTION_HDR, TOWER_API_BASE, get_common_request_items, save_as_attachment, clean_url

JOBS_URL = "ad_hoc_commands/{id}/"
EVENTS_URL = "ad_hoc_commands/{id}/events/"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ansible_tower_get_job_results"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(SECTION_HDR, {})

    @function("ansible_tower_get_ad_hoc_command_results")
    def _ansible_tower_get_job_results_function(self, event, *args, **kwargs):
        """Function: Get the results of a complete job"""
        try:
            validate_fields(("url"), self.options) # validate key app.config settings

            # Get the function parameters:
            tower_job_id = kwargs.get("tower_job_id")  # text
            tower_save_as = self.get_select_param(kwargs.get("tower_save_as")) # select
            incident_id = kwargs.get("incident_id") # number

            log = logging.getLogger(__name__)
            log.info("tower_job_id: %s", tower_job_id)
            log.info("tower_save_as: %s", tower_save_as)
            log.info("incident_id: %s", incident_id)

            result = ResultPayload(SECTION_HDR, **kwargs)
            rc = RequestsCommon(self.opts, self.options)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # common
            basic_auth, cafile = get_common_request_items(self.options)

            # get summary information
            summary_url = "/".join((clean_url(self.options['url']), TOWER_API_BASE, JOBS_URL.format(id=tower_job_id)))
            summary_result = rc.execute_call_v2("get", summary_url, proxies=rc.get_proxies(), auth=basic_auth,
                                                verify=cafile)
            json_summary = summary_result.json()

            event_url = "/".join((clean_url(self.options['url']), TOWER_API_BASE, EVENTS_URL.format(id=tower_job_id)))


            events_result = rc.execute_call_v2("get", event_url, proxies=rc.get_proxies(), auth=basic_auth,
                                               verify=cafile)

            json_events = events_result.json()

            payload = {
                "summary": json_summary,
                "events": json_events
            }

            # save results as attachment will return no results.content
            if tower_save_as == "attachment":
                res_client = self.rest_client()
                save_as_attachment(res_client, incident_id, payload)

            result_payload = result.done(True, payload)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()
