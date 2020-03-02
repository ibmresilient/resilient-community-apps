# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
from resilient_circuits import ResilientComponent
from resilient_lib import IntegrationError, RequestsCommon, ResultPayload
LOG = logging.getLogger(__name__)

class SecureworksCTPProcess(object):

    def __init__(self, options):
        LOG.info("Init")

    def poll_start(self):
        """Handle the timer"""
        LOG.info("Secureworks CTP poll started.")
        self.escalate()

    def run(self):
        try:
            self.poll_start()
        except Exception as err:
            LOG.error("Encountered Exception: {}.".format(str(err)))

    def escalate(self):
        """ Search for Sercureworks CTP tickets and create incidents in Resilient for them
        :return:
        """
        rc = RequestsCommon(opts=self.opts, function_opts=self.options)