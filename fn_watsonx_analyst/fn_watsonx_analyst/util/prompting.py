import datetime
from typing import List
import logging
import os
import json
import regex as re

from fn_watsonx_analyst.types.message_payload import MessagePayload
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking

logger = logging.getLogger(__name__)


class Prompting:

    prompting_config: dict

    def __init__(self) -> None:
        try:
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

    def __retrieve_prompt(self, prompt_key: str) -> str:
        curr_date = datetime.date.today()
        return (
            self.prompting_config.get("system_prompts", {})
            .get(prompt_key)
            .format(
                current_date=f"{curr_date.isoweekday()}, {curr_date.strftime('%Y-%m-%d')}"
            )
        )

    def _get_system_prompt(self, purpose: AiResponsePurpose) -> str:
        match purpose:
            case AiResponsePurpose.ARTIFACT_CONVERSATION:
                return self.__retrieve_prompt("artifact_qna")
            case _:
                return self.__retrieve_prompt("default_prompt")

    def build_prompt(
        self,
        purpose: AiResponsePurpose,
        model: str,
        query: str,
        context: str,
        messages: List[MessagePayload] = [],
        get_relevant_prompts=True,
    ) -> str:
        """
        Builds a prompt based on the model chosen
        Splits a JSON-like dictionary prompt into chunks of string prompts, each limited to a specified maximum size.
        Args:
            purpose (AiResponsePurpose): determines which system prompt(s) to use
            model (str): name of the model in string
            query (str): query that was invoked
            context (str): the relevant context chunk given for the query
            messages (List[MessagePayload]): Previous messages in conversation
            get_relevant_prompts (bool): set to False to exclude relevant prompts
        Returns:
            prompt (str): The final prompt in the models format with the system and user tags
        """
        chunking = Chunking()
        system_prompt = self._get_system_prompt(purpose)
        relevant_prompt_chunks = ""

        if get_relevant_prompts:
            prompt_chunks = chunking.split_json_to_chunks_prompts(
                self.prompting_config.get("prompt_data")
            )
            relevant_prompt_chunks = chunking.retrieve_top_chunks_tfidf(
                query, prompt_chunks, model
            )[:2]

        messages = messages[:-1]  # pop off query message, as not needed.

        message_chunks = []
        if len(messages) > 0:
            message_chunks = chunking.split_data_into_token_chunks(
                "".join(map(lambda x: x.get("content", ""), messages)), 200
            )

            relevant_messages = chunking.retrieve_top_chunks_tfidf(
                query, message_chunks, model, chunking.max_tokens_for_model(model), 0.1
            )
        else:
            relevant_messages = ""

        try:
            if re.search(r"\bibm/granite-3\b", model, re.IGNORECASE):

                # Prompt format for granite 3 models
                prompt = f"""
                <|start_of_role|>system<|end_of_role|>
                {system_prompt}

                {relevant_prompt_chunks}

                {relevant_messages}

                You are going to help the analyst using this information:
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

                You are going to help the analyst using this information:
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

                [INST] You are going to help the analyst using this information:
                {context}
                [INST] </s>
                [INST] {query} [/INST]
                """

            else:
                # default prompt for granite and other models
                prompt = f"""
                    <|system|>
                    {system_prompt}

                    {relevant_prompt_chunks}
                    
                    {relevant_messages}

                    You are going to help the analyst using this information:
                    {context}
                    <|user|>{query}
                    <|assistant|>
                    """
            return prompt
        except Exception as e:
            logger.exception("An error occurred while creating the prompt: %s", e)
            raise
