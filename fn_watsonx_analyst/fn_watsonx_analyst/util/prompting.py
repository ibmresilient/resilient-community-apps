import datetime
from typing import Literal
import regex as re



from fn_watsonx_analyst.config.loaders import LanguagePromptDict, load_prompt_config
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.rich_text import RichTextHelper
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state

logger = create_logger(__name__)


class Prompting:

    supported_languages = ["en", "es", "fr", "de", "pt", "ja"]
    default_language: str
    detected_language: str

    prompting_config: LanguagePromptDict

    def __init__(self) -> None:
        try:
            self.default_language = self._get_default_language()
            self.prompting_config = load_prompt_config()

        except Exception as e:  # pragma: no cover
            logger.exception(
                "An error occurred while initialising the prompting class: %s", e
            )
            raise

    def _get_help_user(self, locale: str) -> str:
        return self.prompting_config.get(locale, {}).get("misc", {}).get("help_user", "")

    @staticmethod
    def _get_default_language() -> str:
        try:
            return app_state.get().opts["fn_watsonx_analyst"]["default_language"]
        except:
            logger.warning("Error getting default language. Using 'en'.")
            return "en"

    def __retrieve_prompt_data(self, locale: str) -> dict:
        return self.prompting_config.get(locale, {}).get("prompt_grounding", {})
        # return self.prompting_config.get("prompt_data", {}).get(locale, {})

    def __retrieve_prompt(self, prompt_type: Literal["system", "user"], prompt_key: str, locale: str) -> str:
        """
        Fetches the prompt string template from the config.
        """

        curr_date = datetime.date.today()
        prompt = (self.prompting_config.get(locale, {})
                  .get(prompt_type + "_prompts", {}).get(prompt_key, ""))

        if not prompt:
            raise ValueError(
                f"Prompt not found for '{prompt_type}' prompt type with key '{prompt_key}' in the locale '{locale}'.")
        if "{current_date}" in prompt:
            prompt = prompt.format(
                current_date=f"{curr_date.isoweekday()}, {curr_date.strftime('%Y-%m-%d')}"
            )
        return prompt

    def _get_user_prompt(self, purpose: AiResponsePurpose, locale: str) -> str:
        key = ""
        if purpose == AiResponsePurpose.ARTIFACT_SUMMARY:
            key = "contents_summary"
        elif purpose == AiResponsePurpose.ARITFACT_META_SUMMARY:
            key = "metadata_summary"
        else:
            return ""

        return self.__retrieve_prompt("user", key, locale)

    def _get_system_prompt(self, purpose: AiResponsePurpose, locale: str) -> str:
        key = "default_prompt"
        match purpose:
            case AiResponsePurpose.ARTIFACT_CONVERSATION:
                key = "artifact_qna"
            case AiResponsePurpose.ARTIFACT_SUMMARY:
                key = "contents_summary"
            case AiResponsePurpose.ARITFACT_META_SUMMARY:
                key = "metadata_summary"
            case _:
                key = "default_prompt"

        return self.__retrieve_prompt("system", key, locale)


    def _detect_language_with_langid(self, text:str, confidence_threshold=0.9)-> str:
        """
        Detects language of query
        Args:
            text (str): Query to detect language of
            confidence_threshold (float): Minimum allowable confidence before fallback
        Returns:
            str: Detected language code from supported_languages or default_lang if confidence too low.
        """
        from py3langid.langid import LanguageIdentifier, MODEL_FILE

        try:
            default_lang = self.default_language
            identifier = LanguageIdentifier.from_pickled_model(MODEL_FILE, norm_probs=True)
            identifier.set_languages(langs=self.supported_languages)

            lang, prob = identifier.classify(text)

            logger.debug("Detected '%s' lang with confidence %s%%", lang, int(prob * 100)) # pylint: disable=consider-using-f-string
            if prob >= confidence_threshold:
                return lang

            logger.debug("Using fallback language")
            return default_lang
        except Exception as e:  # pragma: no cover
            logger.exception(
                "An error occurred during user query language classification: %s", e
            )
            raise

    def prepare_prompt_data(self, query, context, messages, get_relevant_prompts, relevant_fields_info, system_prompt, max_token_limit=800, **kwargs):
        """
        Prepares the data required for building the prompt.

        Args:
            purpose (AiResponsePurpose): Determines which system prompt(s) to use.
            model (str): Name of the model in string.
            query (str): Query that was invoked.
            context (str): The relevant context chunk given for the query.
            chunking (Chunking): Optional dependency injection for chunking operations.
            messages (List[MessagePayload]): Previous messages in conversation.
            get_relevant_prompts (bool): Set to False to exclude relevant prompts.
            **kwargs: Additional keyword arguments for formatting.

        Returns:
            tuple: A tuple containing system_prompt, relevant_prompt_chunks, relevant_messages, help_user_text, query, and context.
        """
        purpose = app_state.get().purpose
        chunking = Chunking()
        relevant_messages = ""
        try:
            relevant_messages = ""
            locale = self.default_language
            if query and purpose is not AiResponsePurpose.INCIDENT_SUMMARY: # avoid pointless language id
                self.detected_language = self._detect_language_with_langid(query)

            help_user_text = ""
            relevant_prompt_chunks = ""

            if purpose in [AiResponsePurpose.NOTE_CONVERSATION, AiResponsePurpose.ARTIFACT_CONVERSATION]:
                locale = self._detect_language_with_langid(query)
                help_user_text = self._get_help_user(locale)
                if get_relevant_prompts:
                    prompt_chunks = chunking.split_json_to_chunks_prompts(
                        self.__retrieve_prompt_data(locale)
                    )
                    relevant_prompt_chunks = chunking.retrieve_relevant_chunks_watsonx(
                        query, prompt_chunks
                    )[:2]

                if messages and len(messages) > 1:
                    messages = messages[:-1]  # pop off query message, as not needed.
                    message_chunks = chunking.split_data_into_token_chunks(
                        "".join(map(lambda x: x.get("content", ""), messages)), 400
                    )
                    relevant_messages = chunking.retrieve_relevant_chunks_watsonx(
                        query, message_chunks, threshold=0.1, score_threshold=0.0
                    )
                    relevant_messages = RichTextHelper.extract_text(' '.join(relevant_messages))
                else:
                    relevant_messages = ""

                system_prompt = self._get_system_prompt(purpose, locale).format(**kwargs)

            # New logic for AiResponsePurpose.INCIDENT_SUMMARY
            elif purpose == AiResponsePurpose.INCIDENT_SUMMARY:
                relevant_messages = ""
                help_user_text = messages
                context_tokens = chunking.estimate_tokens(context)
                total_tokens = (
                    chunking.estimate_tokens(system_prompt) +
                    chunking.estimate_tokens(relevant_fields_info) +
                    chunking.estimate_tokens(relevant_messages) +
                    chunking.estimate_tokens(help_user_text) +
                    context_tokens +
                    chunking.estimate_tokens(query)
                )
                tokens_to_remove = 0
                if total_tokens > max_token_limit:
                    tokens_to_remove = total_tokens - max_token_limit
                if context_tokens > tokens_to_remove:
                    context = context[:len(context) - tokens_to_remove] # Trim context
                else:
                    context = "" # If context is too small, remove it completely
                relevant_prompt_chunks = relevant_fields_info
                return system_prompt, relevant_prompt_chunks, relevant_messages, help_user_text, query, context

            else:
                system_prompt = self._get_system_prompt(purpose, locale).format(**kwargs)
                query = self._get_user_prompt(purpose, locale).format(**kwargs)

            return system_prompt, relevant_prompt_chunks, relevant_messages, help_user_text, query, context
        except Exception as e:
            logger.exception("An error occurred while preparing prompt data: %s", e)
            raise

    def format_prompt(self, model, system_prompt, relevant_prompt_chunks, relevant_messages, help_user_text, query, context):
        """
        Formats the prompt based on the model type.

        Args:
            model (str): Name of the model in string.
            system_prompt (str): The system prompt text.
            relevant_prompt_chunks (str): Relevant prompt chunks.
            relevant_messages (str): Relevant messages from the conversation.
            help_user_text (str): Help text for the user.
            query (str): The query text.
            context (str): The context text.

        Returns:
            str: The formatted prompt string.
        """
        if not context:
            context = ""
        try:
            if relevant_messages:
                relevant_messages = "These are the responses from previous query.\n\n" + relevant_messages + "\n\nThis is the incident payload.\n\n"

            if re.search(r"\bibm/granite-3\b", model, re.IGNORECASE):
                prompt = f"""
                <|start_of_role|>system<|end_of_role|>
                {system_prompt}

                {relevant_prompt_chunks}

                {help_user_text}

                {relevant_messages}

                
                {context}

                <|end_of_text|>
                    <|start_of_role|>user<|end_of_role|>{query}<|end_of_text|>
                    <|start_of_role|>assistant<|end_of_role|>
                    """
            elif re.search(r"\bmeta-llama\b", model, re.IGNORECASE):
                prompt = f"""
                "<|begin_of_text|><|start_header_id|>system<|end_header_id|>
                {system_prompt}

                {relevant_prompt_chunks}

                {relevant_messages}

                {help_user_text}
                {context}

                <|eot_id|>
                <|start_header_id|>user<|end_header_id|>{query}<|eot_id|>
                <|start_header_id|>assistant<|end_header_id|>
                "
                """
            elif re.search(r"\bmistralai\b", model, re.IGNORECASE):
                prompt = f"""
                <s>[INST] 
                {system_prompt}

                {relevant_prompt_chunks}
                
                {relevant_messages}

                [INST] {help_user_text}
                {context}

                [INST] </s>
                [INST] {query} [/INST]
                """
            elif re.search(r'\bcode-instruct\b', model, re.IGNORECASE):
                prompt = f"""
                System:
                {system_prompt}

                {relevant_messages}

                {context}

                Question: 
                {query} 

                Answer:
                """
            else:
                prompt = f"""
                    <|system|>
                    {system_prompt}

                    {relevant_prompt_chunks}
                    
                    {relevant_messages}

                    {help_user_text}
                    {context}
                    <|user|>{query}
                    <|assistant|>
                    """
            prompt = "\n".join([line.lstrip() for line in prompt.split("\n")])
            return prompt
        except Exception as e:
            logger.exception("An error occurred while determining prompt format: %s", e)
            raise

    def build_prompt(self, query, context, messages=None, get_relevant_prompts=True, relevant_fields_info="", system_prompt = "", max_token_limit=800, **kwargs):
        """
        Builds a prompt based on the model chosen by preparing the necessary data and formatting it accordingly.

        Args:
            purpose (AiResponsePurpose): Determines which system prompt(s) to use.
            query (str): Query that was invoked.
            context (str): The relevant context chunk given for the query.
            chunking (Chunking): Optional dependency injection for chunking operations.
            messages (List[MessagePayload], optional): Previous messages in conversation. Defaults to None.
            get_relevant_prompts (bool): Set to False to exclude relevant prompts. Defaults to True.
            **kwargs: Additional keyword arguments for formatting.

        Returns:
            str: The final prompt in the model's format with the system and user tags.
        """
        try:
            model = app_state.get().model_id
            system_prompt, relevant_prompt_chunks, relevant_messages, help_user_text, query, context = self.prepare_prompt_data(
                query, context, messages, get_relevant_prompts,relevant_fields_info, system_prompt, max_token_limit, **kwargs
            )
            return self.format_prompt(model, system_prompt, relevant_prompt_chunks, relevant_messages, help_user_text, query, context)
        except Exception as e:
            logger.exception("An error occurred while building prompt for LLM models: %s", e)
            raise
            
