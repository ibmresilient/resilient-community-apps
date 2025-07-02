import json
import re
from typing import List

import requests
from requests import RequestException, JSONDecodeError
from requests import ConnectionError as RequestsConnectionError

from resilient import SimpleClient

from fn_watsonx_analyst.types import AIResponse, MessagePayload, MessageRole

from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose, ModelTag
from fn_watsonx_analyst.util.errors import (
    WatsonxBadRequestException,
    WatsonxForbiddenException,
    WatsonxModelIdNotFoundException,
    WatsonxNotFoundException,
    WatsonxTokenLimitExceededException,
    WatsonxUnauthorizedException,
    WatsonxUnreachableException,
    WatsonxUnparseableResponseException, WatsonxApiException, WatsonxTooManyRequestsException,
)
from fn_watsonx_analyst.util.persistent_org_cache import PersistentCache
from fn_watsonx_analyst.util.retry import retry_with_backoff
from fn_watsonx_analyst.util.util import create_logger, defang_text
from fn_watsonx_analyst.util.rich_text import RichTextHelper

log = create_logger(__name__)

class QueryHelper:
    """
    Helper class to query the watsonx.ai API
    """

    API_KEY: str
    ENDPOINT: str

    model_id: str
    res_client: SimpleClient
    opts: dict

    headers: dict

    filtered_elements = [
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "table",
        "tbody",
        "thead",
        "tr",
        "td",
    ]

    def __init__(
        self, res_client: SimpleClient = None, model_id: str = None, opts: dict = None
    ):
        self.res_client = res_client
        self.model_id = model_id
        self.opts = opts
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

    def process_output(self, text: str) -> str:
        """
        Run the post-processing of text - replace certain HTML elements that would distract, defang, etc.
        """
        text = defang_text(text)
        for ptrn in self.filtered_elements:
            text = re.sub(rf"<{ptrn}.*?>", "", text)
            text = re.sub(rf"</{ptrn}.*?>", "<br>", text)
            text = re.sub(rf"<{ptrn}.*?/>", "<br>", text)

        return f"<div style='white-space: break-word; white-space-collapse: collapse;'>{text}</div>"

    @retry_with_backoff()
    def text_generation(
        self,
        prompt: str,
        arguments: str = None,
        stop_sequences: List[str] = [
            "<|assistant|>",
            "<|system|>",
            "@Watsonx",
            "@WatsonX",
            "@watsonx",
            "<|watsonx|>",
        ],
        repetition_penalty: float = 1.2,
        min_new_tokens: int = 1,
        max_new_tokens: int = 2000,
        timeout=120 * 1000,
        purpose=AiResponsePurpose.NOTE_CONVERSATION,
        enable_moderation=True,
    ) -> AIResponse:
        """
        Invoke watsonx.ai text generation endpoint, asking to complete the input until it reaches a stop sequence
        """
        if arguments:
            arguments = arguments.split(",")
            prompt = prompt.format(*arguments)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.get_api_key(self.res_client)}",
        }

        hap = {"output": {"enabled": True, "threshold": 0.5}}
        if enable_moderation:
            hap["input"] = {"enabled": True, "threshold": 0.5}

        body = {
            "model_id": self.model_id,
            "input": prompt,
            "project_id": self._get_project_id(),
            "moderations": hap,
            "parameters": {
                "decoding_method": "greedy",
                "repetition_penalty": repetition_penalty,
                "min_new_tokens": min_new_tokens,
                "max_new_tokens": max_new_tokens,
                "stop_sequences": stop_sequences,
                "include_stop_sequence": False,
                "time_limit": timeout,
            },
        }
        try:
            with (requests.post(
                self._get_api_endpoint(),
                json.dumps(body),
                headers=headers,
                timeout=(timeout + 1000) / 1000,
            ) as response):
                match response.status_code:
                    case 200:
                        body = response.json()
                        result = body["results"][0]
                        generated_text: str

                        # flag to render markdown to HTML
                        if self._get_config().get("render_markdown", "true") in ["true", "True", True]:
                            generated_text = defang_text(RichTextHelper.toHTML(result["generated_text"]))
                        else:
                            generated_text = defang_text(result["generated_text"])

                        model_tag = ModelTag(self.model_id, purpose)

                        output: AIResponse = {
                            "generated_text": generated_text,
                            "raw_output": result["generated_text"],
                            "metadata": {
                                "created_at": model_tag.created_at,
                                "input_token_count": result["input_token_count"],
                                "generated_token_count": result[
                                    "generated_token_count"
                                ],
                                "stop_reason": result["stop_reason"],
                                "model_id": body["model_id"],
                            },
                            "tag": str(model_tag),
                        }
                        log.debug(
                            "[Input]:\n%s\n[Output]:\n%s\nInput tokens: %d\tOutput tokens: %d",
                            prompt,
                            output["raw_output"],
                            result["input_token_count"],
                            result["generated_token_count"],
                        )

                        return output
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
                case (200 | 201):
                    resources = response.json().get("resources", None)
                    if resources is None:
                        raise WatsonxUnparseableResponseException()

                    models = []
                    for resource in resources:
                        models.append(resource["model_id"])
                    return models

                case WatsonxBadRequestException.status_code:
                    raise WatsonxBadRequestException()
                case (WatsonxUnauthorizedException.status_code | WatsonxForbiddenException.status_code):
                    raise WatsonxUnauthorizedException()
                case _:
                    raise WatsonxApiException(f"Status code: {response.status_code}")

        except (RequestsConnectionError, ConnectionError, RequestException) as e:
            raise WatsonxUnreachableException() from e

    @retry_with_backoff()
    def generate_embeddings(self, data: List[str])->List[list]:
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
            response = requests.post(url, json.dumps(body), headers=self.headers, timeout=30)
            match response.status_code:
                case (200 | 201):
                    results = response.json().get("results")
                    # Extracting the 'embedding' values
                    formatted_results = [item['embedding'] for item in results]
                    return formatted_results
                case (WatsonxBadRequestException.status_code):
                    raise WatsonxBadRequestException()
                case (WatsonxUnauthorizedException.status_code | WatsonxForbiddenException.status_code):
                    raise WatsonxUnauthorizedException()
                case (WatsonxTooManyRequestsException.status_code):
                    raise WatsonxTooManyRequestsException()
                case _:
                    raise WatsonxApiException(f"Status code: {response.status_code}")

        except (RequestsConnectionError, ConnectionError, RequestException) as e:
            raise WatsonxUnreachableException() from e
