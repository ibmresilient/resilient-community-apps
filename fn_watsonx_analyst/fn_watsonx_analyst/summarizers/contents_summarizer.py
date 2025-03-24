from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from .generic_summarizer import GenericSummarizer

from resilient import SimpleClient


class ContentsSummarizer(GenericSummarizer):
    instruction = ""
    name = "contents"

    MAX_NEW_TOKENS = 350

    def __init__(
        self,
        data: bytes,
        content_type: str,
        model_id: str,
        res_client: SimpleClient,
        opts: dict,
    ):
        self.instruction = ContextHelper().get_prompt(
            Templates.SUMM_CONTENTS, data=data, content_type=content_type
        )
        super().__init__(self.name, self.instruction, model_id, res_client, opts)
