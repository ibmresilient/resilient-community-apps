#-*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_secureworks_ctp.lib.scwx_ctp_client import SCWXClient

CONFIG_DATA_SECTION = "fn_secureworks_ctp"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'secureworks_ctp_close_ticket"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        self._load_options(opts)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["base_url", "username", "password", "query_limit", "query_ticket_types",
                           "query_grouping_types", "assigned_to_customer", "polling_interval"]
        validate_fields(required_fields, self.options)

        # Create Secureworks client
        self.scwx_client = SCWXClient(self.opts, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_secureworks_ctp", {})

    @function("secureworks_ctp_close_ticket")
    def _secureworks_ctp_close_ticket_function(self, event, *args, **kwargs):
        """Function: Close a Secureworks CTP in an incident that has a Secureworks CTP ticket associated with it."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            uri = u"/incidents/{}".format(incident_id)
            incident = self.rest_client().get(uri)
            resolution_summary = incident.get('resolution_summary')
            close_code = incident['properties']['scwx_ctp_close_code']
            self.scwx_client.post_tickets_close(incident_id, resolution_summary, close_code)

            results = {
                "value": ""
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError()