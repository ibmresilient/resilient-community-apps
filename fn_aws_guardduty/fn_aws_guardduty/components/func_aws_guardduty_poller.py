# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Findings poller for AWS GuardDuty """
import logging
import time
from threading import Thread
import sys

from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields
from fn_aws_guardduty.lib.aws_gd_poller import AwsGdPoller
import fn_aws_guardduty.util.config as config

LOG = logging.getLogger(__name__)
# Default polling interval in minutes.
POLLING_INTERVAL_DEFAULT = 10
TIMEOUT_MULTIPLIER = 60
# Extra padding in secs to wait for thread to exit.
TIMEOUT_WAIT = 10


class FuncAwsGuarddutyPoller(ResilientComponent):
    """Component that polls for new findings from AWS GuardDuty"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FuncAwsGuarddutyPoller, self).__init__(opts)
        self.options = opts.get("fn_aws_guardduty", {})
        self.opts = opts
        if int(self.options.get("aws_gd_polling_interval", POLLING_INTERVAL_DEFAULT)) == 0:
            LOG.info("Polling for findings in AWS GuardDuty not enabled")
        else:
            validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)
            config.STOP_THREAD = False
            self.threads = []
            self.poller_setup()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_aws_guardduty", {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)
        config.STOP_THREAD = True
        self.poller_setup()

    def poller_setup(self):
        """Instantiate poller object and setup polling thread"""

        # Amount of time (minutes) to wait to check findings again, use default if not set.
        polling_interval = int(self.options.get("aws_gd_polling_interval", POLLING_INTERVAL_DEFAULT))

        aws_gd_poller = AwsGdPoller(self.opts, self.options, polling_interval)
        # Use a timeout value of polling_interval (in secs) * WAIT_MULTIPLIER + TIMEOUT_WAIT secs to wait for
        # all threads to end.
        thread_timeout = (polling_interval * TIMEOUT_MULTIPLIER) + TIMEOUT_WAIT

        # Wait for threads to stop within thread timeout interval.
        stop_time = time.time() + thread_timeout
        while any(t.isAlive() for t in self.threads) and (time.time() < stop_time):
            time.sleep(0.1)

        # Get rid of stopped threads from list.
        self.threads = [t for t in self.threads if t.is_alive()]

        if self.threads:
            # Polling threads still running raise runtime error.
            LOG.error("There were %d polling threads which did not stop within timeout period on restart",
                      len(self.threads))
            raise RuntimeError("There were {} polling threads which did not stop within timeout period on restart."
                               .format(len(self.threads)))

        # Turn off "STOP_THREAD" flag.
        config.STOP_THREAD = False

        # Create and start polling thread
        thread = Thread(target=aws_gd_poller.run)
        self.threads.append(thread)
        thread.daemon = True
        thread.start()
        LOG.info("Polling for findings in AWS GuardDuty every %d minutes", polling_interval)
