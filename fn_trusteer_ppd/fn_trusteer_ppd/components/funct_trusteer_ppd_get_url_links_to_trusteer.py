# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.3934
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_trusteer_ppd.lib.trusteer_ppd_client import TrusteerPPDClient, PACKAGE_NAME
from fn_trusteer_ppd.lib.configure_tab import init_trusteer_ppd_tab

FN_NAME = "trusteer_ppd_get_url_links_to_trusteer"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'trusteer_ppd_get_url_links_to_trusteer'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        # Initialize the Trusteer tab
        init_trusteer_ppd_tab()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Return the URL links to the Trusteer PUID and the devices.
        Inputs:
            -   fn_inputs.trusteer_ppd_puid
            -   fn_inputs.trusteer_ppd_device_id
        """
        trusteer_client = TrusteerPPDClient(self.rc, self.PACKAGE_NAME, self.options)

        link_url_puid = None
        link_url_device_id = None

        trusteer_ppd_puid = getattr(fn_inputs, "trusteer_ppd_puid", None)
        trusteer_ppd_device_id = getattr(fn_inputs, "trusteer_ppd_device_id", None)
        
        # Get the URL link back to Trusteer PUID.
        if trusteer_ppd_puid:
            link_url_puid = trusteer_client.make_linkback_url(id=trusteer_ppd_puid, id_type='puid')

        # Get the link back to the Device in the Trusteer session.
        if trusteer_ppd_device_id:
            link_url_device_id = trusteer_client.make_linkback_url(id=trusteer_ppd_device_id, 
                                                                   id_type='device_id')

        results = {"link_url_puid": link_url_puid,
                   "link_url_device_id": link_url_device_id}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
