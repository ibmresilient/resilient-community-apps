import json
from resilient import SimpleClient

from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from .generic_summarizer import GenericSummarizer


class ArtifactSummarizer(GenericSummarizer):
    inc_data: Incident

    instruction = ""
    contents_summary = False
    name = "artifacts"

    def __init__(
        self,
        res_client: SimpleClient,
        inc_id: int,
        artifact: Artifact,
        model_id: str,
        opts: dict,
    ):
        self.name = artifact["value"]
        if artifact["attachment"] is not None:
            self.contents_summary = True

        if self.contents_summary:
            art_contents = RestHelper().do_request(
                res_client,
                RestUrls.ARTIFACT_CONTENTS,
                inc_id=inc_id,
                art_id=artifact["id"],
            )
            self.instruction = ContextHelper().get_prompt(
                Templates.ASSESS_SCRIPT,
                name=self.name,
                description=artifact["description"],
                content_type=artifact["attachment"]["content_type"],
                content=art_contents,
            )

        if not self.contents_summary:
            self.instruction = ContextHelper().get_prompt(
                Templates.ASSESS_META_ARTIFACT, data=json.dumps(artifact, indent=2)
            )

        super().__init__("artifacts", self.instruction, model_id, res_client, opts)
