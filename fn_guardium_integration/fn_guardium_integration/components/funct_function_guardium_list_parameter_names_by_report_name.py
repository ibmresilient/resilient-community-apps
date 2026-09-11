# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_list_parameter_names_by_report_name"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_integration", {})
        self.opts_data = opts

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @function("function_guardium_list_parameter_names_by_report_name")
    def _function_guardium_list_parameter_names_by_report_name_function(self, event, *args, **kwargs):
        """Function: A Function to list required parameters by selected report name."""
        try:
            # Initializing the logger and Resilient Guardium Helper classes
            logger_object = logging.getLogger(__name__)

            resilient_object = ResilientRestService(self.opts_data, self.options, logger_object)
            grd_rest_object = GrdRestEndpoint(self.options, resilient_object.client_secret, resilient_object.unique_id,
                                              logger_object)
            # Get the function parameters:
            guardium_report = kwargs.get("guardium_report")  # text

            logger_object.info(u"guardium_report: %s", guardium_report)

            if not resilient_object.client_secret:
                raise ValueError(u"Guardium client secret not generated, please run `Generate Guardium Client Secret`")

            yield StatusMessage(u"Checking for report parameters")
            response_json = grd_rest_object.list_parameter_names_by_report_name(report_name=guardium_report)
            yield StatusMessage(u"Completed checking report parameters.")
            result_string = ""
            for k, v in response_json.items():
                result_string += u"<div><b>{}</b>: {}</div>".format(k, v)

            results = {
                "content": result_string
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as er_msg:
            yield FunctionError(er_msg)
