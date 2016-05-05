#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action Module circuits component to add different users depending on severity"""

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage

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

        # Severity code is an id (SELECT field) so we need to find the text label
        # There's a helper function in ResilientComponent for this purpose.
        incident_severity = incident["severity_code"]
        incident_severity_label = self.get_field_label("severity_code", incident_severity)
        LOG.info(incident_severity_label)

        def update_owner(inc):
            # if High severity, make the owner User 1.
            if (incident_severity_label == "High"):
                inc["owner_id"] = self.options.get("high_owner")
            # else if Medium severity, make the owner the User 5
            elif (incident_severity_label == "Medium"):
                inc['owner_id'] = "Someone"
            # else if low security, make the owner User 6
            elif (incident_severity_label == "Low"):
                inc['owner_id'] = "A Group"
            return inc

        # Update the incident owner
        self.rest_client().get_put("/incidents/"+str(inc_id), update_owner)

        def update_members(inc):
            # if High severity, remove all members.
            if (incident_severity_label == "High"):
                incident["members"] = []
            # else if Medium severity, add User 6 as a member.
            elif (incident_severity_label == "Medium"):
                incident['members'] = [6]
            # else if low security, add User 4 as a member.
            elif (incident_severity_label == "Low"):
                incident['members'] = [4]

        # Update the incident members
        self.rest_client().get_put("/incidents/" + str(inc_id), update_members)

        status = "Finished adding users to incident {0} due to severity change".format(inc_id)
        yield status
