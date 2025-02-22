#
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
import fn_qradar_integration.util.function_utils as function_utils

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_find_reference_set_item"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts)

    @function("qradar_find_reference_set_item")
    def _qradar_find_reference_set_item_function(self, event, *args, **kwargs):
        """Function: Find an item from a given QRadar reference set"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage(f"Starting 'qradar_find_reference_set_item' that was running in workflow '{wf_instance_id}'")

            validate_fields(["qradar_reference_set_name", "qradar_reference_set_item_value"], kwargs)
            # Get the function parameters:
            qradar_reference_set_name = kwargs.get("qradar_reference_set_name")  # text
            qradar_reference_set_item_value = kwargs.get("qradar_reference_set_item_value")  # text
            qradar_label = kwargs.get("qradar_label")  # text

            LOG.info(f"qradar_reference_set_name: {qradar_reference_set_name}")
            LOG.info(f"qradar_reference_set_item_value: {qradar_reference_set_item_value}")
            LOG.info(f"qradar_label: {qradar_label}")

            options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
            qradar_verify_cert = False if options.get("verify_cert", "false").lower() == "false" else options.get("verify_cert")

            LOG.debug("Connection to {} using {}".format(options.get("host"),
                                                         options.get("username") or "service token"))

            qradar_client = QRadarClient(host=options.get("host"),
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            results= qradar_client.search_ref_set(qradar_reference_set_name,
                                                  qradar_reference_set_item_value)

            yield StatusMessage(f"Finished 'qradar_find_reference_set_item' that was running in workflow '{wf_instance_id}'")

            results["inputs"] = {
                "qradar_reference_set_name": qradar_reference_set_name,
                "qradar_reference_set_item_value": qradar_reference_set_item_value,
                "qradar_label": qradar_label
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            LOG.error(str(e))
            yield FunctionError()
