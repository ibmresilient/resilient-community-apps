from typing import Union

from .generic_summarizer import GenericSummarizer

from resilient import SimpleClient

from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.prompting import Prompting

class ContentsSummarizer(GenericSummarizer):
    instruction = ""
    name = "contents"

    MAX_NEW_TOKENS = 350

    def __init__(
        self,
        data: Union[str, bytes],
        content_type: str,
        model_id: str,
        res_client: SimpleClient,
        opts: dict,
    ):
        self.instruction = Prompting(opts).build_prompt(
            AiResponsePurpose.ARTIFACT_SUMMARY, model_id,
            None, data, None, [], False, content_type=content_type)

        super().__init__(self.name, self.instruction, model_id, res_client, opts, AiResponsePurpose.ARTIFACT_SUMMARY)
