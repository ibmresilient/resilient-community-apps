# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Incident poller for a ProofPoint TRAP server """
#from builtins import len, ValueError, Exception, super

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_circuits.rest_helper import get_resilient_client
from resilient_lib import validate_fields, ResultPayload, validate_fields
from fn_scheduler.lib.scheduler_helper import init_scheduler, build_trigger, job_to_json

"""
Summary: 

    Start the scheduler

"""

SECTION_NAME = "fn_scheduler"
SECTION_RESILIENT = "resilient"

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that polls for new data arriving from Proofpoint TRAP"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        self.opts = opts
        self.options = opts.get(SECTION_NAME, {})
        self.validate_app_config()
        self.timezone = self.options.get("timezone")

        self.scheduler = init_scheduler(self.options.get("datastore_dir"),
                                        self.options.get("thread_max"),
                                        self.options.get("timezone"))
        log.info("Scheduler started")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_NAME, {})
        self.validate_app_config()


    def validate_app_config(self):
        validate_fields(('datastore_dir', 'thread_max', 'timezone'), self.options)
        return True

    @function("create_a_schedule")
    def _create_a_schedule_function(self, event, *args, **kwargs):
        """Function: Schedule a rule to run on a schedule. This rule will be executed for a given incident, artifact, task, etc."""
        try:
            # TODO
            # https://localhost:1443/rest/orgs/201/incidents/2219/table_data/1001/row_data/

            # Get the function parameters:
            scheduler_type = self.get_select_param(kwargs.get("scheduler_type"))  # select, values: "cron", "interval", "date"
            scheduler_type_value = kwargs.get("scheduler_type_value")  # text
            scheduler_rule_name = kwargs.get("scheduler_rule_name")  # text
            scheduler_rule_parameters = kwargs.get("scheduler_rule_parameters")  # text
            scheduler_label = kwargs.get("scheduler_label")  # text

            incident_id = kwargs.get("incident_id")  # number
            object_id = kwargs.get("object_id")  # number
            row_id = kwargs.get("row_id") # number
            # TODO row_id is not possible

            if row_id:
                object_id = event.message["workflow"]["object_type"]['id']

            log = logging.getLogger(__name__)
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
            rule_id, rule_object_type = get_rule_by_name(rest_client, scheduler_rule_name.strip(' '))
            if not rule_id:
                raise ValueError("Rule name not found: %s", scheduler_rule_name)

            rc = ResultPayload(SECTION_NAME, **kwargs)

            rule_params = None
            if scheduler_rule_parameters:
                rule_params = self.validate_rule_parameters(scheduler_rule_parameters)

            incident_data = [incident_id, object_id, row_id, scheduler_rule_name,
                             rule_id, rule_object_type, self.opts[SECTION_RESILIENT], rule_params]

            # validate the type and type_value
            trigger = build_trigger(scheduler_type, scheduler_type_value, self.timezone)

            # a d d   j o b
            scheduled_job = self.scheduler.add_job(triggered_job,
                                                   trigger,
                                                   id=scheduler_label,
                                                   args=incident_data,
                                                   kwargs=rule_params)
            log.debug("Scheduled_job: {}".format(scheduled_job))

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = rc.done(True, scheduled_job.__getstate__())

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
        for items in rule_params.split(';'):
            k,v = items.split('=')
            params[k.strip(' ').lower()] = v.strip(' ')

        return params

    @function("remove_a_scheduled_job")
    def _remove_a_scheduled_job(self, event, *args, **kwargs):
        try:
            scheduler_label = kwargs.get("scheduler_label")  # text
            log.info("scheduler_label: %s", scheduler_label)
            validate_fields(["scheduler_label"], kwargs)

            rc = ResultPayload(SECTION_NAME, **kwargs)

            self.scheduler.remove_job(scheduler_label)

            result = rc.done(True, None)
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()

    @function("list_schedules")
    def _create_a_schedule_function(self, event, *args, **kwargs):
        try:
            rc = ResultPayload(SECTION_NAME, **kwargs)

            # Produce a FunctionResult with the results
            jobs = self.scheduler.get_jobs()

            list_jobs = []

            for job in jobs:
                list_jobs.append(job_to_json(job))

            result = rc.done(True, list_jobs)
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()

