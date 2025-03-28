import json

from resilient import SimpleClient

from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates

from .generic_summarizer import GenericSummarizer


class ArtifactDetailsSummarizer(GenericSummarizer):
    """Summarizes artifact JSON metadata"""

    inc_data: Incident

    instruction = ""
    name = "artifacts"

    def __init__(
        self, res_client: SimpleClient, artifact: Artifact, model_id: str, opts: dict
    ):
        self.name = artifact["value"]

        (_, _, data, _) = ContextHelper().cleanse_data(None, [], [artifact], [])

        self.instruction = ContextHelper().get_prompt(
            Templates.ASSESS_META_ARTIFACT, data=json.dumps(data, indent=2)
        )
        # self.instruction += json_str
        super().__init__("artifacts", self.instruction, model_id, res_client, opts)
