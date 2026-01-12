from typing import Dict, Union
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.util.model_helper import ModelHelper
from fn_watsonx_analyst.util.ModelTag import ModelTag
from fn_watsonx_analyst.util.rich_text import RichTextHelper
from fn_watsonx_analyst.types import AppState
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.logging_helper import create_logger, request_id_var

log = create_logger(__name__)


class ResponseHelper:
    """
    Convert watsonx responses to a function result AIResponsePurpose.
    **Warning**: Do not modify request context after instantiating this class, as the information will be stale.
    """

    request_id: str
    request_context: AppState

    def __init__(self):
        self.request_id = request_id_var.get() or ""
        self.request_context = app_state.get()

    def estimate_invocation_cost(
        self,
        model_id: str,
        input_tokens: int,
        output_tokens: int,
        embedding_tokens: int,
    ) -> float:
        input_cost, output_cost, embedding_cost = 0.0, 0.0, 0.0
        try:
            input_cost, output_cost, embedding_cost = ModelHelper().get_model_cost(
                model_id
            )
        except:
            log.warning("Model cost unavailable for %s", model_id)
        cost = 0.0
        if input_cost and output_cost:
            mil = 1_000_000
            cost += (embedding_tokens / mil) * embedding_cost
            cost += (input_tokens / mil) * input_cost
            cost += (output_tokens / mil) * output_cost
        return cost  # leave as zero if no cost information in config

    def error_response(self, error_text: str) -> AIResponse:
        model_id = self.request_context.model_id

        generation_tokens = (
            self.request_context.input_tokens + self.request_context.output_tokens
        )
        estimated_cost = self.estimate_invocation_cost(
            model_id,
            self.request_context.input_tokens,
            self.request_context.output_tokens,
            self.request_context.embedding_tokens,
        )

        response_tag = ModelTag(
            model_id,
            "",
            self.request_context.purpose,
            self.request_id,
            generation_tokens,
            self.request_context.embedding_tokens,
            estimated_cost,
        )

        return {
            "generated_text": error_text,
            "raw_output": error_text,
            "tag": str(response_tag),
            "metadata": {
                "model_id": model_id,
                "estimated_cost": estimated_cost,
                "input_tokens": self.request_context.input_tokens,
                "output_tokens": self.request_context.output_tokens,
                "stop_reason": "",
                "created_at": "",
            },
        }

    def text_generation_to_ai_response(
        self, text_generation: WatsonxTextGenerationResponse
    ) -> AIResponse:

        # Normal Watsonx response handling
        generation_result = text_generation["results"][0]
        model_id = text_generation["model_id"]

        generation_tokens = (
            self.request_context.input_tokens + self.request_context.output_tokens
        )

        estimated_cost = self.estimate_invocation_cost(
            model_id,
            self.request_context.input_tokens,
            self.request_context.output_tokens,
            self.request_context.embedding_tokens,
        )

        response_tag = ModelTag(
            model_id,
            text_generation["created_at"],
            self.request_context.purpose,
            self.request_id,
            generation_tokens,
            self.request_context.embedding_tokens,
            estimated_cost,
        )

        generated_text = generation_result["generated_text"]
        if self.request_context.opts.get("render_markdown", "true") in [
            "true",
            "True",
            True,
        ]:
            generated_text = RichTextHelper().toHTML(generated_text)

        return {
            "generated_text": generated_text,
            "raw_output": generation_result["generated_text"],
            "tag": str(response_tag),
            "metadata": {
                "model_id": model_id,
                "created_at": text_generation["created_at"],
                "estimated_cost": estimated_cost,
                "input_tokens": self.request_context.input_tokens,
                "output_tokens": self.request_context.output_tokens,
                "stop_reason": generation_result["stop_reason"],
            },
        }
