import datetime
from typing import List, Literal

from fn_watsonx_analyst.config.loaders import LanguagePromptDict, load_prompt_config
from fn_watsonx_analyst.types import MessagePayload, MessageRole
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.rich_text import RichTextHelper
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state

logger = create_logger(__name__)


class ChatPrompting:
    """
    Simplified prompting class for chat-based interactions with watsonx.
    Loads prompts from prompts.yaml and builds message arrays for chat APIs.
    """

    supported_languages = ["en", "es", "fr", "de", "pt", "ja"]
    default_language: str
    prompting_config: LanguagePromptDict

    def __init__(self) -> None:
        """Initialize the prompting system with configuration."""
        try:
            self.default_language = self._get_default_language()
            self.prompting_config = load_prompt_config()
        except Exception as e:
            logger.exception("Error initializing ChatPrompting: %s", e)
            raise

    @staticmethod
    def _get_default_language() -> str:
        """Get the default language from configuration."""
        try:
            return app_state.get().opts["fn_watsonx_analyst"]["default_language"]
        except Exception:
            logger.warning("Error getting default language. Using 'en'.")
            return "en"

    def detect_language(self, text: str, confidence_threshold: float = 0.9) -> str:
        """
        Detect the language of the given text.
        
        Args:
            text: Text to analyze
            confidence_threshold: Minimum confidence to accept detection
            
        Returns:
            Detected language code or default language
        """
        try:
            from py3langid.langid import LanguageIdentifier, MODEL_FILE

            identifier = LanguageIdentifier.from_pickled_model(MODEL_FILE, norm_probs=True)
            identifier.set_languages(langs=self.supported_languages)

            lang, prob = identifier.classify(text)

            logger.debug("Detected '%s' language with confidence %d%%", lang, int(prob * 100))
            
            if prob >= confidence_threshold:
                return lang

            logger.debug("Using fallback language: %s", self.default_language)
            return self.default_language
            
        except Exception as e:
            logger.exception("Error during language detection: %s", e)
            return self.default_language

    def _get_prompt_text(
        self, 
        prompt_type: Literal["system_prompts", "user_prompts", "misc", "prompt_grounding"],
        key: str,
        locale: str
    ) -> str:
        """
        Retrieve a prompt text from the configuration.
        
        Args:
            prompt_type: Type of prompt section
            key: Specific prompt key
            locale: Language code
            
        Returns:
            Prompt text with current date substituted
        """
        prompt = (
            self.prompting_config
            .get(locale, {})
            .get(prompt_type, {})
            .get(key, "")
        )

        if not prompt:
            logger.warning(
                "Prompt not found: type='%s', key='%s', locale='%s'",
                prompt_type, key, locale
            )
            return ""

        # Substitute current date if present
        if "{current_date}" in prompt:
            curr_date = datetime.date.today()
            prompt = prompt.format(
                current_date=f"{curr_date.isoweekday()}, {curr_date.strftime('%Y-%m-%d')}"
            )

        return prompt

    def get_system_prompt(self, purpose: AiResponsePurpose, locale: str, **kwargs) -> str:
        """
        Get the system prompt for a given purpose.
        
        Args:
            purpose: The purpose/type of AI response
            locale: Language code
            **kwargs: Additional format arguments
            
        Returns:
            Formatted system prompt
        """
        # Map purpose to prompt key
        if purpose == AiResponsePurpose.ARTIFACT_CONVERSATION:
            key = "artifact_qna"
        elif purpose == AiResponsePurpose.ARTIFACT_SUMMARY:
            key = "contents_summary"
        elif purpose == AiResponsePurpose.ARITFACT_META_SUMMARY:
            key = "metadata_summary"
        elif purpose == AiResponsePurpose.ARTIFACT_META_CONVERSATION:
            key = "metadata_conversation"
        else:
            key = "default_prompt"
        prompt = self._get_prompt_text("system_prompts", key, locale)
        
        # Format with any provided kwargs
        if kwargs:
            try:
                prompt = prompt.format(**kwargs)
            except KeyError as e:
                logger.warning("Missing format key in system prompt: %s", e)
        
        return prompt

    def get_user_prompt(self, purpose: AiResponsePurpose, locale: str, **kwargs) -> str:
        """
        Get the user prompt for a given purpose.
        
        Args:
            purpose: The purpose/type of AI response
            locale: Language code
            **kwargs: Additional format arguments
            
        Returns:
            Formatted user prompt
        """
        # Map purpose to prompt key
        if purpose == AiResponsePurpose.ARTIFACT_SUMMARY:
            key = "contents_summary"
        elif purpose == AiResponsePurpose.ARITFACT_META_SUMMARY:
            key = "metadata_summary"
        elif purpose == AiResponsePurpose.ARTIFACT_META_CONVERSATION:
            key = "metadata_conversation"
        else:
            return ""
        
        prompt = self._get_prompt_text("user_prompts", key, locale)
        
        # Format with any provided kwargs
        if kwargs:
            try:
                prompt = prompt.format(**kwargs)
            except KeyError as e:
                logger.warning("Missing format key in user prompt: %s", e)
        
        return prompt

    def get_help_text(self, locale: str) -> str:
        """Get the help text for the user in the specified language."""
        return self._get_prompt_text("misc", "help_user", locale)

    def get_grounding_text(self, key: str, locale: str) -> str:
        """
        Get grounding/context text for incidents, artifacts, etc.
        
        Args:
            key: Type of grounding (incident, artifact, attachment, task)
            locale: Language code
            
        Returns:
            Grounding text
        """
        return self._get_prompt_text("prompt_grounding", key, locale)

    def build_chat_messages(
        self,
        purpose: AiResponsePurpose,
        query: str,
        context: str = "",
        previous_messages: List[MessagePayload] | None = None,
        locale: str | None = None,
        include_relevant_prompts: bool = True,
        max_context_tokens: int = 800,
        **format_kwargs
    ) -> List[MessagePayload]:
        """
        Build a list of chat messages for the watsonx chat API.
        
        Args:
            purpose: The purpose/type of AI response
            query: User's query or prompt
            context: Additional context (artifact data, incident data, etc.)
            previous_messages: Previous conversation messages
            locale: Language code (auto-detected if None)
            include_relevant_prompts: Whether to include relevant prompt chunks
            max_context_tokens: Maximum tokens for context
            **format_kwargs: Additional formatting arguments
            
        Returns:
            List of MessagePayload objects ready for chat API
        """
        try:
            # Detect language if not provided
            if locale is None:
                if query and purpose != AiResponsePurpose.INCIDENT_SUMMARY:
                    locale = self.detect_language(query)
                else:
                    locale = self.default_language

            messages: List[MessagePayload] = []
            chunking = Chunking()

            # Build system message
            system_content_parts = []
            
            # Add main system prompt
            system_prompt = self.get_system_prompt(purpose, locale, **format_kwargs)
            if system_prompt:
                system_content_parts.append(system_prompt)

            # Add relevant prompt chunks for conversation purposes
            if include_relevant_prompts and purpose in [
                AiResponsePurpose.NOTE_CONVERSATION,
                AiResponsePurpose.ARTIFACT_CONVERSATION,
                AiResponsePurpose.ARTIFACT_META_CONVERSATION
            ]:
                grounding_data = self.prompting_config.get(locale, {}).get("prompt_grounding", {})
                if grounding_data:
                    prompt_chunks = chunking.split_json_to_chunks_prompts(grounding_data)
                    relevant_chunks = chunking.retrieve_relevant_chunks_watsonx(
                        query, prompt_chunks
                    )[:2]
                    if relevant_chunks:
                        system_content_parts.append("\n".join(relevant_chunks))

            # Legacy context support: If context is provided but no format_kwargs,
            # append to system message for backward compatibility
            # New code should use format_kwargs instead
            if context and not format_kwargs:
                logger.warning(
                    "Using deprecated 'context' parameter. Consider using format_kwargs instead."
                )
                system_content_parts.append(f"Context:\n{context}")

            # Create system message
            if system_content_parts:
                messages.append({
                    "role": "system",
                    "content": "\n\n".join(system_content_parts)
                })

            # Add relevant previous messages for conversations
            if previous_messages and purpose in [
                AiResponsePurpose.NOTE_CONVERSATION,
                AiResponsePurpose.ARTIFACT_CONVERSATION,
                AiResponsePurpose.ARTIFACT_META_CONVERSATION
            ]:
                # Extract relevant messages using chunking
                if len(previous_messages) > 1:
                    # Don't include the current query message
                    prev_msgs = previous_messages[:-1]
                    message_text = "".join(msg.get("content", "") for msg in prev_msgs)
                    message_chunks = chunking.split_data_into_token_chunks(message_text, 400)
                    relevant_msg_chunks = chunking.retrieve_relevant_chunks_watsonx(
                        query, message_chunks, threshold=0.1, score_threshold=0.0
                    )

                    if relevant_msg_chunks:
                        relevant_text = RichTextHelper.extract_text(' '.join(relevant_msg_chunks))
                        if relevant_text:
                            messages.append({
                                "role": "system",
                                "content": f"Previous conversation context:\n{relevant_text}"
                            })

            # Add user message
            user_content_parts = []

            # Add specific user prompt if available
            user_prompt = self.get_user_prompt(purpose, locale, **format_kwargs)
            if user_prompt:
                user_content_parts.append(user_prompt)

            # Add the actual query
            if query:
                user_content_parts.append(query)

            if user_content_parts:
                messages.append({
                    "role": "user",
                    "content": "\n\n".join(user_content_parts)
                })

            logger.debug("Built %d chat messages for purpose: %s", len(messages), purpose)
            return messages

        except Exception as e:
            logger.exception("Error building chat messages: %s", e)
            raise

    def build_simple_chat(
        self,
        system_prompt: str,
        user_message: str,
        previous_messages: List[MessagePayload] | None = None
    ) -> List[MessagePayload]:
        """
        Build a simple chat message array without complex processing.
        
        Args:
            system_prompt: System prompt text
            user_message: User's message
            previous_messages: Optional previous conversation messages
            
        Returns:
            List of MessagePayload objects
        """
        messages: List[MessagePayload] = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        if previous_messages:
            messages.extend(previous_messages)
        
        if user_message:
            messages.append({"role": "user", "content": user_message})
        
        return messages
