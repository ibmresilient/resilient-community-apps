# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_splunk_integration.util import splunk_utils

SECTION_HDR = "fn_splunk_integration"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'splunk_update_notable"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(SECTION_HDR, {})

    @function("splunk_update_notable")
    def _splunk_update_notable_function(self, event, *args, **kwargs):
        """Function: Update notable events according to the status of the corresponding incident.

        Inputs:
            event_id:   the notable event id in the splunk_notable_event_id field
            comment:    add a note to the notable event
            status:     Notable event status. Integer: 2=active, 5= closed
        """
        try:
            # Get the function parameters:
            event_id = kwargs.get("event_id")  # text
            comment = kwargs.get("comment")  # text
            notable_event_status = kwargs.get("notable_event_status")  # number

            splunk_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                splunk_verify_cert = False

            log = logging.getLogger(__name__)
            log.info("event_id: %s", event_id)
            log.info("comment: %s", comment)
            log.info("notable_event_status: %s", notable_event_status)
            log.info("splunk_verify_cert: " + str(splunk_verify_cert))

            log.info("Splunk host: %s, port: %s, username: %s",
                     self.options["host"], self.options["port"], self.options["username"])

            yield StatusMessage("starting...")

            result_payload = ResultPayload(SECTION_HDR, **kwargs)

            splnk_utils = splunk_utils.SplunkUtils(host=self.options["host"],
                                                   port=self.options["port"],
                                                   username=self.options["username"],
                                                   password=self.options["splunkpassword"],
                                                   verify=splunk_verify_cert)

            splunk_result = splnk_utils.update_notable(event_id=event_id,
                                                 comment=comment,
                                                 status=notable_event_status,
                                                 cafile=splunk_verify_cert)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the return value
            yield FunctionResult(result_payload.done(True, splunk_result.get('content', {})))
        except Exception as e:
            log.error("Function execution throws exception: {}".format(str(e)))
            yield FunctionError()
