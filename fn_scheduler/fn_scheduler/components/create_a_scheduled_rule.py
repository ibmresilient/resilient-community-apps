# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError, StatusMessage
from resilient_circuits.rest_helper import get_resilient_client
from resilient_lib import ResultPayload, validate_fields
from fn_scheduler.components import SECTION_SCHEDULER, SECTION_RESILIENT
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.resilient_helper import get_incident, get_rule_by_id, get_rule_by_name, add_comment, lookup_object_type

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'create_a_scheduled_job"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        options = opts.get(SECTION_SCHEDULER, {})

        validate_fields(["datastore_dir", "thread_max", "timezone"], options)

        self.res_scheduler = ResilientScheduler(options.get("datastore_dir"),
                                                options.get("thread_max"),
                                                options.get("timezone"))


    @function("create_a_scheduled_rule")
    def _create_a_schedule_function(self, event, *args, **kwargs):
        """Function: Schedule a rule to run on a schedule. This rule will be executed for a given incident, artifact, task, etc."""
        try:
            # Get the function parameters:
            scheduler_type = self.get_select_param(kwargs.get("scheduler_type"))  # select, values: "cron", "interval", "date"
            scheduler_type_value = kwargs.get("scheduler_type_value")  # text
            scheduler_rule_name = kwargs.get("scheduler_rule_name")  # text
            scheduler_rule_parameters = kwargs.get("scheduler_rule_parameters")  # text
            scheduler_label = kwargs.get("scheduler_label")  # text

            incident_id = kwargs.get("incident_id")  # number
            object_id = kwargs.get("object_id")  # number
            # row_id is presently unavailable from a pre-proessing script.
            # A future change to resilient is needed to allow this natively. Presently, supplying this information manually is needed
            row_id = kwargs.get("row_id") # number

            if row_id:
                object_id = event.message["workflow"]["object_type"]['id']

            object_type_id = event.message["workflow"]["object_type"]['id']
            object_type_name = event.message["workflow"]["object_type"]['name']

            log.info("scheduler_type: %s", scheduler_type)
            log.info("scheduler_type_value: %s", scheduler_type_value)
            log.info("scheduler_rule_name: %s", scheduler_rule_name)
            log.info("scheduler_rule_parameters: %s", scheduler_rule_parameters)
            log.info("scheduler_label: %s", scheduler_label)

            log.info("incident_id: %s", incident_id)
            log.info("object_id: %s", object_id)
            log.info("row_id: %s", row_id)

            # get the rule id
            rest_client = self.rest_client()

            # make sure incident isn't closed
            resp = get_incident(rest_client, incident_id)
            if not resp.get("success", True):
                raise FunctionError("Incident {} not found".format(incident_id))

            if not resp or resp['end_date'] is not None:
                raise FunctionError("Incident is closed")

            # get the rule id
            rule_id, rule_object_type_id = get_rule_by_name(rest_client, scheduler_rule_name.strip(' '))
            if not rule_id:
                raise ValueError(u"Rule name not found: %s", scheduler_rule_name)

            if object_type_id != rule_object_type_id:
                raise ValueError(u"Rule does not match the action object: %s", object_type_name)

            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            rule_params = None
            if scheduler_rule_parameters:
                rule_params = self.validate_rule_parameters(scheduler_rule_parameters)

            incident_data = [incident_id, object_id, row_id,
                             scheduler_label,
                             scheduler_rule_name, rule_id, rule_object_type_id, rule_params,
                             self.opts[SECTION_RESILIENT]]

            # validate the type and type_value
            trigger = self.res_scheduler.build_trigger(scheduler_type, scheduler_type_value)

            # a d d   j o b
            scheduler = ResilientScheduler.get_scheduler()
            scheduled_job = scheduler.add_job(triggered_job,
                                              trigger,
                                              id=scheduler_label,
                                              args=incident_data,
                                              kwargs=rule_params)

            log.debug(u"Scheduled_job: {}".format(scheduled_job))

            yield StatusMessage("Rule scheduled")

            # convert for results
            job = scheduled_job.__getstate__()
            job['next_run_time'] = self.res_scheduler.get_str_date(job['next_run_time'])
            job['trigger'] = None
            # clear args which contain passwords ([resilient])
            job = ResilientScheduler.clean_password(job)

            results = rc.done(True, job)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    def validate_rule_parameters(self, rule_params):
        """
        should be json formatted string
        :param rule_params: name=value;name=value
        :return: json data
        """
        params = {}
        if rule_params:
            for items in rule_params.split(';'):
                # improperly formatted parameters will fail with KeyError
                k, v = items.split('=')
                params[k.strip(' ').lower()] = v.strip(' ')

        return params

def triggered_job(incident_id, object_id, row_id,
                  scheduler_label,
                  rule_name, rule_id, rule_object_type_id, rule_params,
                  opts, **kwargs):
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
    :param opts: contains [resilient] parameters needed to connect back to Resilient for API calls
    :param kwargs: catch all for additional arguments as necessary
    :return: None
    """
    log.debug(incident_id)
    log.debug(rule_id)
    log.debug(rule_object_type_id)
    log.debug(rule_params)
    log.debug(kwargs)

    # get the rest client
    rest_client = get_resilient_client(opts)
    scheduler = ResilientScheduler.get_scheduler()

    # make sure the incident is still open
    resp = get_incident(rest_client, incident_id)
    if not resp or resp['end_date'] is not None:
        log.warning(u"Incident %s is not found or closed. Removing scheduled rule: %s", incident_id, rule_name)
        scheduler.remove_job(scheduler_label)
        return

    # make sure the rule is still enabled
    try:
        get_rule_by_id(rest_client, rule_id)
    except KeyError as err:
        # remove rules which no longer exist
        log.error(u"Rule '%s' not found and schedule will be removed.", rule_name)
        add_comment(rest_client, incident_id, u"Error running rule '{}': {}".format(scheduler_label, str(err)))
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
        "action_id": rule_id,
        "properties": rule_params
    }

    log.info("Executing Rule '{}:{}' for Incident {}".format(scheduler_label, rule_name, incident_id))

    # run the rule
    resp = rest_client.post(url, payload)
    log.debug(resp)
    if rule_type:
        add_comment(rest_client, incident_id, u"Scheduled job '{}' run on {}: {}".format(rule_name, rule_type, object_id))
    else:
        add_comment(rest_client, incident_id, u"Scheduled job '{}' run on incident".format(rule_name))
