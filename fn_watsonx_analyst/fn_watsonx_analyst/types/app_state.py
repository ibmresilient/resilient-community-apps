from typing import Literal, Union

from resilient import SimpleClient

from fn_watsonx_analyst.config import load_model_config
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.logging_helper import create_logger

log = create_logger(__name__)

class AppState():
    """
    Overall state on a per-function request level.

    Used to persist model id, request purpose
    and to track token usage, for post-invocation analysis and cost tracking

    Can be used for dependency injection for opts, and res_client
    """
    model_id: str
    purpose: AiResponsePurpose

    input_tokens: int
    output_tokens: int
    embedding_tokens: int

    res_client: Union[SimpleClient, None]
    opts: dict

    def __init__(self):
        self.reset()

    data_config: Union[Literal["default"], str] = "default"

    def reset(self):
        """
        Reset values to zero values
        """
        self.model_id = None
        self.purpose = None

        self.input_tokens = 0
        self.output_tokens = 0
        self.embedding_tokens = 0

        self.res_client = None
        self.opts = None
        self.data_config = "default"

    def set_model(self, model_id: str):
        if model_id not in [model["name"] for model in load_model_config()]:
            log.warning("Model ID %s not supported", model_id)
        self.model_id = model_id

    def increment_input_tokens(self, input_tokens: int):
        self.input_tokens += input_tokens

    def increment_output_tokens(self, output_tokens: int):
        self.output_tokens += output_tokens

    def increment_embedding_tokens(self, embedding_tokens: int):
        self.embedding_tokens += embedding_tokens
