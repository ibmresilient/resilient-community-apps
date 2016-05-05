#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action Module circuits component to add different users depending on severity"""

from __future__ import print_function
from circuits import Component, Debugger
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
import os
import csv
import logging
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'addgroup1'

class AddGroupComponent(ResilientComponent):
    """Adds different users and groups depending on an incident's severity"""

    # This component adds different users and groups depending on an incident's severity

    def __init__(self, opts):
        super(AddGroupComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file, or default to 'filelookup'
        self.channel = "actions." + self.options.get("queue", "addgroup")


    @handler()
    def _time_delta(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Actions module.
        """

        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # get information about the incident, such as its ID and severity
        incident = event.message["incident"]
        inc_id = incident["id"]
        incident_severity = incident["severity_code"]
        
        # if High severity, make the owner User 1. 
        if (incident_severity==52):
                incident["owner_id"] = 1
        # else if Medium severity, make the owner the User 5
        elif (incident_severity==51):
                incident['owner_id'] = 5
        # else if low security, make the owner User 6
        elif (incident_severity==50):
                incident['owner_id'] = 6

        # save progress 
        self.rest_client().put("/incidents/"+str(inc_id), incident)
        incident = self.rest_client().get("/incidents/"+str(inc_id))

        # if High severity, remove all members.                       
        if (incident_severity==52):
                incident["members"] = []
        # else if Medium severity, add User 6 as a member. 
        elif (incident_severity==51):
                incident['members'] = [6]
        # else if low security, add User 4 as a member.                          
        elif (incident_severity==50):
                incident['members'] = [4]
	
	# upload to resilient. 
	self.rest_client().put("/incidents/"+str(inc_id), incident)
        
	# Log output
	LOG.info("Finished adding users to incident %s due to severity change", inc_id)

        yield "User updated!"
    #end _lookup_action
