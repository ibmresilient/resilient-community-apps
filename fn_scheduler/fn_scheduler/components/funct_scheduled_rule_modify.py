# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_scheduler.components import SECTION_SCHEDULER as PACKAGE_NAME
from fn_scheduler.lib.scheduler_helper import ResilientScheduler

FN_NAME = "scheduled_rule_modify"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'scheduled_rule_modify'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        self.options = opts.get(PACKAGE_NAME, {})

        self.res_scheduler = ResilientScheduler(self.options.get("db_url"),
                                                self.options.get("datastore_dir"),
                                                self.options.get("thread_max"),
                                                self.options.get("timezone"))

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Modify an existing schedule
        Inputs:
            -   fn_inputs.scheduler_type
            -   fn_inputs.scheduler_rule_parameters
            -   fn_inputs.scheduler_type_value
            -   fn_inputs.scheduler_label
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        inputs = fn_inputs._asdict()
        validate_fields(["scheduler_label"], inputs)

        self.LOG.info("scheduler_label: %s", fn_inputs.scheduler_label)

        job = self.res_scheduler.get_job_by_id(fn_inputs.scheduler_label)
        if job is None:
            raise KeyError("Job not found: {}".format(fn_inputs.scheduler_label))

        job_state = job.__getstate__()   # get all the parameters
        self.LOG.debug(job_state)
        changes = {}
        # changes to scheduler_type and value?
        if inputs.get("scheduler_type") and inputs.get("scheduler_type_value"):
            # validate the type and type_value
            changes['trigger'] = self.res_scheduler.build_trigger(inputs.get("scheduler_type"), inputs.get("scheduler_type_value"))

        if inputs.get("scheduler_rule_parameters"):
            rule_params = self.res_scheduler.validate_rule_parameters(inputs.get("scheduler_rule_parameters"))

            # replace the specific parameters for the rule/playbook
            incident_data = list(job_state.get('args', ()))
            incident_data[7] = rule_params
            changes['args'] = incident_data
            changes['kwargs'] = incident_data # values repeated here

        self.LOG.debug(changes)
        job.modify(**changes)

        # get the updated job
        updated_job = self.res_scheduler.get_job_by_id(job_state.get("id"))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(ResilientScheduler.sanitize_job(updated_job))
