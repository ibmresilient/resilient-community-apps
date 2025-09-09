# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_text_generation"

log = create_logger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_text_generation'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Perform Text Generation against watsonx™. 
            Can replace '{}' in prompts with comma-separated strings in `fn_watsonx_analyst_arguments`.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_prompt
            -   fn_inputs.fn_watsonx_analyst_system_prompt
            -   fn_inputs.fn_watsonx_analyst_arguments
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_model_id_override
        """
        _ = generate_request_id()

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_state.get().reset()

        app_state.get().set_model(getattr(fn_inputs, "fn_watsonx_analyst_model_id", None))
        app_state.get().opts = self.opts
        app_state.get().res_client = self.rest_client()
        app_state.get().purpose = AiResponsePurpose.TEXT_GENERATION

        prompt = getattr(fn_inputs, "fn_watsonx_analyst_prompt", None)
        system_prompt = ""
        args = ""

        # optional parameters
        try:
            system_prompt = getattr(fn_inputs, "fn_watsonx_analyst_system_prompt", None)
            args = str(getattr(fn_inputs, "fn_watsonx_analyst_arguments", None))
        except:
            pass  # ignore as optional parameters not being found is fine

        text_prompt = "" + system_prompt + "\n\n" + prompt
        try:
            query_helper = QueryHelper()
            response = query_helper.text_generation(text_prompt, args)
            results = ResponseHelper().text_generation_to_ai_response(response)

            yield FunctionResult(results)
        # pylint: disable=broad-exception-caught
        except Exception as e:
            yield FunctionResult({"error": str(e)}, success=False, reason=str(e))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

