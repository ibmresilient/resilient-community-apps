# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""
import re
from io import BytesIO

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import write_file_attachment
from fn_extrahop.lib.rx_client import RxClient
from fn_extrahop.lib.app_common import set_params

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_search_packets"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_search_packets'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Search for and download packets stored on the ExtraHop Reveal(x) system.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.extrahop_bpf
            -   fn_inputs.extrahop_ip2
            -   fn_inputs.extrahop_active_until
            -   fn_inputs.extrahop_port1
            -   fn_inputs.extrahop_output
            -   fn_inputs.extrahop_always_return_body
            -   fn_inputs.extrahop_active_from
            -   fn_inputs.extrahop_port2
            -   fn_inputs.extrahop_limit_search_duration
            -   fn_inputs.extrahop_limit_bytes
            -   fn_inputs.extrahop_ip1
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)
        self.LOG.info("fn_inputs: %s", fn_inputs)

        # Set params dict:
        params = {}
        params = set_params(fn_inputs, params, "extrahop_")

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.search_packets(**params)
        filename = None
        if response.status_code == 204:
            result = {"status": "No search matches found."}
        elif response.status_code == 200:
            cd_headers = response.headers.get("Content-Disposition")
            if cd_headers:
                filename = re.findall("filename=(.+)", cd_headers)[0].strip('"')
            if filename:
                datastream = BytesIO(response.content)
                write_file_attachment(self.rest_client(), filename, datastream, fn_inputs.incident_id,
                                      task_id=None, content_type=None)
                result = {"attachment": filename}
            else:
                self.LOG.error("File name not found in 'Content-Disposition' response headers.")

                result = {"error": "Missing response header"}

        # Return filename in result
        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
