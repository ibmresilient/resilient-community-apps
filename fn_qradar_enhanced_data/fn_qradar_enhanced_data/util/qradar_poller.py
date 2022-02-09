# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
import logging
from fn_aws_guardduty.fn_aws_guardduty.util.config import STOP_THREAD
from fn_qradar_enhanced_data.util.function_utils import get_servers_list
from fn_aws_guardduty.fn_aws_guardduty.lib.aws_gd_poller import WAIT_MULTIPLIER

LOG = logging.getLogger(__name__)
# Multiplier to convert minutes to seconds
WAIT_MULTIPLIER = 60
STOP_THREAD = False

class QRadarPoller():
    """Component that polls for updates to incident"""

    def __init__(self, opts, polling_interval):
        self.polling_interval = polling_interval
        self.opts = opts
        self.servers_list = get_servers_list(opts)

    def run(self):
        """"Run polling thread, alternately check for new data and wait"""

        while not STOP_THREAD:
            #check for updated information
            LOG.info("Polling QRadar incident {} for ".format())


