"""Unit Tests for Prompting"""

# pylint: disable=line-too-long

import pytest
import json
import os

from unittest.mock import patch

from fn_watsonx_analyst.types.message_payload import MessagePayload
from fn_watsonx_analyst.util.prompting import Prompting
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.state_manager import app_state
from tests import helper
from tests.helper import generate_app_state


@patch("fn_watsonx_analyst.util.QueryHelper.QueryHelper.get_api_key", helper.mock_get_api_key)
@patch("fn_watsonx_analyst.util.QueryHelper.QueryHelper.generate_embeddings", helper.mock_generate_embeddings)
class TestPrompting:
    """Unit tests for Prompting class."""

    prompting: Prompting
    model_config: dict

    generate_app_state()

    def create_chunker(self) -> Chunking:
        return Chunking()

    def setup_method(self):
        """Initialize the model config"""
        self.prompting = Prompting()

        current_dir = os.path.dirname(__file__)

        # Construct the relative path to model_config.json from the current directory
        model_config_path_test = os.path.abspath(
            os.path.join(current_dir, "../../../../fn_watsonx_analyst/fn_watsonx_analyst/util/model_config.json")
        )

        # Load the model configuration file
        with open(model_config_path_test, "r", encoding="utf-8") as f:
            self.model_config = json.load(f)


    def test_return_type(self):
        """Test to see if the prompt is of a correct type for granite 3"""
        model = "ibm/granite-3-2b-instruct"
        generate_app_state(model_id=model)
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        result = Prompting.build_prompt(
            self.prompting,
            model=model,
            query=query,
            context=context,
            chunking=self.create_chunker()
        )
        assert isinstance(result, str)

    def test_code_results(self):
        """Test to see if the prompt format is correct for code instruct models """
        model = 'ibm/granite-8b-code-instruct'
        generate_app_state(model_id=model)
        query = "Give me a code to loop from 1 to 3"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        app_state.get().set_model(model)

        result = Prompting.build_prompt(
            self.prompting,
            query=query,
            context=context,
        )
        assert result.strip().endswith("Answer:")

    def test_invalid_model(self):
        """Test to see if the method catches an invalid model ask"""
        generate_app_state(model_id='google/bard')
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        expected_error ="model not found"
        with pytest.raises(ValueError) as error:
            Prompting().build_prompt(
            query=query,
            context=context,
        )
        assert str(error.value) == str(expected_error)

    def test_default_model(self):
        """ Test to see if the method catches an invalid model ask"""
        generate_app_state()
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        result = Prompting().build_prompt(
            query=query,
            context=context,
        )
        assert result.strip().startswith("<|start_of_role|>")


    def test_contains_header(self):
        """Test to see if the tag is contained in the prompt for granite"""
        generate_app_state()
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"

        result = Prompting().build_prompt(
            query=query,
            context=context,
        )
        assert "<|start_of_role|>" in result

    def test_result_length(self):
        """Test to see if the prompt length is within the window for mistral"""
        model = next((model for model in self.model_config if model['model_name'] == 'mistralai/mistral-large'), None)
        app_state.get().model_id = model["model_name"]
        query = "summarise this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"

        result = Prompting().build_prompt(
            query=query,
            context=context,
        )
        assert 0 <= len(result) <= model["context_length"]

    def test_message(self):
        """Test to see if message's contents are added to prompt"""
        generate_app_state()
        query = "summarize this incident"
        context = "In the age of information, data-driven decisions shape the world. Every click, like, and share becomes a data point in a vast digital ecosystem, where algorithms analyze human behavior to predict preferences"
        message: MessagePayload = {"role": "assistant", "content": "This incident resulted in a data security breach caused by a faulty fail2ban instance, allowing an attacker access to the system."}

        result = Prompting().build_prompt(
            query,
            context,
            [message, {}]
        )
        assert message["content"] in result

    def test_default_language(self):
        lang = "pt"
        app_state.get().opts["fn_watsonx_analyst"]["default_language"] = lang
        assert Prompting()._get_default_language() == lang

    def test_default_language_fallback(self):
        opts = app_state.get().opts["fn_watsonx_analyst"]
        del opts["default_language"]
        app_state.get().opts = opts
        assert Prompting()._get_default_language() == "en"

    def test_format(self):
        generate_app_state(purpose=AiResponsePurpose.ARTIFACT_SUMMARY)
        assert Prompting().build_prompt(
            query=None,
            context="",
            messages=None,
            get_relevant_prompts=False,
            content_type="application/json"
        ).__contains__("observe the above section of application/json data")
