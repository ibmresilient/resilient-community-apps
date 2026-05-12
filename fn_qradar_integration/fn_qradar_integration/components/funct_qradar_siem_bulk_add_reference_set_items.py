# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
import fn_qradar_integration.util.function_utils as function_utils

FN_NAME = "qradar_siem_bulk_add_reference_set_items"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'qradar_siem_bulk_add_reference_set_items'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = function_utils.get_servers_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add or update data in a reference set.
        Inputs:
            -   fn_inputs.qradar_domain_id
            -   fn_inputs.qradar_namespace
            -   fn_inputs.qradar_label
            -   fn_inputs.qradar_reference_set_values
            -   fn_inputs.qradar_reference_set_name
        """
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            # Validate required fields
            validate_fields(["qradar_namespace", "qradar_reference_set_name", "qradar_domain_id", "qradar_reference_set_values"], fn_inputs)

            # Get qradar_label if one is given
            qradar_label = fn_inputs.qradar_label if getattr(fn_inputs, "qradar_label", None) else None
            self.LOG.info("qradar_label: %s", qradar_label)

            # Test to see if given label exists then return server_options for the server with that label
            server_options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
            qradar_verify_cert = False if server_options.get("verify_cert", "false").lower() == "false" else server_options.get("verify_cert")

            self.LOG.debug("Connecting to QRadar instance @ %s", server_options.get('host'))

            # Create connection to QRadar server
            qradar_client = QRadarClient(host=server_options.get("host"),
                                        username=server_options.get("username", None),
                                        password=server_options.get("qradarpassword", None),
                                        token=server_options.get("qradartoken", None),
                                        cafile=qradar_verify_cert,
                                        opts=self.opts,
                                        function_opts=server_options)

            ref_set_values_list = fn_inputs.qradar_reference_set_values.replace(", ", ",").split(",")
            # Make call to bulk load values into a reference set
            results = qradar_client.bulk_load_ref_set_values(namespace=getattr(fn_inputs, "qradar_namespace", None),
                                                             name=getattr(fn_inputs, "qradar_reference_set_name", None),
                                                             domain_id=getattr(fn_inputs, "qradar_domain_id", None),
                                                             values=ref_set_values_list)

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
