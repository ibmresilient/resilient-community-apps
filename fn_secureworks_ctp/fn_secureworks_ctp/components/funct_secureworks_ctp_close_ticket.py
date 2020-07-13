#-*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, IntegrationError, clean_html
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
        required_fields = ["base_url", "username", "password", "query_limit", "query_ticket_grouping_types",
                           "assigned_to_customer", "polling_interval"]
        validate_fields(required_fields, self.options)

        # Create Secureworks client
        self.scwx_client = SCWXClient(self.opts, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("secureworks_ctp_close_ticket")
    def _secureworks_ctp_close_ticket_function(self, event, *args, **kwargs):
        """Function: Close a Secureworks CTP in an incident that has a Secureworks CTP ticket associated with it."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            yield StatusMessage(u"Starting Close Secureworks CTP ticket.")

            # Get the incident
            uri = u"/incidents/{}?handle_format=names".format(incident_id)
            incident = self.rest_client().get(uri)

            if not incident:
                IntegrationError("Secureworks CTP close ticket: Incident {0} not found".format(incident_id))

            # Make sure there is an SecureWorks CTP ticket associated with this incident
            ticket_id = incident.get('properties', {}).get('scwx_ctp_ticket_id', None)

            if not ticket_id:
                raise IntegrationError("Secureworks CTP close ticket: Incident {0} does not contain a ticketId".format(incident_id))

            resolution_summary = clean_html(incident.get('resolution_summary'))
            close_code = incident.get('properties', {}).get('scwx_ctp_close_code', None)

            response = self.scwx_client.post_tickets_close(ticket_id, resolution_summary, close_code)

            success = bool(response.get('code') == 'SUCCESS')

            results = rp.done(success, response)

            yield StatusMessage(u"Returning results for Close Secureworks CTP ticketId: {0} incident ID: {1}".format(ticket_id, incident_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError()
