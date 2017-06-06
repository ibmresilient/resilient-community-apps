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

        # Get all the tasks, into an array, and set the owner of each
        tasks_to_update = []
        for task_id in task_ids:
            task_url = "/tasks/{}".format(task_id)
            task = self.rest_client().get(task_url)
            if task["status"] == "O" and task["owner_id"] is None:
                LOG.info("Setting ownership for task {}".format(task["id"]))
                task["owner_id"] = user_id
                tasks_to_update.append(task)

        # Update them all at once
        if tasks_to_update:
            self.rest_client().put("/tasks", tasks_to_update, co3_context_token=event.context)

        LOG.info("Done")
