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

"""Action Module circuits component to programmatically assign users to tasks"""

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'assigntasks'


class AssignTasksComponent(ResilientComponent):
    """Assigns users to each task in an incident"""

    def __init__(self, opts):
        super(AssignTasksComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'assigntasks'
        self.channel = "actions." + self.options.get("queue", "assigntasks")

    @handler("assign_tasks")
    def _assign_tasks(self, event, *args, **kwargs):
        """Function to assign tasks in an incident"""
        # get information about the incident, such as its ID
        incident = event.message["incident"]
        inc_id = incident["id"]
        LOG.info("Got incident info!")
        # get the tasks and groups from resilient
        mytasks = self.rest_client().get('/incidents/'+str(inc_id)+'/tasktree')
        mygroups = self.rest_client().get('/groups')
        LOG.info("Got incident "+str(inc_id)+" tasktree and groups!")
        # make a list of all the members and owner of an incident
        idlist = [incident['owner_id']]+incident['members']
        # if the id belongs to a group, remove the group and replace it with
        # its constituent members
        for group in mygroups:
            if group['id'] in idlist:
                idlist.remove(group['id'])
                idlist += group['members']
        LOG.info("Made user ID list!")

        # assign the tasks to random users in the group list
        # store the modified tasks in a list
        newtasklist = []
        for phase in mytasks:
            for task in phase['child_tasks']:
                task['owner_id'] = idlist[random.randrange(len(idlist))]
                newtasklist.append(task)
                LOG.info(task['owner_id'])
        LOG.info("Made new tasks list!")

        # put the tasks back in resilient
        LOG.info("Putting the tasks back in resilient...")
        self.rest_client().put('/tasks', newtasklist)

        LOG.info("Finished assigning tasks! :D")

        # How to post things to the original org:
        # self.rest_client().put("/incidents/"+str(inc_id), incident)

        yield "User updated!"
        # end _assign_tasks
