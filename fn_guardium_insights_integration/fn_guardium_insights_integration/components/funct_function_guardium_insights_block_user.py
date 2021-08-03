# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload

from fn_guardium_insights_integration.lib.insights_services import InsightsServices


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_insights_block_user"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_insights_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_insights_integration", {})

    @function("function_guardium_insights_block_user")
    def _function_guardium_insights_block_user_function(self, event, *args, **kwargs):
        """Function: A Function to Block User From Guardium Insights."""
        try:
            # Get the function parameters:
            input_field_guardium_insights_config_id = kwargs.get("input_field_guardium_insights_config_id")  # text
            input_field_guardium_insights_guardium_id = kwargs.get("input_field_guardium_insights_guardium_id")  # text
            input_field_guardium_insights_who = kwargs.get("input_field_guardium_insights_who")  # text
            input_field_guardium_insights_what = kwargs.get("input_field_guardium_insights_what")  # text

            log = logging.getLogger(__name__)
            log.info("Guardium Insights Config ID: %s", input_field_guardium_insights_config_id)
            log.info("Guardium Insights Guardium ID: %s", input_field_guardium_insights_guardium_id)
            log.info("Guardium Insights Who: %s", input_field_guardium_insights_who)
            log.info("Guardium Insights What: %s", input_field_guardium_insights_what)
            yield StatusMessage("Blocking user action for: {} initiated...".format(input_field_guardium_insights_who))

            # Initializing the GI service class
            gi_service = InsightsServices(self.options, log)

            what_info = json.loads(input_field_guardium_insights_what)

            # Initializing the result payload
            _inputs = {"guardium_id": input_field_guardium_insights_guardium_id,
                       "config_id": input_field_guardium_insights_config_id,
                       "database_user/actor/who": input_field_guardium_insights_who,
                       "what": what_info}
            res_payload = ResultPayload("fn_guardium_insights_integration", **_inputs)

            _db_name = what_info.get("database_name")
            _db_port = what_info.get("server_port")

            _db_ip = ""
            if what_info.get("sever_hostname", None):
                _db_ip = what_info.get("sever_hostname")
            else:
                _db_ip = what_info.get("server_ip")

            _payload = {"destination": {"config_id": input_field_guardium_insights_config_id,
                                        "guardium_id": input_field_guardium_insights_guardium_id},
                        "details": {"bdbname": _db_name, "bip": _db_ip, "bport": _db_port,
                                    "buser": input_field_guardium_insights_who}}
            # Calling GI block user API.
            response = gi_service.block_user(_payload)
            function_res = res_payload.done(success=True, content=response)

            yield StatusMessage("Blocking user action for: {} completed...".format(input_field_guardium_insights_who))
            # Produce a FunctionResult with the results
            yield FunctionResult(function_res)
        except Exception as funct_msg:
            yield FunctionError(funct_msg)
