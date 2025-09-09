from typing import Union
from datetime import datetime
from enum import Enum

import pkg_resources

class AiResponsePurpose(Enum):
    ARTIFACT_SUMMARY = "Artifact Summary"
    NOTE_CONVERSATION = "Note Conversation"
    ARTIFACT_CONVERSATION = "Artifact Conversation"
    ARITFACT_META_SUMMARY= "Artifact Metadata Summary"
    INCIDENT_SUMMARY = "Incident Summary"
    TEXT_GENERATION = "Text Generation"

    def __eq__(self, other):
        return self.value == other.value


class ModelTag:

    model_id: str
    created_at: str
    purpose: AiResponsePurpose
    request_id: str
    app_version: str = pkg_resources.require("fn_watsonx_analyst")[0].version
    input_tokens: int
    output_tokens: int
    embedding_tokens: int
    estimated_cost: Union[float, str]

    UNKNOWN = "Unknown"

    def __init__(
        self,
        model_id: str,
        created_at: str,
        purpose: AiResponsePurpose,
        request_id: str,
        generation_tokens: int,
        embedding_tokens: int,
        estimated_cost: float,
    ):
        self.model_id = model_id
        if not model_id:
            self.model_id = self.UNKNOWN

        self.purpose = purpose
        if not self.purpose:
            self.purpose = AiResponsePurpose.NOTE_CONVERSATION # fallback default
        

        self.request_id = request_id
        if not self.request_id:
            self.request_id = self.UNKNOWN

        try:
            self.created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ').strftime("%H:%M %B %d, %Y")
        except:
            # fallback to now if time format changes
            self.created_at = datetime.now().strftime("%H:%M %B %d, %Y")
        self.generation_tokens = generation_tokens
        self.embedding_tokens = embedding_tokens

        if estimated_cost > 0.0:
            self.estimated_cost = round(estimated_cost * 100, 6) # dollar to cents
        else:
            self.estimated_cost = self.UNKNOWN

    def _get_name(self) -> str:
        return f"watsonx.ai for SOAR Analysts v{self.app_version}"

    def __repr__(self) -> str:
        return f"""<div style="white-space: nowrap; display: table-row; height:48px; border: 1px solid #4589ff;">
<span style="display: table-cell; text-align: center; vertical-align: middle; width: 48px; font-size: 12px; border: 1px solid #fff;user-select: none;"title="AI-Generated Content"><span style="user-select: none;">AI</span></span>
<small style="font-size: 12px;"><span style="display: table-cell; font-size: 12px; padding-left: 1em;"><span style="color: lightgrey;">GenAI Contribution by {self._get_name()} for {self.purpose.value}</span><br><span>Using {self.model_id} at {self.created_at}. Request ID: <span style="font-family: monospace;">{self.request_id}</span></span><br><span style="color: lightgrey;"><span title="Input and output tokens used to generate text.">Generation tokens: <span style="font-family: monospace">{self.generation_tokens}</span></span>, <span title="Tokens used for embedding reference data.">Embedding tokens: <span style="font-family: monospace">{self.embedding_tokens}</span></span>. <span title="Estimated cost in US Dollar cents of generation and embedding tokens used for this request.">Estimated cost: <span style="font-family: monosace">{self.estimated_cost}</span> USD cents</span>. <a href="https://www.ibm.com/products/watsonx-ai/pricing">Learn more</a>.</small></div>
"""
