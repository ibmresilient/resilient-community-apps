#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resilient Systems, Inc. ("Resilient") is willing to license software
# or access to software to the company or entity that will be using or
# accessing the software and documentation and that you represent as
# an employee or authorized agent ("you" or "your") only on the condition
# that you accept all of the terms of this license agreement.
#
# The software and documentation within Resilient's Development Kit are
# copyrighted by and contain confidential information of Resilient. By
# accessing and/or using this software and documentation, you agree that
# while you may make derivative works of them, you:
#
# 1)  will not use the software and documentation or any derivative
#     works for anything but your internal business purposes in
#     conjunction your licensed used of Resilient's software, nor
# 2)  provide or disclose the software and documentation or any
#     derivative works to any third party.
#
# THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

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
        # or default to 'timedelta1'
        self.channel = "actions." + self.options.get("queue", "timedelta1")

    # Handle a custom action named "Time Delta"
    @handler("time_delta")
    def _time_delta(self, event, *args, **kwargs):
        """Adds two fields together and puts them in a third field"""

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
