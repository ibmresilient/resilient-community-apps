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

"""Action Module circuits component """

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'assigntasks'


class AssignTasksToMeComponent(ResilientComponent):
    """Assigns users to each task in an incident"""

    def __init__(self, opts):
        super(AssignTasksToMeComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'assigntasks'
        self.channel = "actions." + self.options.get("queue", "assigntasks")

    def _ensure_user_is_member(self, incident, user_id, co3_context_token=None):
        # First ensure that this user is a member or owner of the incident,
        # either directly, or indirectly via groups.
        # (otherwise it is not possible to assign them a task).
        # If not a member, add them.
        #
        # Direct tests are easy
        if user_id == incident["owner_id"]:
            return
        if user_id in incident["members"]:
            return
        #
        # Get the user's info
        client = self.rest_client()
        user_def = client.get("/users/{}".format(user_id))
        # User info includes a list of the groups that the user belongs to
        user_groups = user_def["group_ids"]
        # Now we can check the incident member list
        if len(set(incident["members"]).intersection(set(user_groups))) > 0:
            # Yes, user is in a group that is in the incident
            return

        def update_func(incident):
            """Update the incident to add a user as member"""
            LOG.info("Adding %s as an incident member so they can own tasks", user_def["email"])
            incident["members"].append(user_id)
            return incident
        incident_url = "/incidents/{}".format(incident["id"])
        client.get_put(incident_url, update_func, co3_context_token=co3_context_token)

    def _tasks_in_current_phase(self, incident):
        """Get a list of ids of the tasks in the current incident phase"""
        phase_id = incident["phase_id"]
        tasks_url = "/incidents/{}/tasks".format(incident["id"])
        client = self.rest_client()
        tasks = client.get(tasks_url)
        tasks_in_phase = [task for task in tasks if task["phase_id"] == phase_id]
        task_ids = [task["id"] for task in tasks_in_phase]
        return task_ids

    @handler("assign_tasks_to_me")
    def _assign_tasks(self, event, *args, **kwargs):
        """Function to assign tasks in an incident"""

        # Incident that this action applies to
        incident = event.message["incident"]

        # Find information about the user who initiated the action
        responsible_user = event.message["user"]
        user_id = responsible_user["id"]

        # First ensure that this user is a member or owner of the incident,
        # (otherwise it is not possible to assign them a task).
        self._ensure_user_is_member(incident, user_id, co3_context_token=event.context)

        # Find the tasks in the current phase
        task_ids = self._tasks_in_current_phase(incident)

        def update_task(task):
            """Callback function to update a task and set its owner"""
            if task["status"] == "O" and task["owner_id"] is None:
                LOG.info("Setting ownership for task %s", task["id"])
                task["owner_id"] = user_id

        for task_id in task_ids:
            task_url = "/tasks/{}".format(task_id)
            self.rest_client().get_put(task_url, update_task, co3_context_token=event.context)

        LOG.info("Done")
