# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_scheduler
"""
import logging
from fn_scheduler.components import SECTION_SCHEDULER
from fn_scheduler.lib.scheduler_helper import ResilientScheduler

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get(SECTION_SCHEDULER, {})

    scheduler = None
    state = None
    reason = None
    try:
        scheduler = ResilientScheduler(options.get("datastore_dir"),
                                       options.get("thread_max"),
                                       options.get("timezone"))

        job = scheduler.get_scheduler().add_job(myfunc, 'interval', minutes=2)
        job.remove()

        state = "success"
    except Exception as e:
        state = "failure"
        reason = str(e)
    finally:
        if scheduler:
            scheduler.get_scheduler().shutdown()

    return {
        "state": state,
        "reason": reason
    }

def myfunc():
    """
    dummy function for job triggers
    :return:
    """
    return