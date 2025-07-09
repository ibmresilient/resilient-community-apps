from typing import Literal
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.QueryHelper import QueryHelper

from resilient import SimpleClient

from fn_watsonx_analyst.util.parallel.parallel import ParallelRunnable
from fn_watsonx_analyst.util.util import create_logger

log = create_logger(__name__)

class GenericSummarizer(ParallelRunnable):

    valid: bool = True

    model_id: str
    opts: dict

    typ: Literal["incident", "playbook_executions", "artifacts", "notes"]
    instruction: str
    purpose: AiResponsePurpose = None

    res_client: SimpleClient

    def __init__(
        self,
        typ: Literal[
            "aggregate", "incident", "playbook_executions", "artifacts", "notes", "contents"
        ],
        instruction: str,
        model_id: str,
        res_client: SimpleClient,
        opts: dict,
        purpose: AiResponsePurpose
    ):
        self.typ = typ
        self.instruction = instruction
        self.model_id = model_id
        self.res_client = res_client
        self.opts = opts
        self.purpose = purpose

    def run(self) -> AIResponse:
        if not self.valid:
            return (self.typ, {}, self.valid)
        query_helper = QueryHelper(self.res_client, self.model_id, self.opts)
        try:
            return query_helper.text_generation(self.instruction, purpose=self.purpose)
        except Exception as e:
            import traceback

            log.error(traceback.format_exc())
            log.error(f"Error summarizing... {e}")
            raise e

    def is_Valid(self):
        return self.valid
