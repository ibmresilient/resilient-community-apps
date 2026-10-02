import pytest

from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.util.model_helper import ModelHelper
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.rich_text import RichTextHelper

from tests import helper

class TestResponseHelper:

    mock_inputs = [
        "mistralai/mistral-small-3-1-24b-instruct-2503",
        "meta-llama/llama-3-405b-instruct"
    ]

    @pytest.mark.parametrize("model", mock_inputs)
    def test_ai_response_to_function_result(self, model: str):
        helper.generate_app_state(model_id=model)
        genai_result: WatsonxTextGenerationResponse = helper.sample_output

        response = ResponseHelper().text_generation_to_ai_response(genai_result)

        assert response["raw_output"] == genai_result["results"][0]["generated_text"]
        assert response["generated_text"] == RichTextHelper().toHTML(genai_result["results"][0]["generated_text"])

    def test_error_response(self):
        error_message = "Error, something went wrong."
        response = ResponseHelper().error_response(error_message)

        assert response["generated_text"] == response["generated_text"]

    def test_cost_tracking(self):
        helper.generate_app_state()
        input_cost, output_cost, embedding_cost = ModelHelper().get_model_cost(app_state.get().model_id)

        cost = ResponseHelper().estimate_invocation_cost(
            app_state.get().model_id, 1_000_000, 1_000_000, 1_000_000
        )

        assert cost == input_cost + output_cost + embedding_cost

    def test_opt_in_for_rich_text(self):
        helper.generate_app_state()
        app_state.get().opts = {
            "render_markdown": True
        }

        assert ResponseHelper().text_generation_to_ai_response(helper.sample_output)["generated_text"] == RichTextHelper().toHTML(helper.sample_output["results"][0]["generated_text"])

    def test_not_explicit_rich_text(self):
        helper.generate_app_state()

        assert ResponseHelper().text_generation_to_ai_response(helper.sample_output)["generated_text"] == RichTextHelper().toHTML(helper.sample_output["results"][0]["generated_text"])

    def test_opt_out_of_rich_text(self):
        helper.generate_app_state()
        app_state.get().opts = {
            "render_markdown": False
        }

        assert ResponseHelper().text_generation_to_ai_response(helper.sample_output)["generated_text"] == helper.sample_output["results"][0]["generated_text"]
