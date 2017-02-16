# -*- coding: utf-8 -*-

"""Action Module circuits component to add an incident manually"""

import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent
import co3 as resilient
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'addincident'


class AddIncidentComponent(ResilientComponent):
    """Adds an incident once a menu item is clicked"""

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

        # set verify option
        verify = self.options['verify']
        if self.options['verify'] == "False":
            verify = False
        elif self.options['verify'] == "True":
            verify = True

        LOG.info("Connecting to alternate org...")
        resilient_client = resilient.SimpleClient(self.options['to_org_name'],
                                                  self.options['to_org_address'],
                                                  verify=verify)
        LOG.info("Authenticating with alternate org...")
        resilient_client.connect(self.options['to_org_username'],
                                 self.options['to_org_password'])
        LOG.info("Creating new incident...")
        new_incident = {'name': 'New Incident Copied From Other Org',
                        'description': 'Incident created from incident '+str(inc_id),
                        'discovered_date': incident['discovered_date']} 
        LOG.info("Posting new incident to alternate org...")
        resilient_client.post('/incidents', new_incident)

        # How to post things to the original org:
        # self.rest_client().put("/incidents/"+str(inc_id), incident)

        # Log output
        LOG.info("Finished incident posting! :D")

        yield "Incident Created"
    # end _add_incident
