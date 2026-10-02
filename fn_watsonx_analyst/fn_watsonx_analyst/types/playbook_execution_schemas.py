from typing import ClassVar, List

from pydantic import BaseModel, ConfigDict, Field

from ibm_watsonx_ai.foundation_models.schema import (
    TextChatResponseFormat, TextChatResponseFormatType, TextChatResponseJsonSchema)

from fn_watsonx_analyst.types.playbook import PlaybookActivationType
from fn_watsonx_analyst.util.watsonx_client import StructuredOutputBase

class ExecutionPhase(BaseModel):
    model_config = ConfigDict(extra="ignore")

    phase_name: str
    is_complete: bool
    notes: List[str]
    conditions: List[str]


class PlaybookAnalysis(StructuredOutputBase):
    """Fields are declared in generation order. Executive summary MUST be last."""
    model_config = ConfigDict(extra="ignore")

    SAMPLE_DATA: ClassVar[dict] = {
        "activation_summary": "Lorem ipsum",
        "execution_phases": [
            {"phase_name": "Lorem", "is_complete": True, "notes": ["note 1", "note 2"], "conditions": ["condition 1"]}
        ],
        "recommendations": "Lorem ipsum",
        "executive_summary": "Lorem ipsum"
    }

    activation_summary: str
    execution_phases: List[ExecutionPhase]
    recommendations: str
    executive_summary: str

class PlaybookContext(BaseModel):
    playbook_name: str
    playbook_description: str
    status: str

    activated_by_name: str
    activation_type: PlaybookActivationType
    activation_conditions_str: str

    activities_str: str
    outstanding_tasks: str

    incident_ref: str
    incident_types: str

    target_type: str
    target_object: str
    start_time: str
    end_time: str
    duration: str

    mermaid_diagram: str
    scripts_info: str

class PlaybookExecutionSummaryData(PlaybookContext):
    """Wraps deterministic platform data with LLM-generated analysis."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    analysis: PlaybookAnalysis = Field(description="AI-generated structured breakdown")

def get_playbook_analysis_schema() -> TextChatResponseFormat:
    """Returns schema optimized for IBM watsonx AI JSON mode."""
    return TextChatResponseFormat(
        TextChatResponseFormatType.JSON_SCHEMA, TextChatResponseJsonSchema(
            name="Playbook analysis", schema=PlaybookAnalysis.model_json_schema()))
