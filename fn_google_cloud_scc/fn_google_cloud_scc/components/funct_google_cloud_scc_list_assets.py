# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import pprint

from fn_google_cloud_scc.lib.scc_common import PACKAGE_NAME, GoogleSCCCommon
from fn_google_cloud_scc.poller.soar_common import SOARCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "google_cloud_scc_list_assets"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'google_cloud_scc_list_assets'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: List the assets of a Google Cloud organization that is being monitored in SCC.
        Inputs:
            -   fn_inputs.google_scc_filter
            -   fn_inputs.google_scc_field_mask
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        self.app_common = GoogleSCCCommon(self.options, self.rc)
        self.soar_common = SOARCommon(self.rest_client())

        assets_filter = getattr(fn_inputs, "google_scc_filter", None)
        field_mask = getattr(fn_inputs, "google_scc_field_mask", None)

        # capture poorly given filter or field-mask errors
        # and fail the function
        # other errors should be thrown as normal and handled on the platform
        # as the workflow designer wants
        try:
            assets = self.app_common.list_assets(filter=assets_filter, fields_to_return=field_mask)

            results = {
                "assets_formatted": self.app_common.format_assets(assets),
                "assets_raw": assets
            }
            success = True
            reason = None
        except IntegrationError as e:
            # list_assets only throws an IntegrationError when filter or field mask is incorrect
            results = {}
            success = False
            reason = e.value

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=success, reason=reason)

