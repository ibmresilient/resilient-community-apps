"""Unit Tests for Prompting"""

# pylint: disable=line-too-long

import pytest
import json
import os

from fn_watsonx_analyst.types.message_payload import MessagePayload
from fn_watsonx_analyst.util.prompting import Prompting
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose


class TestPrompting:
    """Unit tests for Prompting class."""

    prompting: Prompting
    model_config: dict

    def setup_method(self):
        """Initialize the model config"""
        # self.text = "This is a sample text to test the split_data_into_token_chunks function."
        # self.max_tokens = 10
        self.prompting = Prompting()
        model_config_path = os.path.abspath(
                os.path.join(os.path.dirname("fn_watsonx_analyst/util/"), "model_config.json")
                )
        with open(model_config_path, "r", encoding="utf-8") as f:
            self.model_config = json.load(f)


    def test_return_type(self):
        """Test to see if the prompt is of a correct type for granite 3"""
        model = next((model for model in self.model_config if model['model_name'] == 'ibm/granite-3-2b-instruct'), None)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"

        result = Prompting.build_prompt(
            self.prompting,
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            model=model["model_name"],
            query=query,
            context=context,
        )
        assert isinstance(result, str)

    def test_return_format(self):
        """Test to see if the prompt format is correct for granite """
        model = next((model for model in self.model_config if model['model_name'] == 'ibm/granite-13b-instruct'), None)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"

        result = Prompting.build_prompt(
            self.prompting,
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            model=model["model_name"],
            query=query,
            context=context,
        )
        assert result.strip().startswith("<|system|>")

    def test_invalid_model(self):
        """Test to see if the method catches an invalid model ask"""
        model = next((model for model in self.model_config if model['model_name'] == 'google/bard'), None)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        expected_error = TypeError("'NoneType' object is not subscriptable")
        with pytest.raises(TypeError) as error:
            Prompting.build_prompt(
            self.prompting,
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            model=model["model_name"],
            query=query,
            context=context,
        )
        assert str(error.value) == str(expected_error)

    def test_default_model(self):
        """ Test to see if the method catches an invalid model ask"""
        model = next((model for model in self.model_config if model['model_name'] == 'google/flan-t5-xl-3b'), None)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        result = Prompting.build_prompt(
            self.prompting,
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            model=model["model_name"],
            query=query,
            context=context,
        )
        print(result)
        assert result.strip().startswith("<|system|>")

    def test_contains_header(self):
        """Test to see if the tag is contained in the prompt for llama"""
        model = next((model for model in self.model_config if model['model_name'] == 'meta-llama/llama-3-70b-instruct'), None)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"

        result = Prompting.build_prompt(
            self.prompting,
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            model=model["model_name"],
            query=query,
            context=context,
        )
        assert "<|eot_id|>" in result

    def test_result_length(self):
        """Test to see if the prompt length is within the window for mistral"""
        model = next((model for model in self.model_config if model['model_name'] == 'mistralai/mistral-large'), None)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"

        result = Prompting.build_prompt(
            self.prompting,
            purpose=AiResponsePurpose.NOTE_CONVERSATION,
            model=model["model_name"],
            query=query,
            context=context,
        )
        assert len(result)>=0 and len(result)<=model["context_length"]

    def test_message(self):
        """Test to see if message's contents are added to prompt"""
        model = 'ibm/granite-3-2b-instruct'
        query = "summarize this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        message: MessagePayload = {"role": "assistant", "content": "This incident resulted in a data security breach caused by a faulty fail2ban instance, allowing an attacker access to the system."}

        result = self.prompting.build_prompt(
            AiResponsePurpose.NOTE_CONVERSATION,
            model,
            query,
            context,
            [message, {}]
        )
        assert message["content"] in result
