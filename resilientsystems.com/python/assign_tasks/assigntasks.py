#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        # or default to 'filelookup'
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
