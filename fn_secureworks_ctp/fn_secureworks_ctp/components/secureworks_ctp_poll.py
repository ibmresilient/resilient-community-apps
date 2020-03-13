# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation"""

import logging
import threading
from circuits import Event, Timer, task
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields
from fn_secureworks_ctp.lib.scwx_client import SCWXClient


CONFIG_DATA_SECTION = "fn_secureworks_ctp"
SCWX_CTP_POLL_CHANNEL = "scwx_ctp_poll"
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

        LOG.info(u"Secureworks CTP escalation initiated, polling interval %s", self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info("Secureworks CTP poll start")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info("Secureworks CTP poll completed")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["base_url", "username", "password", "query_ticket_types",
                           "query_grouping_types", "polling_interval"]
        validate_fields(required_fields, self.options)
        self.scwx_client = SCWXClient(self.opts, self.options)
        # Timer interval (seconds).  Default 10 minutes.
        self.polling_interval = int(self.options.get("polling_interval", 600))

    def _escalate(self):
        """ Search for Sercureworks CTP tickets and create incidents in Resilient for them
        :return:
        """
        LOG.info("Secureworks CTP escalate.")
        try:


            response = self.scwx_client.post_tickets_updates()
            tickets = response.get('tickets')
            for ticket in tickets:
                response_ack = self.scwx_client.post_tickets_acknowledge(ticket)
                if response_ack.get("code") == "SUCCESS":

        except Exception as err:
            raise err
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())