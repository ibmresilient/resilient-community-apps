# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError, StatusMessage
from resilient_lib import ResultPayload
from fn_scheduler.components import SECTION_SCHEDULER
from fn_scheduler.lib.scheduler_helper import ResilientScheduler

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'list_scheduled_jobs"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        options = opts.get(SECTION_SCHEDULER, {})

        self.res_scheduler = ResilientScheduler(options.get("datastore_dir"),
                                                options.get("thread_max"),
                                                options.get("timezone"))

    @function("list_scheduled_jobs")
    def _create_a_schedule_function(self, event, *args, **kwargs):
        try:
            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            # Produce a FunctionResult with the results
            scheduler = ResilientScheduler.get_scheduler()
            jobs = scheduler.get_jobs()

            list_jobs = []

            for job in jobs:
                job_json = self.res_scheduler.job_to_json(job)

                # hide settings with contain passwords
                params = list(job_json['args'])
                params[8] = None
                job_json['args'] = tuple(params)
                list_jobs.append(job_json)

            log.debug(list_jobs)
            if len(list_jobs) == 0:
                yield StatusMessage("No scheduled jobs")

            result = rc.done(True, list_jobs)
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()
