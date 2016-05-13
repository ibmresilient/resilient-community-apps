#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action Module circuits component to add an incident manually"""

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent
import co3 as resilient
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'addincident'


class AddIncidentComponent(ResilientComponent):
    """Adds an incident once a manual action is clicked"""

    # This component adds an incident once a manual action is clicked

    def __init__(self, opts):
        super(AddIncidentComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'addincident'
        self.channel = "actions." + self.options.get("queue", "addincident")

    @handler("escalate_incident_between_orgs")
    def _add_incident(self, event, *args, **kwargs):
        """Function to add an incident to another org."""

        # get information about the incident, such as its ID
        incident = event.message["incident"]
        inc_id = incident["id"]
        LOG.info("Connecting to alternate org...")
        resilient_client = resilient.SimpleClient(self.options['to_org_name'],
                                                  self.options['to_org_address'],
                                                  verify=self.options['verify'])
        LOG.info("Authenticating with alternate org...")
        resilient_client.connect(self.options['to_org_username'],
                                 self.options['to_org_password'])
        LOG.info("Creating new incident...")
        new_incident = {'name': 'New Incident From Manual Action',
                        'description': 'Incident created from incident '+str(inc_id),
                        'discovered_date': int('1461516765'),
                        'resilient_org_id': str(inc_id)}
        LOG.info("Posting new incident to alternate org...")
        resilient_client.post('/incidents', new_incident)

        # How to post things to the original org:
        # self.rest_client().put("/incidents/"+str(inc_id), incident)

        # Log output
        LOG.info("Finished incident posting! :D")

        yield "User updated!"
        # end _lookup_action
