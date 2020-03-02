# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation"""

import logging
import threading
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields
from fn_secureworks_ctp.lib.secureworks_ctp_helper import SecureworksCTPProcess

CONFIG_DATA_SECTION = 'fn_secureworks_ctp'
SCWX_CTP_POLL_CHANNEL = "scwx_ctp_escalation"
TICKET_ID_FIELDNAME = "scwx_ctp_ticket_id"
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (SCWX_CTP_POLL_CHANNEL,)
    LOG.info("class Poll")

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (SCWX_CTP_POLL_CHANNEL,)
    LOG.info("class Poll complete")

class SecureworksCTPPollComponent(ResilientComponent):
    """
    Event-driven polling for Secureworks CTP tickets
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = SCWX_CTP_POLL_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SecureworksCTPPollComponent, self).__init__(opts)

        self._load_options(opts)

        if self.polling_interval == 0:
            LOG.info(u"Secureworks CTP escalation interval is not configured.  Automated escalation is disabled.")
            return

        scwx_poll = SecureworksCTPProcess(opts)
        self.scwx_thread = threading.Thread(target=scwx_poll.run)
        self.scwx_thread.daemon = True

        Timer(self.polling_interval, Poll(), persist=True).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.debug("Secureworks CTP poll timer initiated")
        scwx_poll = SecureworksCTPProcess(self.options)
        try:
            if self.scwx_thread.is_alive() == True:
                LOG.info("Secureworks CTP Thread already running.")
            else:
                LOG.info("Secureworks CTP Thread is not running.")
                self.scwx_thread = threading.Thread(target=scwx_poll.run)
                self.scwx_thread.daemon = True
                self.scwx_thread.start()
        except Exception as err:
            LOG.error("Error starting the Secureworks CTP thread: {}".format(str(err)))

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["base_url", "username", "password", "query_ticket_type",
                           "query_ticket_group", "polling_interval"]
        validate_fields(required_fields, self.options)

        # Timer interval (seconds).  Default 10 minutes.
        self.polling_interval = int(self.options.get("polling_interval", 600))


    def _escalate(self):
        """Query the Secureworks CTP endpoint for new tickets, and raise them to Resilient"""
        LOG.info(u"Getting list of open tickets")
