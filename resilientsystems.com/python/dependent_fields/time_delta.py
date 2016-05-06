#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action Module circuits component to add combine two fields to third field"""

from __future__ import print_function
import logging
from circuits import Component, Debugger
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'timedelta1'


class TimeDeltaComponent(ResilientComponent):
    """Add two fields to get a third field"""

    # This component is supposed to add two fields into a third field

    def __init__(self, opts):
        super(TimeDeltaComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'timedelta'
        self.channel = "actions." + self.options.get("queue", "timedelta1")

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

        # Get the incident and incident ID from the message
        incident = event.message["incident"]
        inc_id = incident["id"]
        # Get the source field names from the config file
        source_fieldname = self.options["source_field"]
        source_fieldname2 = self.options["source_field2"]
        dest_fieldname = self.options["dest_field"]
        # Get the value of the source fields
        source_value = incident["properties"].get(source_fieldname, "")
        source_value2 = incident["properties"].get(source_fieldname2, "")
        # Cast the values as ints and add them together
        value = int(source_value) + int(source_value2)

        LOG.info("READ %s:%s, %s:%s,   STORED %s:%s",
                 source_fieldname, source_value, source_fieldname2,
                 source_value2, dest_fieldname, value)

        def update_field(incident, fieldname, value):
            """Updates the field value, given an incident and field name"""
            incident["properties"][fieldname] = value

        # Store value in specified incident field
        self.rest_client().get_put("/incidents/{0}".format(inc_id),
                                   lambda incident: update_field(incident, dest_fieldname, value))

        yield "field %s updated" % dest_fieldname
    # end _lookup_action
