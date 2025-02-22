# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError, StatusMessage
from resilient_lib import ResultPayload
from fn_scheduler.components import SECTION_SCHEDULER, SECTION_RESILIENT
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.resilient_helper import validate_app_config

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'list_scheduled_jobs"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        options = opts.get(SECTION_SCHEDULER, {})

        validate_app_config(options)

        resilient_connection = opts.get(SECTION_RESILIENT, {})
        self.res_scheduler = ResilientScheduler.get_scheduler(options.get("db_url"),
                                                              options.get("datastore_dir"),
                                                              options.get("thread_max"),
                                                              options.get("timezone"),
                                                              resilient_connection)

    @function("list_scheduled_rules")
    def _create_a_schedule_function(self, event, *args, **kwargs):
        incident_id = kwargs.get("incident_id")  # number
        log.info("incident_id: %s", incident_id)

        try:
            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            # Produce a FunctionResult with the results
            scheduler = self.res_scheduler.scheduler
            jobs = scheduler.get_jobs()

            list_jobs = []

            for job in jobs:
                job_json = ResilientScheduler.sanitize_job(job)
                params = list(job_json['args'])

                if incident_id is None or incident_id == 0 or \
                    incident_id == params[0]:
                    list_jobs.append(job_json)

            log.debug(list_jobs)
            if not list_jobs:
                yield StatusMessage("No scheduled jobs")

            result = rc.done(True, list_jobs)
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()
