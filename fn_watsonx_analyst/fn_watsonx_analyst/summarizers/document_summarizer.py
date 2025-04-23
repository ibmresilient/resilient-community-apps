from resilient import SimpleClient

from fn_watsonx_analyst.summarizers.generic_summarizer import GenericSummarizer
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose


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
        super().__init__(self.name, self.instruction, model_id, res_client, opts, AiResponsePurpose.ARTIFACT_SUMMARY)
