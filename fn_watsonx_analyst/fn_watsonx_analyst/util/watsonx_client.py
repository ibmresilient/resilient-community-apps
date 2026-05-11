import json
from typing import List, Sequence

from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference, Embeddings
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters

from fn_watsonx_analyst.types import MessagePayload, MessageRole
from fn_watsonx_analyst.types.watsonx_responses import WatsonxChatResponse
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
    WatsonxInternalErrorException,
)
from fn_watsonx_analyst.util.retry import retry_with_backoff
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state

log = create_logger(__name__)


class WatsonxClient:
    """
    Client for interacting with IBM watsonx.ai services.
    Provides chat, embeddings, and model listing capabilities.
    """

    def __init__(self):
        """Initialize the Watsonx client with credentials from app configuration."""
        self.model_id = app_state.get().model_id
        self.res_client = app_state.get().res_client
        self.opts = app_state.get().opts

        if not self.opts:
            raise ValueError("Application options not configured")

        self.credentials = Credentials(
            url=self._get_config_value('watsonx_endpoint'),
            api_key=self._get_config_value('watsonx_api_key')
        )
        self.wx_client = APIClient(self.credentials)
        self.project_id = self._get_config_value('watsonx_project_id')

    def _get_config_value(self, key: str) -> str | None:
        """
        Retrieve a configuration value from the fn_watsonx_analyst config section.
        
        Args:
            key: Configuration key to retrieve
            
        Returns:
            Configuration value
            
        Raises:
            ValueError: If configuration key is not found
        """
        config = self.opts.get("fn_watsonx_analyst", {})
        value = config.get(key)
        if not value:
            log.debug(f"Configuration key '{key}' not found or empty")
            return None
        return value

    def build_message(self, role: MessageRole, content: str) -> MessagePayload:
        """
        Build a message payload for chat interactions.
        
        Args:
            role: The role of the message sender (system, user, or assistant)
            content: The message content
            
        Returns:
            MessagePayload dictionary
        """
        return {"content": content, "role": role}

    @retry_with_backoff()
    def chat(
        self,
        messages: Sequence[MessagePayload],
        temperature: float = 1.0,
        max_tokens: int | None = None
    ) -> WatsonxChatResponse:
        """
        Send a chat request to watsonx.ai.
        
        Args:
            messages: Sequence of message payloads forming the conversation
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum tokens to generate (defaults to model's max)
            
        Returns:
            WatsonxChatResponse containing the model's reply
            
        Raises:
            Various WatsonxException types for different error conditions
        """
        try:

            if len(messages) < 1:
                raise ValueError("No messages specified for ai chat")

            # Set up chat parameters
            params = TextChatParameters(
                temperature=temperature,
                max_tokens=max_tokens or ModelHelper.max_output_tokens_for_model(self.model_id)
            )

            # Create model inference instance
            model = ModelInference(
                model_id=self.model_id,
                api_client=self.wx_client,
                params=params,
                project_id=self.project_id
            )

            # Execute chat - convert to list of dicts for SDK
            messages_list = [dict(msg) for msg in messages]
            response: WatsonxChatResponse = model.chat(messages_list) # type: ignore
            if "system" in response and "warnings" in response["system"]:
                log.warning(f"Warning from watsonx.ai: {json.dumps(response['system']['warnings'], indent=2)}")
            
            # Update token counts in app state
            if 'usage' in response:
                usage = response['usage']
                if 'prompt_tokens' in usage:
                    app_state.get().increment_input_tokens(usage['prompt_tokens'])
                if 'completion_tokens' in usage:
                    app_state.get().increment_output_tokens(usage['completion_tokens'])

            # Log response
            if response.get('choices') and response['choices']:
                reply = response['choices'][0]['message']['content']

                log.debug(
                    "[Input]:\n%s\n[Output]:\n%s",
                    messages[-1], reply,
                )
            else:
                log.warning(f"Unexpected response: {json.dumps(response, indent=2)}")

            return response

        except Exception as e:
            self._handle_exception(e)
            raise  # Ensure we don't fall through

    @retry_with_backoff()
    def generate_embeddings(self, texts: List[str], use_local: bool | None = None) -> List[list]:
        """
        Generate embeddings for text data.
        
        Args:
            texts: List of text strings to embed (max 1000)
            use_local: Override config to use local sentence transformer
            
        Returns:
            List of embedding vectors
            
        Raises:
            Various WatsonxException types for different error conditions
        """
        # Limit to 1000 texts
        if len(texts) > 1000:
            log.warning(f"Truncating {len(texts)} texts to 1000 for embedding")
            texts = texts[:1000]
        
        # Determine if using local embeddings
        if use_local is None:
            local_config = self._get_config_value('local_embeddings')
            use_local = local_config not in (None, "False", "false", "", "0")
        
        if use_local:
            return self._generate_local_embeddings(texts)
        else:
            return self._generate_watsonx_embeddings(texts)

    def _generate_local_embeddings(self, texts: List[str]) -> List[list]:
        """Generate embeddings using local sentence transformer model."""
        try:
            from sentence_transformers import SentenceTransformer
            
            log.debug("Using local sentence transformer for embeddings")
            model = SentenceTransformer('all-MiniLM-L6-v2')
            embeddings = model.encode(texts)
            
            # Convert to list of lists
            if hasattr(embeddings, 'tolist'):
                result = embeddings.tolist()
                if result and isinstance(result, list):
                    if not isinstance(result[0], list):
                        return [result]
                    return result
            return [list(e) for e in embeddings]

        except Exception as e:
            log.exception("Error generating local embeddings: %s", e)
            raise

    @retry_with_backoff()
    def _generate_watsonx_embeddings(self, texts: List[str]) -> List[list]:
        """Generate embeddings using watsonx.ai API."""
        try:
            embedding_model = ModelHelper.get_embedding_model(self.opts)
            log.debug(f"Using {embedding_model} on watsonx.ai for embeddings")
            
            embedding_model = Embeddings(
                model_id="ibm/slate-125m-english-rtrvr-v2", # TODO make configurable
                api_client=self.wx_client,
                project_id=self.project_id
            )

            results = embedding_model.generate(texts)
            if "input_token_count" in results:
                app_state.get().increment_embedding_tokens((results["input_token_count"])) # TODO count embedding tokens
            else:
                log.warning("Did not receive token usage from watsonx.")
            embeddings = []
            for result in results["results"]:
                embeddings.append(result["embedding"])
            return embeddings
        except Exception as e:
            self._handle_exception(e)
            raise  # Ensure we don't fall through

    def check_project(self) -> bool:
        """Interrogate watsonx api about project id - if project id is invalid, return False"""
        if not self.project_id:
            return False
        
        try:
            self.wx_client.projects.get_details(self.project_id)
            return True
        except Exception:
            return False

    def get_available_models(self) -> bool:
        """
        Retrieve list of available text generation models from watsonx.ai.
        
        Returns:
            List of model IDs
            
        Raises:
            Various WatsonxException types for different error conditions
        """
        try:
            model_specs = self.wx_client.foundation_models.get_model_specs(
                filters="function_text_chat"
            )

            if not model_specs or "resources" not in model_specs:
                raise WatsonxUnparseableResponseException()
            
            models = [resource["model_id"] for resource in model_specs["resources"]]
            log.debug(f"Retrieved {len(models)} available models")
            return True

        except Exception:
            return False

    def _handle_exception(self, exception: Exception) -> None:
        """
        Map SDK exceptions to custom exception types.
        
        Args:
            exception: The exception to handle
            
        Raises:
            Appropriate WatsonxException subclass
        """
        error_msg = str(exception).lower()

        if isinstance(exception, WatsonxUnparseableResponseException):
            raise exception
        
        # Token limit errors
        if "token" in error_msg and "limit" in error_msg:
            raise WatsonxTokenLimitExceededException() from exception

        # Authentication errors
        if "unauthorized" in error_msg or "401" in error_msg:
            raise WatsonxUnauthorizedException(str(exception)) from exception

        # Permission errors
        if "forbidden" in error_msg or "403" in error_msg:
            raise WatsonxForbiddenException(str(exception)) from exception

        # Not found errors
        if "not found" in error_msg or "404" in error_msg:
            if "model" in error_msg:
                raise WatsonxModelIdNotFoundException(self.model_id) from exception
            raise WatsonxNotFoundException(str(exception)) from exception

        # Bad request errors
        if "bad request" in error_msg or "400" in error_msg:
            raise WatsonxBadRequestException(str(exception)) from exception

        # Rate limiting errors
        if "rate limit" in error_msg or "429" in error_msg:
            raise WatsonxTooManyRequestsException(str(exception)) from exception

        # Connection errors
        if "connection" in error_msg or "timeout" in error_msg:
            raise WatsonxUnreachableException() from exception

        # Internal server errors
        if "500" in error_msg or "internal" in error_msg:
            raise WatsonxInternalErrorException(str(exception)) from exception

        # Generic API error
        log.exception("Unexpected watsonx API error: %s", exception)
        raise WatsonxApiException(str(exception)) from exception
