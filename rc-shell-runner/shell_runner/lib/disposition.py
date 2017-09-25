#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action dispositions"""

from __future__ import print_function
import os
import resilient
import json
import tempfile
import collections
import logging
LOG = logging.getLogger(__name__)


# Make a disposition
# Call when ready, passing the event (which has all the incident, etc)
# and the result (which should be suitable for executing your disposition).
#

def update_with_result(message, result):
    """Update the dict 'message', applying the values in 'result'
        recursively (unlike dict.update() which is shallow).

        >>> update_with_result({"a": 1, "b": "B"}, {"b": 2})
        {'a': 1, 'b': 2}

        >>> update_with_result({"properties": {"a": 1}}, {"properties": {"b": 2}})
        {'properties': {'a': 1, 'b': 2}}

        >>> update_with_result({'values': None}, {'properties': {'b': 2}})
        {'values': None, 'properties': {'b': 2}}

        >>> update_with_result({"properties": "string"}, {"properties": {"b": 2}})
        {'properties': {'b': 2}}

    """
    # LOG.info("Message: %s", message)
    # LOG.info("Result: %s", result)
    for k, v in result.iteritems():
        if isinstance(message, collections.Mapping):
            if isinstance(v, collections.Mapping):
                r = update_with_result(message.get(k, {}), v)
                message[k] = r
            else:
                message[k] = result[k]
        else:
            message = {k: result[k]}
    return message


class Disposition(dict):
    """A description of how to effect changes"""

    def __init__(self, resilient_client, dispmethod):
        """Initialize a dispatcher based on optional method name"""
        super(Disposition, self).__init__()
        assert dispmethod is not None
        self.client = resilient_client
        # Disposition can be "name,arg1=value1,arg2=value2,..."
        # in which case the args dict will be passed to the disposition function.
        (method, sep, all_args) = dispmethod.partition(",")
        args = {}
        if all_args != "":
            pair_args = all_args.split(",")
            for pair in pair_args:
                (key, equals, value) = pair.partition("=")
                args[key] = value
        self._args = args
        try:
            self._disposition = Disposition.__dict__[method]
        except KeyError:
            raise Exception("Disposition '{}' not found".format(method))

    def call(self, event, data):
        """Do the action associated with this disposition"""
        return self._disposition(self, self._args, event, data)

    def ignore(self, args, event, data):
        """A disposition that does nothing"""
        pass

    # Update the (incident, task, note, etc)

    def update_incident(self, args, event, data):
        """Update with data"""
        if not isinstance(data, dict):
            data = json.loads(data)
        incident_id = event.incident["id"]
        # If the data is an incident with plan_status="C", it's (being) closed.
        # In this case we update in two steps:
        # 1- Strip the plan_status field from the data, and update.
        # 2- Apply the pln_status field to close the incident.
        # If status was "C" (closed) already, that's OK, because get_put is lazy
        # and the second time (closing the incident) will do nothing.
        # If status is changing from C to A (reopening), it's ok in one step.
        status = data.get("plan_status", None)
        if status in ["C", "Closed"]:
            # Don't close it yet
            data.pop("plan_status", None)
        result = self.client.get_put("/incidents/{}".format(incident_id),
                                     lambda incident: update_with_result(incident, data),
                                     co3_context_token=event.context)
        if status in ["C", "Closed"]:
            # Now close the incident
            data = {"plan_status": status}
            result = self.client.get_put("/incidents/{}".format(incident_id),
                                         lambda incident: update_with_result(incident, data),
                                         co3_context_token=event.context)
        return result

    def update_incident_field(self, args, event, data):
        """Set a specific field in the incident, from raw data"""
        fieldname = args.get("field", "unspecified_field_name")
        payload = {"properties": {fieldname: data}}
        return self.update_incident(args, event, payload)

    def update_task(self, args, event, data):
        """Update with data"""
        if not isinstance(data, dict):
            data = json.loads(data)
        task_id = event.task["id"]
        return self.client.get_put("/tasks/{}".format(task_id),
                                   lambda task: update_with_result(task, data),
                                   co3_context_token=event.context)

    def update_note(self, args, event, data):
        """Update with data"""
        if not isinstance(data, dict):
            data = json.loads(data)
        incident_id = event.incident["id"]
        note_id = event.note["id"]
        return self.client.get_put("/incidents/{}/comments/{}".format(incident_id, note_id),
                                   lambda note: update_with_result(note, data),
                                   co3_context_token=event.context)

    def update_milestone(self, args, event, data):
        """Update with data"""
        if not isinstance(data, dict):
            data = json.loads(data)
        incident_id = event.incident["id"]
        milestone_id = event.milestone["id"]
        # Milestones don't support get_put because they don't individually support 'get' (in v23)
        # So just apply the update to the existing milestone data and then `put`
        # Note, this may cause undetected conflicts!
        return self.client.put("/incidents/{}/milestones/{}".format(incident_id, milestone_id),
                               update_with_result(event.milestone, data),
                               co3_context_token=event.context)

    def update_artifact(self, args, event, data):
        """Update with data"""
        if not isinstance(data, dict):
            data = json.loads(data)
        incident_id = event.incident["id"]
        artifact_id = event.artifact["id"]
        return self.client.get_put("/incidents/{}/artifacts/{}".format(incident_id, artifact_id),
                                   lambda artifact: update_with_result(artifact, data),
                                   co3_context_token=event.context)

    # Add new (tasks, notes, etc)

    def new_incident(self, args, event, data):
        """Add a new incident from data"""
        if not (isinstance(data, dict) or isinstance(data, list)):
            # Data was probably a string, load it
            data = json.loads(data)
        if isinstance(data, list):
            # Load each of the things in the list
            return [self.new_incident(args, event, item) for item in data]
        ctx = None
        if event is not None:
            ctx = event.context
        return self.client.post("/incidents", data, co3_context_token=ctx)

    def new_task(self, args, event, data):
        """Add a new task to the event's incident"""
        if not (isinstance(data, dict) or isinstance(data, list)):
            # Data was probably a string, load it
            data = json.loads(data)
        if isinstance(data, list):
            # Load each of the things in the list
            return [self.new_task(args, event, item) for item in data]
        incident_id = event.incident["id"]
        return self.client.post("/incidents/{}/tasks".format(incident_id), data, co3_context_token=event.context)

    def new_note(self, args, event, data):
        """Add a new note to the event's incident"""
        if not (isinstance(data, dict) or isinstance(data, list)):
            # Data was probably a string, load it
            data = json.loads(data)
        if isinstance(data, list):
            # Load each of the things in the list
            return [self.new_note(args, event, item) for item in data]
        incident_id = event.incident["id"]
        return self.client.post("/incidents/{}/comments".format(incident_id), data, co3_context_token=event.context)

    def new_note_text(self, args, event, data):
        """Add a new note to the event's incident. Wraps the 'data' string payload into a comment DTO"""
        incident_id = event.incident["id"]
        return self.client.post("/incidents/{}/comments".format(incident_id),
                                {"text" : {"format" : "text", "content" : data}},
                                co3_context_token=event.context)

    def new_milestone(self, args, event, data):
        """Add a new milestone to the event's incident"""
        if not (isinstance(data, dict) or isinstance(data, list)):
            # Data was probably a string, load it
            data = json.loads(data)
        if isinstance(data, list):
            # Load each of the things in the list
            return [self.new_milestone(args, event, item) for item in data]
        incident_id = event.incident["id"]
        return self.client.post("/incidents/{}/milestones".format(incident_id), data, co3_context_token=event.context)

    def new_artifact(self, args, event, data):
        """Add a new artifact to the event's incident.  NOTE: result is a list"""
        if not (isinstance(data, dict) or isinstance(data, list)):
            # Data was probably a string, load it
            data = json.loads(data)
        if isinstance(data, list):
            # Load each of the things in the list
            return [self.new_artifact(args, event, item) for item in data]
        incident_id = event.incident["id"]
        return self.client.post("/incidents/{}/artifacts".format(incident_id), data, co3_context_token=event.context)

    def new_attachment(self, args, event, data):
        """Add a new attachment to the event's incident.  Data can be string or binary or JSON-serializable dict."""
        LOG.debug("Attachment data of type %s", type(data))
        incident_id = event.incident["id"]
        attachment_filename = args.get("filename", "attachment.dat")
        mode = "wb"
        if not isinstance(data, bytes):
            mode = "wt"
        if isinstance(data, list):
            data = json.dumps(data, indent=2, sort_keys=True)
        if isinstance(data, dict):
            data = json.dumps(data, indent=2, sort_keys=True)
        with tempfile.NamedTemporaryFile(mode=mode, delete=False) as temp_file:
            temp_filename = temp_file.name
            temp_file.write(data)
        result = self.client.post_attachment('/incidents/{0}/attachments'.format(incident_id),
                                             temp_filename,
                                             filename=attachment_filename,
                                             co3_context_token=event.context)
        os.remove(temp_filename)
        return result


