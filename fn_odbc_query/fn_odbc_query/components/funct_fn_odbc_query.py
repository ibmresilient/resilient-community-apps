# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_odbc_query.util import function_utils, odbc_utils

PACKAGE_NAME = "fn_odbc_query"
FN_NAME = "fn_odbc_query"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_odbc_query'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        validate_fields([], self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that runs ODBC queries. Parameters are passed to the database separately, protecting against SQL injection attacks.
        Inputs:
        sql_query: a SQL query with set parameters using a question mark as a place holder, SQL statements SELECT, INSERT, UPDATE and DELETE are supported
        sql_condition_value1: value for the question mark - condition value 1
        sql_condition_value2: value for the question mark - condition value 2
        sql_condition_value3: value for the question mark - condition value 3
        Inputs:
            -   fn_inputs.sql_query
            -   fn_inputs.sql_condition_value3
            -   fn_inputs.sql_condition_value1
            -   fn_inputs.sql_condition_value2
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate function parameters
        validate_fields(["sql_query"], fn_inputs)

        # Get the function parameters:
        sql_query = fn_inputs.sql_query
        sql_condition_value1 = getattr(fn_inputs, "sql_condition_value1", None)
        sql_condition_value2 = getattr(fn_inputs, "sql_condition_value2", None)
        sql_condition_value3 = getattr(fn_inputs, "sql_condition_value3", None)

        # Log parameers
        self.LOG.info(str(fn_inputs))

        sql_params = function_utils.prepare_sql_parameters(sql_condition_value1, sql_condition_value2,
                                                               sql_condition_value3)

        # Validate


        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

        # Example accessing optional attribute in fn_inputs and initializing it to None if it does not exist (this is similar for app_configs)
        # optional_input =  getattr(fn_inputs, "optional_input", None)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Call API implementation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()
        #
        # yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        #
        # yield FunctionResult(results)
        ##############################################

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
