# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v50.0.108

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_mandiant.lib.mandiant_client import MandiantClient


PACKAGE_NAME = "fn_mandiant"
FN_NAME = "mandiant_threat_intelligence"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mandiant_threat_intelligence'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        # The app client is created and authenticated once on installation.
        # This prevents the app from authenticating with the endpoint on
        # every function invocation.
        self.client = MandiantClient(self.rc, self.options)
        self.client.authenticate()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Provides customers with intelligence on who is most likely going to attack them,
            how they are going to attack, and what tools they will use. This allows customers to
            prepare their defenses against an imminent attack.
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields([
            "mandiant_artifact_type",
            "mandiant_artifact_data"
        ], fn_inputs)

        # Get artifact type and data. Supported type:
        artifact_type  = getattr(fn_inputs, "mandiant_artifact_type").lower() # text
        artifact_data  = getattr(fn_inputs, "mandiant_artifact_data") # text

        # Checks if the application is authenticated and if the acquired ACCESS_TOKEN has not expired.
        # Otherwise simply reauthenticates with the endpoint.
        if not self.client.check_authenticated():
            self.LOG("Reauthenticate application with endpoint")
            self.client.authenticate()

        # Searching for artifact related information
        search_results = self.client.search_artifact(
            artifact_data=artifact_data,
            artifact_type=artifact_type
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
        yield FunctionResult(search_results)
        # yield FunctionResult({}, success=False, reason="Bad call")

