from typing import List, Type
import pytest
from unittest.mock import MagicMock

from fn_watsonx_analyst.types.playbook_execution_schemas import PlaybookAnalysis
from fn_watsonx_analyst.types.watsonx_responses import WatsonxChatResponse
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.watsonx_client import StructuredOutputBase

class MockAPIClient:

    foundation_models = MagicMock()

    def __init__(self, credentials):
        self.credentials = credentials
    
    def set(self, *args, **kwargs):
        """Mock the set method that watsonx APIClient uses"""
        pass

class MockModelInference:
    sample_output: str = None

    def __init__(self, model_id: str, api_client: object, params: object, project_id: str, response_format: Type[StructuredOutputBase] = None):
        if response_format:
            self.sample_output = response_format.sample().model_dump_json()

    def chat(self, messages: list[dict[str, str]]) -> WatsonxChatResponse:

        msg = "Lorem ipsum"

        if app_state.get().purpose == AiResponsePurpose.ARTIFACT_CONVERSATION:
            msg = "Artifact conversation"
        
        if self.sample_output:
            msg = self.sample_output

        return {
            "id": "asdf",
            "object": "asdf",

            "model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
            "model": "mistralai/mistral-small-3-1-24b-instruct-2503",

            "choices" : [
                {
                    "finish_reason" : "stop",
                    "index": 0,
                    "message": {
                        "content" : msg,
                        "role" : "assistant"
                    }
                }
            ],

            "created": 1234567890,
            "created_at": "123456789",

            "usage": {
                "prompt_tokens": 200,
                "completion_tokens": 1000
            },
            "system": {},
        }

class MockEmbeddings:
    def __init__(self, **kwargs):
        pass
    def embed_documents(self, texts: List[str], use_local: bool | None = None) -> List[list]:
        return [[-1, 2, 3]]
    def generate(self, inputs: List[str]) -> dict:
        return {
            "results": [
                {"embedding": [-1, 2, 3]},
                {"embedding": [-1, 2, 3]},
            ],
            "input_token_count": 7
        }


@pytest.fixture(autouse=True, scope="session")
def global_watsonx_client_mock():
    # MockAPI = MagicMock(name="MockAPIClient")
    MockCreds = MagicMock(name="MockCredentials")
    # MockEmbeddings = MagicMock(name="MockEmbeddings")


    with pytest.MonkeyPatch().context() as mp:
        mp.setattr("fn_watsonx_analyst.util.watsonx_client.APIClient", MockAPIClient)
        mp.setattr("fn_watsonx_analyst.util.watsonx_client.Credentials", MockCreds)
        mp.setattr("fn_watsonx_analyst.util.watsonx_client.Embeddings", MockEmbeddings)
        mp.setattr("fn_watsonx_analyst.util.watsonx_client.ModelInference", MockModelInference)

        yield
