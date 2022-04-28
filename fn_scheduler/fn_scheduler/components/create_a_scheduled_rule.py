# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError, StatusMessage
from resilient_lib import ResultPayload
from fn_scheduler.components import SECTION_SCHEDULER, SECTION_RESILIENT
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.resilient_helper import get_incident, get_rule_by_name, validate_app_config
from fn_scheduler.lib.triggered_job import triggered_job

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'create_a_scheduled_job"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        resilient_connection = opts.get(SECTION_RESILIENT, {})

        options = opts.get(SECTION_SCHEDULER, {})

        validate_app_config(options)

        self.res_scheduler = ResilientScheduler.get_scheduler(options.get("db_url"),
                                                              options.get("datastore_dir"),
                                                              options.get("thread_max"),
                                                              options.get("timezone"),
                                                              resilient_connection)


    @function("create_a_scheduled_rule")
    def _create_a_schedule_function(self, event, *args, **kwargs):
        """Function: Schedule a rule to run on a schedule. This rule will be executed for a given incident, artifact, task, etc."""
        try:
            # Get the function parameters:
            scheduler_type = self.get_select_param(kwargs.get("scheduler_type"))  # select, values: "cron", "interval", "date"
            scheduler_type_value = kwargs.get("scheduler_type_value")  # text
            scheduler_rule_name = kwargs.get("scheduler_rule_name")  # text
            scheduler_rule_parameters = kwargs.get("scheduler_rule_parameters")  # text
            scheduler_label_prefix = kwargs.get("scheduler_label_prefix")  # text
            scheduler_is_playbook = kwargs.get("scheduler_is_playbook", False) # boolean

            incident_id = kwargs.get("incident_id")  # number
            object_id = kwargs.get("object_id")  # number
            # row_id is presently unavailable from a pre-proessing script.
            # A future change to resilient is needed to allow this natively. Presently, supplying this information manually is needed
            row_id = kwargs.get("row_id") # number

            if row_id:
                object_id = event.message["workflow"]["object_type"]['id']

            object_type_id = event.message["workflow"]["object_type"]['id']
            object_type_name = event.message["workflow"]["object_type"]['name']

            scheduler_label_prefix = "{}-{}".format(scheduler_label_prefix, incident_id)

            LOG.info("scheduler_type: %s", scheduler_type)
            LOG.info("scheduler_type_value: %s", scheduler_type_value)
            LOG.info("scheduler_rule_name: %s", scheduler_rule_name)
            LOG.info("scheduler_rule_parameters: %s", scheduler_rule_parameters)
            LOG.info("scheduler_label_prefix: %s", scheduler_label_prefix)
            LOG.info("scheduler_is_playbook: %s", scheduler_is_playbook)

            LOG.info("incident_id: %s", incident_id)
            LOG.info("object_id: %s", object_id)
            LOG.info("row_id: %s", row_id)

            # get the rule id
            rest_client = self.rest_client()

            # make sure incident isn't closed
            resp = get_incident(rest_client, incident_id)
            if not resp.get("success", True):
                raise FunctionError("Incident {} not found".format(incident_id))

            if not resp or resp['end_date'] is not None:
                raise FunctionError("Incident is closed")

            # get the rule id
            rule_id, rule_object_type_id = get_rule_by_name(rest_client,
                                                            scheduler_rule_name.strip(),
                                                            scheduler_is_playbook)
            if not rule_id:
                raise ValueError(u"Rule/Playbook name not found: %s", scheduler_rule_name)

            if object_type_id != rule_object_type_id:
                raise ValueError(u"Rule/Playbook does not match the action object: %s", object_type_name)

            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            rule_params = None
            if scheduler_rule_parameters:
                rule_params = self.res_scheduler.validate_rule_parameters(scheduler_rule_parameters)

            incident_data = [incident_id, object_id, row_id,
                             scheduler_label_prefix,
                             scheduler_rule_name, rule_id, rule_object_type_id, rule_params,
                             scheduler_is_playbook,
                             self.opts[SECTION_SCHEDULER]]

            # validate the type and type_value
            trigger = self.res_scheduler.build_trigger(scheduler_type, scheduler_type_value)

            # a d d   j o b
            scheduler = self.res_scheduler.scheduler
            scheduled_job = scheduler.add_job(triggered_job,
                                              trigger,
                                              id=scheduler_label_prefix,
                                              args=incident_data,
                                              kwargs=rule_params)

            LOG.debug(u"Scheduled_job: {}".format(scheduled_job))

            yield StatusMessage("Rule scheduled")

            # get a clean copy for the results
            created_job = self.res_scheduler.get_job_by_id(scheduler_label_prefix)

            results = rc.done(True, ResilientScheduler.sanitize_job(created_job))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
