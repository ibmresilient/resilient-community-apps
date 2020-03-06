# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
from resilient_circuits import ResilientComponent
from resilient_lib import IntegrationError, RequestsCommon, ResultPayload
from fn_secureworks_ctp.lib.scwx_client import SCWXClient

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = "fn_secureworks_ctp"

class SecureworksCTPProcess(ResilientComponent):

    def __init__(self, opts):
        LOG.info("Init")
        super(SecureworksCTPProcess, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self.polling_interval = int(self.options.get("polling_interval", 600))
        if self.polling_interval == 0:
            log.warn("Secureworks CTP escalation interval is not configured.  Automated escalation is disabled.")
            return
        self.scwx_client = SCWXClient(self.options)
        self.rest_client = self.rest_client()

    def poll_start(self):
        """Handle the timer"""
        LOG.info("Secureworks CTP poll started.")
        self.escalate()

    def run(self):
        LOG.info("Secureworks CTP run.")
        try:
            self.poll_start()
        except Exception as err:
            LOG.error("Encountered Exception: {}.".format(str(err)))

    def escalate(self):
        """ Search for Sercureworks CTP tickets and create incidents in Resilient for them
        :return:
        """
        LOG.info("Secureworks CTP escalate.")
        try:
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            tickets_list = self.scwx_client.post_tickets_updates()
        except Exception as err:
            raise err
