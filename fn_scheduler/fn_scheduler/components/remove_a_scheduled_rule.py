# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import logging
from apscheduler.jobstores.base import JobLookupError
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError, StatusMessage
from resilient_lib import validate_fields, ResultPayload
from fn_scheduler.components import SECTION_SCHEDULER, SECTION_RESILIENT
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.resilient_helper import validate_app_config

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'remove_a_scheduled_job"""

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

    @function("remove_a_scheduled_rule")
    def _remove_a_scheduled_job(self, event, *args, **kwargs):
        try:
            scheduler_label = kwargs.get("scheduler_label")  # text
            log.info(u"scheduler_label: %s", scheduler_label)
            validate_fields(["scheduler_label"], kwargs)

            rc = ResultPayload(SECTION_SCHEDULER, **kwargs)

            scheduler = self.res_scheduler.scheduler

            try:
                scheduler.remove_job(scheduler_label)
                log.info(u"Rule '{}' deleted".format(scheduler_label))

                yield StatusMessage("Scheduled rule removed")
                result = rc.done(True, None)
            except JobLookupError:
                yield StatusMessage("Scheduled rule not found")
                result = rc.done(False, None)

            yield FunctionResult(result)
        except Exception:
            yield FunctionError()
