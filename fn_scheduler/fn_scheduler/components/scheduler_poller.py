# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Incident poller for a ProofPoint TRAP server """

import logging
from resilient_circuits import ResilientComponent, handler
from fn_scheduler.components import SECTION_SCHEDULER
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from fn_scheduler.lib.resilient_helper import validate_app_config

"""
Summary:

    Start the scheduler

"""

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that polls for new data arriving from Proofpoint TRAP"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        options = opts.get(SECTION_SCHEDULER, {})
        validate_app_config(options)
        self.timezone = options.get("timezone")

        self.scheduler = ResilientScheduler(options.get("db_url"),
                                            options.get("datastore_dir"),
                                            options.get("thread_max"),
                                            options.get("timezone"))
        log.info("Scheduler started")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        options = opts.get(SECTION_SCHEDULER, {})
        validate_app_config(options)

        # TODO restart the scheduler

