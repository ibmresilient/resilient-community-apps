# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.triggered_job import triggered_job
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_scheduler"
FN_NAME = "run_schedule_job_now"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'run_schedule_job_now'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Run a scheduled job now
        Inputs:
            -   fn_inputs.scheduler_label
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        inputs = fn_inputs._asdict()
        validate_fields(["scheduler_label"], inputs)

        self.LOG.info("scheduler_label: %s", inputs['scheduler_label'])

        job = ResilientScheduler.get_scheduler(None, None, None, None, None).\
            get_job_by_id(fn_inputs.scheduler_label)
        if job is None:
            raise KeyError("Job not found: {}".format(inputs['scheduler_label']))

        job_state = job.__getstate__()   # get all the parameters
        self.LOG.debug(job_state)

        # separate into their own fields
        incident_id, object_id, row_id, \
        scheduler_label, \
        rule_name, rule_id, rule_object_type_id, rule_params, \
        is_playbook, options = job_state.get('args', ())

        triggered_job(incident_id, object_id, row_id,
                  scheduler_label,
                  rule_name, rule_id, rule_object_type_id, rule_params,
                  is_playbook, options)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult({})
