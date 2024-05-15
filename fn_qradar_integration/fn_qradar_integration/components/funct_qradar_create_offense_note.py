# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
from fn_qradar_integration.util import function_utils

PACKAGE_NAME = "fn_qradar_integration"
FN_NAME = "qradar_create_offense_note"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'qradar_create_offense_note'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.servers_list = function_utils.get_servers_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.qradar_id
            -   fn_inputs.qradar_label
            -   fn_inputs.qradar_siem_note
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["qradar_id", "qradar_siem_note"], fn_inputs)

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        qradar_label = fn_inputs.qradar_label
        self.LOG.info("qradar_label: %s", qradar_label)

        # Test to see if given label exists then return server_options for the server with that label
        server_options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
        qradar_verify_cert = False if server_options.get("verify_cert", "false").lower() == "false" else server_options.get("verify_cert")

        self.LOG.debug("Connecting to QRadar instance @ %s", server_options.get('host'))

        qradar_client = QRadarClient(host=server_options.get("host"),
                                     username=server_options.get("username", None),
                                     password=server_options.get("qradarpassword", None),
                                     token=server_options.get("qradartoken", None),
                                     cafile=qradar_verify_cert,
                                     opts=self.opts,
                                     function_opts=server_options)

        results = qradar_client.create_offense_note(fn_inputs.qradar_id, fn_inputs.qradar_siem_note)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=bool(results))
