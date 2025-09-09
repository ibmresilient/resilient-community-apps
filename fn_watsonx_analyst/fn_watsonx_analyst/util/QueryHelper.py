import json
from typing import List
import requests
from requests import RequestException, JSONDecodeError
from requests import ConnectionError as RequestsConnectionError

from resilient import SimpleClient

from fn_watsonx_analyst.types import MessagePayload, MessageRole

from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.util.model_helper import ModelHelper
from fn_watsonx_analyst.util.errors import (
    WatsonxBadRequestException,
    WatsonxForbiddenException,
    WatsonxModelIdNotFoundException,
    WatsonxNotFoundException,
    WatsonxTokenLimitExceededException,
    WatsonxUnauthorizedException,
    WatsonxUnreachableException,
    WatsonxUnparseableResponseException,
    WatsonxApiException,
    WatsonxTooManyRequestsException,
)
from fn_watsonx_analyst.util.persistent_org_cache import PersistentCache
from fn_watsonx_analyst.util.retry import retry_with_backoff
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state

log = create_logger(__name__)


class QueryHelper:
    """
    Helper class to query the watsonx.ai API
    """

    API_KEY: str
    ENDPOINT: str

    model_id: str = app_state.get().model_id
    res_client: SimpleClient = app_state.get().res_client
    opts: dict = app_state.get().opts

    headers: dict = None

    def __init__(self):
        self.model_id = app_state.get().model_id
        self.res_client = app_state.get().res_client
        self.opts = app_state.get().opts
        if self.opts:
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.get_api_key(self.res_client)}",
            }

    def build_message(self, role: MessageRole, content: str) -> MessagePayload:
        """Builds a MessagePayload from a role and text content"""
        return {"content": content, "role": role}

    def _get_config(self) -> dict:
        try:
            return self.opts.get("fn_watsonx_analyst")
        except Exception as e:
            raise e

    def _get_base_endpoint(self) -> str:
        return self._get_config().get("watsonx_endpoint")

    def _get_project_id(self) -> str:
        return self._get_config().get("watsonx_project_id")

    def _get_api_endpoint(self) -> str:
        watsonx_ai_endpoint = self._get_base_endpoint()
        return watsonx_ai_endpoint + "/ml/v1/text/generation?version=2023-05-29"

    def get_api_key(self, res_client: SimpleClient) -> str:
        """
        Accesses fs cache to look for access token. If not found, it will attempt to fetch a new one.
        """
        try:
            api_key = self._get_config().get("watsonx_api_key")
        except Exception as e:
            log.error("Failed to get configuration.")
            raise e
        resp = PersistentCache("watsonx_key").get_data(
            res_client, "watsonx_key", api_key
        )
        try:
            return resp["access_token"]
        except Exception as e:
            raise WatsonxUnauthorizedException() from e

    @retry_with_backoff()
    def text_generation(
        self,
        prompt: str,
        arguments: str = None,
        stop_sequences: List[str] = None,
        repetition_penalty: float = 1.2,
        min_new_tokens: int = 1,
        max_new_tokens: int = 4096,
        timeout=120 * 1000,
        enable_moderation=True,
    ) -> WatsonxTextGenerationResponse:
        """
        Invoke watsonx.ai text generation endpoint, asking to complete the input until it reaches a stop sequence
        """
        if not stop_sequences:
            stop_sequences = [
                "<|assistant|>",
                "<|system|>",
                "@Watsonx",
                "@WatsonX",
                "@watsonx",
                "<|watsonx|>",
            ]

        if arguments:
            arguments = arguments.split(",")
            prompt = prompt.format(*arguments)

        hap = {"output": {"enabled": True, "threshold": 0.5}}
        if enable_moderation:
            hap["input"] = {"enabled": True, "threshold": 0.5}

        request_body = {
            "model_id": self.model_id,
            "input": prompt,
            "project_id": self._get_project_id(),
            "moderations": hap,
            "parameters": {
                "decoding_method": "greedy",
                "repetition_penalty": repetition_penalty,
                "min_new_tokens": min_new_tokens,
                "max_new_tokens": min(
                    max_new_tokens,
                    ModelHelper.max_output_tokens_for_model(self.model_id),
                ),
                "stop_sequences": stop_sequences,
                "include_stop_sequence": False,
                "time_limit": timeout,
            },
        }

        try:
            with requests.post(
                self._get_api_endpoint(),
                json.dumps(request_body),
                headers=self.headers,
                timeout=(timeout + 1000) / 1000,
            ) as response:
                match response.status_code:
                    case 200:
                        response_body: WatsonxTextGenerationResponse = response.json()
                        log.debug(
                            "[Input]:\n%s\n[Output]:\n%s",
                            request_body["input"],
                            response_body["results"][0]["generated_text"],
                        )
                        app_state.get().increment_input_tokens(
                            response_body["results"][0]["input_token_count"]
                        )
                        app_state.get().increment_output_tokens(
                            response_body["results"][0]["generated_token_count"]
                        )
                        return response_body
                    case WatsonxBadRequestException.status_code:
                        body = response.json()

                        match body["errors"][0]["code"]:
                            case WatsonxTokenLimitExceededException.code:
                                raise WatsonxTokenLimitExceededException()
                            case _:
                                raise WatsonxBadRequestException(json.dumps(body))
                    case WatsonxUnauthorizedException.status_code:
                        body = response.json()
                        raise WatsonxUnauthorizedException(json.dumps(body["errors"]))

                    case WatsonxForbiddenException.status_code:
                        body = response.json()
                        match body["errors"][0]["code"]:
                            case _:
                                raise WatsonxForbiddenException(
                                    json.dumps(body["errors"])
                                )

                    case WatsonxNotFoundException.status_code:
                        body = response.json()
                        match body["errors"][0]["code"]:
                            case WatsonxModelIdNotFoundException.code:
                                log.error("Model not found")
                                raise WatsonxModelIdNotFoundException(self.model_id)
                            case _:
                                raise WatsonxNotFoundException(
                                    json.dumps(body["errors"])
                                )
        except (ValueError, JSONDecodeError) as e:  # catch JSON parsing exceptions
            raise WatsonxUnparseableResponseException() from e
        except (RequestsConnectionError, ConnectionError, RequestException) as e:
            raise WatsonxUnreachableException() from e

    def get_generation_models(self) -> List[str]:
        """
        Helper method to get the text generation-capable models
        """
        url = (
            self._get_base_endpoint()
            + "/ml/v1/foundation_model_specs?version=2023-05-29?filters=function_text_generation"
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.get_api_key(self.res_client)}",
        }

        try:
            response = requests.get(url, headers=headers, timeout=30)
            match response.status_code:
                case 200 | 201:
                    resources = response.json().get("resources", None)
                    if resources is None:
                        raise WatsonxUnparseableResponseException()

                    models = []
                    for resource in resources:
                        models.append(resource["model_id"])
                    return models

                case WatsonxBadRequestException.status_code:
                    raise WatsonxBadRequestException(response.text)
                case (
                    WatsonxUnauthorizedException.status_code
                    | WatsonxForbiddenException.status_code
                ):
                    raise WatsonxUnauthorizedException(response.text)
                case _:
                    raise WatsonxApiException(f"Status code: {response.status_code}")

        except (RequestsConnectionError, ConnectionError, RequestException) as e:
            log.exception('unknown network/connection exception %s', e)
            raise WatsonxUnreachableException() from e

    def get_sentence_transformer(self):
        try:
            from sentence_transformers import SentenceTransformer
            return SentenceTransformer('all-MiniLM-L6-v2')
        except Exception as e:
            log.exception(
                "An error occurred while importing and loading sentence transformer model: %s",
                e,
            )
            raise

    @retry_with_backoff()
    def generate_embeddings(self, data: List[str])->List[list]:
        """
        generate embeddings (vector representations) of text data using either 
        a local sentence transformer model or an external Watson Natural Language Understanding (NLU) API, 
        depending on the configuration. 

        Takes only first 1000 chunks of data if data is too large.
        """
        local_embeddings = self._get_config().get("local_embeddings")
        if len(data) > 1000:
            data = data[0:1000]
        if local_embeddings is not None and local_embeddings not in ("False", "false"):
            try:
                transformer_model = self.get_sentence_transformer()
                embeddings = transformer_model.encode(data)
                return embeddings
            except Exception as e:
                log.exception(
                    "An error occurred while generating embeddings: %s",
                    e,
                )
                raise
        else:
            url = (
                self._get_base_endpoint()
                + "/ml/v1/text/embeddings?version=2023-10-25"
            )
            try:
                body = {
                    "inputs": data,
                    "model_id": "ibm/slate-125m-english-rtrvr",
                    "project_id": self._get_project_id()
                }
                response = requests.post(url, json.dumps(body), headers=self.headers, timeout=60)
                match response.status_code:
                    case (200 | 201):
                        results = response.json().get("results")
                        # Extracting the 'embedding' values
                        formatted_results = [item['embedding'] for item in results]
                        app_state.get().increment_embedding_tokens(response.json().get("input_token_count", 0))
                        return formatted_results
                    case (WatsonxBadRequestException.status_code):
                        raise WatsonxBadRequestException(response.text)
                    case (WatsonxUnauthorizedException.status_code | WatsonxForbiddenException.status_code):
                        raise WatsonxUnauthorizedException(response.text)
                    case (WatsonxTooManyRequestsException.status_code):
                        raise WatsonxTooManyRequestsException(response.text)
                    case _:
                        raise WatsonxApiException(f"Status code: {response.status_code}")

            except (RequestsConnectionError, ConnectionError, RequestException) as e:
                raise WatsonxUnreachableException() from e
