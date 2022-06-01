# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_lib import ResultPayload
from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME
from fn_splunk_integration.util.function_utils import get_servers_list
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkUtils
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

log = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'splunk_update_notable"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.servers_list = get_servers_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.servers_list = get_servers_list(opts)

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
            event_id = kwargs.get("event_id")                          # text
            comment = kwargs.get("comment")                            # text
            notable_event_status = kwargs.get("notable_event_status")  # number
            splunk_label = kwargs.get("splunk_label")                  # text

            options = SplunkServers.splunk_label_test(splunk_label, self.servers_list)

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            # Log all the info
            log.info("event_id: %s", event_id)
            log.info("comment: %s", comment)
            log.info("notable_event_status: %s", notable_event_status)
            log.info("splunk_verify_cert: " + str(splunk_verify_cert))
            log.info("splunk_label: %s", splunk_label)

            log.info("Splunk host: %s, port: %s, username: %s",
                     options.get("host"), options.get("port"), options.get("username"))

            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'splunk_update_notable' that was running in workflow '{}'".format(wf_instance_id))

            result_payload = ResultPayload(PACKAGE_NAME, **kwargs)

            splnk_utils = SplunkUtils(host=options.get("host"),
                                      port=options.get("port"),
                                      username=options.get("username"),
                                      password=options.get("splunkpassword"),
                                      verify=splunk_verify_cert)

            splunk_result = splnk_utils.update_notable(event_id=event_id,
                                                       comment=comment,
                                                       status=notable_event_status,
                                                       cafile=splunk_verify_cert)

            yield StatusMessage("Finished 'splunk_update_notable' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the return value
            yield FunctionResult(result_payload.done(True, splunk_result.get('content', {})))
        except Exception as e:
            log.error("Function execution throws exception: {}".format(str(e)))
            yield FunctionError()
