from datetime import datetime
from enum import Enum

import pkg_resources

from fn_watsonx_analyst.util.util import request_id_var


class AiResponsePurpose(Enum):
    ARTIFACT_SUMMARY = "Artifact Summary"
    NOTE_CONVERSATION = "Note Conversation"
    ARTIFACT_CONVERSATION = "Artifact Conversation"

    def __eq__(self, other):
        return self.value == other.value


class ModelTag:
    model_id: str
    created_at: str
    purpose: AiResponsePurpose
    request_id: str
    app_version: str = pkg_resources.require("fn_watsonx_analyst")[0].version

    margin = "------------------------------------------------------------------------"

    def __init__(
        self,
        model_id: str,
        purpose: AiResponsePurpose = AiResponsePurpose.ARTIFACT_SUMMARY,
    ):
        self.model_id = model_id
        self.created_at = datetime.now().strftime("%H:%M %B %d, %Y")
        self.purpose = purpose
        self.request_id = request_id_var.get()

    def _get_name(self) -> str:
        return f"watsonx.ai for SOAR Analysts v{self.app_version}"

    def __repr__(self) -> str:
        return f"""<div style="white-space: nowrap; display: table-row; height:32px; border: 1px solid #4589ff;">
<span style="display: table-cell; text-align: center; vertical-align: middle; width: 32px; font-size: 12px; border: 1px solid #fff;user-select: none;" title="AI-Generated Content"><span style="user-select: none;">AI</span></span>
<small style="font-size: 12px;"><span style="display: table-cell; font-size: 12px; padding-left: 1em;"><span style="color: lightgrey;">GenAI Contribution by {self._get_name()} for {self.purpose.value}</span><br><span>Using {self.model_id} at {self.created_at}. Request ID: <span style="font-family: monospace;">{self.request_id}</span></span></small></div></div>
"""
