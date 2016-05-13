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

"""Action Module circuits component to add an incident manually"""

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
import co3 as resilient
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'closeco3incident'


class AddIncidentComponent(ResilientComponent):
    """Adds an incident once a manual action is clicked"""

    # This component adds an incident once a manual action is clicked

    def __init__(self, opts):
        super(AddIncidentComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)
        self.resilient_client = 0

        # The queue name can be specified in the config file,
        # or default to 'filelookup'
        self.channel = "actions." + self.options.get("queue", "addincident")

    @handler()
    def _add_incident(self, event, *args, **kwargs):
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

        # get information about the incident, such as its ID
        myincident = event.message["incident"]
        inc_id = myincident["id"]

        LOG.info("Connecting to alternate org...")
        self.resilient_client = resilient.SimpleClient(self.options['to_org_name'],
                                                       self.options['to_org_address'],
                                                       verify=False)
        LOG.info("Authenticating with alternate org...")
        self.resilient_client.connect(self.options['to_org_username'],
                                      self.options['to_org_password'])
        LOG.info("Getting incidents...")
        incidents = self.resilient_client.get('/incidents')
        LOG.info("Closing incidents...")

        def close_incident(inc):
            """function to close incidents"""
            inc['plan_status'] = 'C'
            return incident

        # Closes out incidents
        for incident in incidents:
            if str(incident['resilient_org_id']) == str(inc_id):
                self.resilient_client.get_put('/incidents/'+str(incident['id']), close_incident)
                LOG.info('Closed incident '+str(incident['id']))
        LOG.info("Finished closing incidents! :D")

        # How to post things to the original org:
        # self.rest_client().put("/incidents/"+str(inc_id), incident)

        # Log output
        LOG.info("Finished incident posting! :D")

        yield "User updated!"
        # end _lookup_action