def test():
    """Test some basic functionality"""
    from resilient_circuits.rest_helper import get_resilient_client
    from resilient_circuits.actions_component import ActionMessage
    import time

    opts = vars(resilient.ArgumentParser(config_file=os.environ.get("APP_CONFIG_FILE")).parse_args())
    client = get_resilient_client(opts)

    action_event = None
    result = Disposition(client, "new_incident").call(action_event, {"name": "new test incident", "discovered_date": 0})
    LOG.debug(result)
    assert result["id"] > 0
    print("Created incident {}".format(result["id"]))
    incident = result

    action_event = ActionMessage(message={"incident": incident})
    result = Disposition(client, "new_task").call(action_event, {"name": "new task"})
    LOG.debug(result)
    assert result["id"] > 0
    action_event.task = result
    result = Disposition(client, "update_task").call(action_event, {"name": "updated task"})
    LOG.info(result)

    result = Disposition(client, "new_note").call(action_event, {"text": "new note"})
    LOG.debug(result)
    assert result["id"] > 0
    action_event.note = result
    result = Disposition(client, "update_note").call(action_event, {"text": "updated note"})
    LOG.info(result)

    t_now = int(time.time() * 1000)
    result = Disposition(client, "new_milestone").call(action_event, {"date": t_now, "title": "new milestone"})
    LOG.debug(result)
    assert result["id"] > 0
    action_event.milestone = result
    result = Disposition(client, "update_milestone").call(action_event, {"title": "updated milestone"})
    LOG.info(result)

    result = Disposition(client, "new_artifact").call(action_event, {"type": "DNS Name", "value": "rtfm.mit.edu"})
    LOG.debug(result)
    assert result[0]["id"] > 0
    action_event.artifact = result[0]
    result = Disposition(client, "update_artifact").call(action_event, {"description": "updated artifact"})
    LOG.info(result)

    result = Disposition(client, "new_attachment").call(action_event, "string value\nfor attachment")
    result = Disposition(client, "new_attachment").call(action_event, u"unicode value\nfor attachment")
    result = Disposition(client, "new_attachment").call(action_event, b"bytes value\nfor attachment")
    result = Disposition(client, "new_attachment").call(action_event, {"value": "json value\nfor attachment"})

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    import doctest
    doctest.testmod()
    # test()
