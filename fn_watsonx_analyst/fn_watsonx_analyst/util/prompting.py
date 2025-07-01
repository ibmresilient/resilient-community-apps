import datetime
import logging
from typing import List, Optional, Literal
import os
import json
import regex as re

from py3langid.langid import LanguageIdentifier, MODEL_FILE

from fn_watsonx_analyst.types.message_payload import MessagePayload
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.rich_text import RichTextHelper
from fn_watsonx_analyst.util.util import create_logger

logger = create_logger(__name__)

class Prompting:

    supported_languages = ["en", "es", "fr", "de", "pt"]
    default_language: str

    prompting_config: dict

    def __init__(self, opts: dict = None) -> None:
        try:
            self.default_language = self._get_default_language(opts)
            prompting_config_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "prompting_config.json")
            )
            with open(prompting_config_path, "r", encoding="utf-8") as f:
                self.prompting_config = json.load(f)

        except Exception as e:  # pragma: no cover
            logger.exception(
                "An error occurred while initialising the prompting class: %s", e
            )
            raise

    def _get_help_user(self, locale: str) -> str:
        return self.prompting_config.get("misc", {}).get(locale, {}).get("help_user", "")

    @staticmethod
    def _get_default_language(opts: dict):
        try:
            return opts["fn_watsonx_analyst"]["default_language"]
        except:
            logger.warning("Error getting default language. Using 'en'.")
            return "en"

    def __retrieve_prompt_data(self, locale: str) -> dict:
        return self.prompting_config.get("prompt_data", {}).get(locale, {})

    def __retrieve_prompt(self, prompt_type: Literal["system", "user"], prompt_key: str, locale: str) -> str:
        """
        Fetches the prompt string template from the config.
        """
        curr_date = datetime.date.today()
        prompt = (self.prompting_config.get(prompt_type+ "_prompts", {})
                  .get(locale)
                  .get(prompt_key))
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

        return self.__retrieve_prompt("user", key, locale)

    def _get_system_prompt(self, purpose: AiResponsePurpose, locale: str) -> str:
        key = "default_prompt"
        if purpose == AiResponsePurpose.ARTIFACT_CONVERSATION:
            key = "artifact_qna"
        elif purpose in [AiResponsePurpose.ARTIFACT_SUMMARY]:
            key = "contents_summary"

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

    def build_prompt(
        self,
        purpose: AiResponsePurpose,
        model: str,
        query: Optional[str],
        context: Optional[str],
        chunking: Optional[Chunking],
        messages: List[MessagePayload] = None,
        get_relevant_prompts=True,
        **kwargs
    ) -> str:
        """
        Builds a prompt based on the model chosen
        Splits a JSON-like dictionary prompt into chunks of string prompts, each limited to a specified maximum size.
        Args:
            purpose (AiResponsePurpose): determines which system prompt(s) to use
            model (str): name of the model in string
            query (str): query that was invoked
            context (str): the relevant context chunk given for the query
            chunking (Chunking): Optional dependency injection
            messages (List[MessagePayload]): Previous messages in conversation
            get_relevant_prompts (bool): set to False to exclude relevant prompts
        Returns:
            prompt (str): The final prompt in the models format with the system and user tags
        """

        locale = self.default_language
        if query:
            locale = self._detect_language_with_langid(query)

        system_prompt = self._get_system_prompt(purpose, locale)

        help_user_text = ""
        relevant_prompt_chunks = ""
        if purpose in [AiResponsePurpose.NOTE_CONVERSATION, AiResponsePurpose.ARTIFACT_CONVERSATION]:

            help_user_text = self._get_help_user(locale)

            relevant_prompt_chunks = ""

            if get_relevant_prompts:
                prompt_chunks = chunking.split_json_to_chunks_prompts(
                    self.__retrieve_prompt_data(locale)
                )
                relevant_prompt_chunks = chunking.retrieve_relevant_chunks_watsonx(
                    query, prompt_chunks, model
                )[:2]
        if purpose == AiResponsePurpose.ARTIFACT_SUMMARY:
            query = self._get_user_prompt(purpose, self.default_language)

        if messages and len(messages) > 1:
            messages = messages[:-1]  # pop off query message, as not needed.
            message_chunks = chunking.split_data_into_token_chunks(
                "".join(map(lambda x: x.get("content", ""), messages)), 200
            )
            relevant_messages = chunking.retrieve_relevant_chunks_watsonx(
                query, message_chunks, model, chunking.max_tokens_for_model(model), 0.1
            )

            relevant_messages = RichTextHelper.extract_text(' '.join(relevant_messages))
        else:
            relevant_messages = ""

        system_prompt = system_prompt.format(**kwargs)
        query = query.format(**kwargs)

        try:
            if re.search(r"\bibm/granite-3\b", model, re.IGNORECASE):

                # Prompt format for granite 3 models
                prompt = f"""
                <|start_of_role|>system<|end_of_role|>
                {system_prompt}

                {relevant_prompt_chunks}

                {relevant_messages}

                {help_user_text}
                {context}

                <|end_of_text|>
                    <|start_of_role|>user<|end_of_role|>{query}<|end_of_text|>
                    <|start_of_role|>assistant<|end_of_role|>
                    """

            elif re.search(r"\bmeta-llama\b", model, re.IGNORECASE):
                # Prompt format for meta-llama models
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
                # Prompt format for mistral models
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

            elif(re.search(r'\bcode-instruct\b', model, re.IGNORECASE)):
                # Prompt format for code instruct models
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
                # default prompt for granite and other models
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
            # remove left-padding
            prompt = "\n".join([line.lstrip() for line in prompt.split("\n")])
            return prompt
        except Exception as e:
            logger.exception("An error occurred while creating the prompt: %s", e)
            raise
