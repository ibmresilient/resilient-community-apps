import os
from typing import List, TypedDict
from functools import cache

import yaml

from fn_watsonx_analyst.util.logging_helper import create_logger

log = create_logger(__name__)


class ModelConfig(TypedDict):
    name: str

    context_length: int
    max_output_tokens: int

    input_cost: float
    output_cost: float


class GroundingPrompts(TypedDict):
    incident: str
    artifact: str
    attachment: str
    task: str


class UserPrompts(TypedDict):
    contents_summary: str
    metadata_summary: str


class SystemPrompts(UserPrompts, TypedDict):
    default_prompt: str
    artifact_qna: str


class PromptDict(TypedDict):
    prompt_grounding: GroundingPrompts
    system_prompts: SystemPrompts
    user_prompts: UserPrompts


class LanguagePromptDict(TypedDict):
    en: PromptDict
    fr: PromptDict
    de: PromptDict
    es: PromptDict
    pt: PromptDict


@cache
def load_summarization_config() -> dict:
    """
    Load the configuration for incident summaries.

    Contains the prompt, and metadata for summarizing an incident.
    """
    config_path = os.path.join(
        os.path.dirname("fn_watsonx_analyst/config/"), "summarization_config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


@cache
def load_prompt_config() -> LanguagePromptDict:
    """
    Load the LLM prompts from the config yaml.

    Each supported ISO language code gets its own object.
    """
    config_path = os.path.join(
        os.path.dirname("fn_watsonx_analyst/config/"), "prompts.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@cache
def load_model_config() -> List[ModelConfig]:
    """
    Load LLM model config.

    Contains the model id, context length, max output tokens, and cost
        information for each supported model.
    """
    model_config_path = os.path.abspath(
        os.path.join(
            os.path.dirname("fn_watsonx_analyst/config/"), "models.yaml")
    )
    with open(model_config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@cache
def load_data_config(data_config_name: str) -> dict:
    """
    Load the data payload config yaml.

    To be used to select what data gets reserved in ContextHelper
    """
    if data_config_name == "default":
        path = os.path.abspath(
            os.path.join(
                os.path.dirname("fn_watsonx_analyst/config/"), "datapayload.yaml"
            )
        )
    else:
        path = os.path.join(
            "/var/rescircuits/", data_config_name + ".yaml"
        )

    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        log.exception(f"Failed to load data payload config from file: {path}.\nException: {e}")
        raise e
