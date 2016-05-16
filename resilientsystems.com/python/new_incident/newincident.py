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
                        'discovered_date': incident['discovered_date']} 
        LOG.info("Posting new incident to alternate org...")
        resilient_client.post('/incidents', new_incident)

        # How to post things to the original org:
        # self.rest_client().put("/incidents/"+str(inc_id), incident)

        # Log output
        LOG.info("Finished incident posting! :D")

        yield "User updated!"
        # end _lookup_action
