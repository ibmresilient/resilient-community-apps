# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields
from resilient_circuits import FunctionResult, AppFunctionComponent, app_function

FN_NAME = "mcafee_epo_find_a_system"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'mcafee_epo_find_a_system''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Find ePO systems based on property such as system name, tag, IP address, MAC address, etc.
           Return: List of systems found and information about the systems"""

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get the function parameters:
        validate_fields(["mcafee_epo_systems"], fn_inputs)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        def response(systems):
            return client.request(
                "system.find",
                {"searchText": systems.strip().replace(",","")}
            )

        if ',' in fn_inputs.mcafee_epo_systems:
            results = []
            systems = fn_inputs.mcafee_epo_systems.split()
            for system in systems:
                results.append(response(system)[0])
        else:
            results = response(fn_inputs.mcafee_epo_systems)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