def triggered_job(incident_id, object_id, row_id, rule_name, rule_id, rule_object_type, rule_params, opts, **kwargs):
    log.debug(incident_id)
    log.debug(rule_id)
    log.debug(rule_object_type)
    log.debug(rule_params)
    log.debug(kwargs)
    """
    https://localhost:1443/rest/orgs/201/incidents/2219/artifacts/87/action_invocations
{"action_id":29,"properties":{"trap_list_id":100,"trap_description":"abc","trap_expiration":1568174400000,"trap_duration":100}}
    https://localhost:1443/rest/orgs/201/incidents/2219/table_data/1001/row_data/1/action_invocations
    """

    # get the rest client
    rest_client = get_resilient_client(opts)

    # make sure the incident is still open
    resp = get_incident(rest_client, incident_id)
    if not resp or resp['end_date'] is not None:
        log.warning("Incident %s is not found or closed. Removing scheduled job: %s", incident_id, rule_name)
        # scheduler.remove_job(rule_name)
        return

    # make sure the rule is still enabled
    get_rule_by_id(rest_client, rule_id)

    # build url for invoking a rule
    rule_type = lookup_object_type(rest_client, rule_object_type)
    url = "/incidents/{}".format(incident_id)

    if rule_type != '':
        url = url + "/{}/{}".format(rule_type, object_id)

    if row_id:
        url = url + "/row_data/{}".format(row_id)

    url = url + "/action_invocations"

    # build the JSON for rule
    payload = { "action_id": rule_id,
                "properties": rule_params
              }

    # run the rule
    resp = rest_client.post(url, payload)
    log.debug(resp)
    if rule_type:
        add_comment(rest_client, incident_id, u"Scheduled job '{}' run on {}: {}".format(rule_name, rule_type, object_id))
    else:
        add_comment(rest_client, incident_id, u"Scheduled job '{}' run on incident".format(rule_name, rule_type, object_id))

def get_incident(rest_client, incident_id):
    url = "/incidents/{}".format(incident_id)
    resp = rest_client.get(url)

    return resp

def get_rule_by_name(rest_client, rule_name):
    rules = get_rules(rest_client)

    for rule in rules['entities']:
        if rule['name'].lower() == rule_name.lower():
            if not rule['enabled']:
                raise AttributeError("Rule is disabled")

            return (rule['id'], rule["object_type"])

    return (None, None)

def get_rule_by_id(rest_client, rule_id):
    """

    :param incident_id:
    :param rule_id:
    :return: True / False if rule is enabled for an incident
    """
    rules = get_rules(rest_client)

    for rule in rules['entities']:
        if rule['id'] == rule_id:
            if rule['enabled']:
                return True
            else:
                raise AttributeError("Rule is disabled")

    raise KeyError("Rule id %s is not found", rule_id)

def get_rules(rest_client):
    url = "/actions"

    return rest_client.get(url)

def add_comment(rest_client, incident_id, comment):
    url = "/incidents/{}/comments".format(incident_id)
    payload = {
        "text": {
            "format": "text",
            "content": comment
        }
    }

    resp = rest_client.post(url, payload)

def lookup_object_type(rest_client, type_id):
    """

    :param type: internal number of object
    :return: object name or ValueError if not found
    """
    lookup = ['', 'tasks', 'notes', 'milestones', 'artifacts', 'attachments', None, 'organizations']

    if type_id <= len(lookup):
        if lookup[type_id] is not None:
            return lookup[type_id]
    else:
        # check to see if a datatable
        url = "/types/{}".format(type_id)
        resp = rest_client.get(url)

        if resp['type_id'] == 8:
            return "table_data"

    raise ValueError("Rule type not supported")









