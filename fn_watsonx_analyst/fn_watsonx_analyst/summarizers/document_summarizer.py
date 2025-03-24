from asyncio import Queue
import json
from typing import List
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from .generic_summarizer import GenericSummarizer

from resilient import SimpleClient


class DocumentSummarizer(GenericSummarizer):
    instruction = ""
    name = "document"

    def __init__(
        self,
        data: str,
        content_type: str,
        model_id: str,
        res_client: SimpleClient,
        opts: dict,
    ):
        self.instruction = ContextHelper().get_prompt(
            Templates.SUMM_DOCUMENT, data=data, content_type=content_type
        )
        self.MAX_NEW_TOKENS = 200
        super().__init__(self.name, self.instruction, model_id, res_client, opts)
