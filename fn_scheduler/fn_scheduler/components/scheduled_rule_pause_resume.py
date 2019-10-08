# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_scheduler.components import SECTION_SCHEDULER
from fn_scheduler.lib.scheduler_helper import ResilientScheduler

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'scheduled_rule_pause"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_scheduler", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_scheduler", {})

    @function("scheduled_rule_pause")
    def _scheduled_rule_pause_function(self, event, *args, **kwargs):
        """Function: Pause a scheduled rule"""
        try:
            # Get the function parameters:
            scheduler_label = kwargs.get("scheduler_label")  # text

            log = logging.getLogger(__name__)
            log.info("scheduler_label: %s", scheduler_label)

            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            job = self.find_job_by_label(scheduler_label)
            if job is None:
                raise KeyError("Job not found: {}".format(scheduler_label))

            job.pause()
            yield StatusMessage("Job paused: {}".format(scheduler_label))

            results = rc.done(True, ResilientScheduler.sanitize_job(job))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    @function("scheduled_rule_resume")
    def _scheduled_rule_resume_function(self, event, *args, **kwargs):
        """Function: Resume a scheduled job"""
        try:
            # Get the function parameters:
            scheduler_label = kwargs.get("scheduler_label")  # text

            log = logging.getLogger(__name__)
            log.info("scheduler_label: %s", scheduler_label)

            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            job = self.find_job_by_label(scheduler_label)
            if job is None:
                raise KeyError("Job not found: {}".format(scheduler_label))

            job.resume()
            yield StatusMessage("Job resumed: {}".format(scheduler_label))

            results = rc.done(True, ResilientScheduler.sanitize_job(job))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


    def find_job_by_label(self, scheduler_label):
        """
        find the job by it's label
        :param scheduler_label:
        :return: job found or None
        """
        scheduler = ResilientScheduler.get_scheduler()
        jobs = scheduler.get_jobs()

        for job in jobs:
            if job.id.lower() == scheduler_label.lower():
                return job

        return None
