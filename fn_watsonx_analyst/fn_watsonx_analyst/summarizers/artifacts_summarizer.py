import json
from typing import List

from resilient import SimpleClient

from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from .generic_summarizer import GenericSummarizer


class ArtifactsSummarizer(GenericSummarizer):
    """Summarizes multiple artifacts"""

    inc_data: Incident

    instruction = ""
    name = "artifacts"

    def __init__(
        self,
        art_data: List[Artifact],
        model_id: str,
        res_client: SimpleClient,
        opts: dict,
    ):
        if len(art_data) <= 0:
            self.valid = False
        self.instruction = ContextHelper().get_prompt(
            Templates.SUMM_ARTIFACT, data=json.dumps(art_data, indent=2)
        )

        super().__init__("artifacts", self.instruction, model_id, res_client, opts)
