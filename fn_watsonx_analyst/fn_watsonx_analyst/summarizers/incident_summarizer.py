from asyncio import Queue
import json
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from .generic_summarizer import GenericSummarizer

from resilient import SimpleClient


class IncidentSummarizer(GenericSummarizer):
    instruction = ""
    name = "incident"

    def __init__(
        self, inc_data: Incident, model_id: str, res_client: SimpleClient, opts: dict
    ):
        self.instruction = ContextHelper().get_prompt(
            Templates.SUMM_INCIDENT, data=json.dumps(inc_data, indent=2)
        )
        super().__init__("incident", self.instruction, model_id, res_client, opts)
