# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Service listener implementation"""

import logging
from resilient_circuits import ResilientComponent
from fn_mcafee_opendxl.util.helper import verify_config, event_subscriber

log = logging.getLogger(__name__)


class DxlComponentListener(ResilientComponent):

    def __init__(self, opts):
        super(DxlComponentListener, self).__init__(opts)
        self.config = verify_config(opts)
        self.main()

    def main(self):
        if self.config["topic_listener_on"] == "True":
            res_client = self.rest_client()
            log.info("Service Listener called")

            event_subscriber(res_client, self.config)
        else:
            log.info("Event subscriber not listening. To turn on set topic_listener_on to True")
