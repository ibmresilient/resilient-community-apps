# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.resilient_helper import get_incident, get_rule_by_id, add_comment, \
    lookup_object_type
from resilient import SimpleHTTPException
from resilient_lib import str_to_bool
from resilient_circuits.rest_helper import get_resilient_client

LOG = logging.getLogger(__name__)

def triggered_job(incident_id, object_id, row_id,
                  scheduler_label,
                  rule_name, rule_id, rule_object_type_id, rule_params,
                  is_playbook, options, **kwargs):
    """
    This function is called when a scheduled rule is triggered. It is run asynchronous of the create_scheduled_rule process.
    It's role is to build the api call-back to Resilient to run the rule.
    In addition to invoking a rule, a note is added to the incideent to indicate that a scheduled rule was run.
    :param incident_id:
    :param object_id: task_id, note_id, artifact_id, etc.
    :param row_id: used when object_id is a datatable_id
    :param scheduler_label:
    :param rule_name:
    :param rule_id:
    :param rule_object_type_id: internal id referring to incident, task, artifact, etc.
    :param rule_params:
    :param is_playbook: true if a playbook, false if a rule
    :param options: contains [fn_scheduler] parameters
    :param kwargs: catch all for additional arguments as necessary
    :return: None
    """
    LOG.debug(incident_id)
    LOG.debug(rule_id)
    LOG.debug(rule_object_type_id)
    LOG.debug(rule_params)
    LOG.debug(kwargs)

    disable_notes = str_to_bool(options.get("disable_notes", False))
    LOG.debug(disable_notes)

    # get the rest client
    scheduler = ResilientScheduler.get_scheduler(None, None, None, None, None)
    rest_client = get_resilient_client(scheduler.resilient_connection)

    # make sure the incident is still open and not deleted
    try:
        resp = get_incident(rest_client, incident_id)
    except SimpleHTTPException:
        resp = None

    if not resp or resp['end_date'] is not None:
        LOG.warning(u"Incident %s is not found or closed. Removing scheduled rule: %s", incident_id, rule_name)
        scheduler.remove_job(scheduler_label)
        return

    # make sure the rule is still enabled
    try:
        get_rule_by_id(rest_client, rule_id, is_playbook)
    except KeyError as err:
        # remove rules which no longer exist
        LOG.error(u"Rule/Playbook '%s' not found and schedule will be removed.", rule_name)
        (not disable_notes) and add_comment(rest_client, incident_id, u"Error running rule '{}': {}".format(scheduler_label, str(err)))
        scheduler.remove_job(scheduler_label)
        return

    # build url for invoking a rule
    rule_type = lookup_object_type(rest_client, rule_object_type_id)
    if rule_type == "tasks":
        url = "/{}/{}".format(rule_type, object_id)
    else:
        url = "/incidents/{}".format(incident_id)

        if rule_type != '':
            url = url + "/{}/{}".format(rule_type, object_id)

    if row_id:
        url = url + "/row_data/{}".format(row_id)

    url = url + "/action_invocations"

    # build the JSON for rule
    payload = {
        "action_id": rule_id
    }
    if is_playbook:
        payload["type_id_handle"] = {"name":"playbookfields"}
    if rule_params:
        payload["properties"] = rule_params

    LOG.info("Executing rule/playbook '%s:%s' for incident %s.",
        scheduler_label, rule_name, incident_id)
    LOG.debug(payload)

    # run the rule
    try:
        resp = rest_client.post(url, payload)
        LOG.debug(resp)
    except SimpleHTTPException as err:
        # is the object removed?
        if "Not Found" in str(err):
            LOG.error("Object not found and schedule will be removed for rule/playbook '%s'", rule_id)
            scheduler.remove_job(scheduler_label)
        else:
            LOG.error("An error occurred for rule/playbook '%s': %s", rule_id, str(err))
        (not disable_notes) and add_comment(rest_client, incident_id, u"Error running rule/playbook '{}': {}".format(scheduler_label, str(err)))
        return

    if rule_type:
        (not disable_notes) and add_comment(rest_client, incident_id, u"Scheduled job '{}' run on {}: {}".format(rule_name, rule_type, object_id))
    else:
        (not disable_notes) and add_comment(rest_client, incident_id, u"Scheduled job '{}' run on incident".format(rule_name))
