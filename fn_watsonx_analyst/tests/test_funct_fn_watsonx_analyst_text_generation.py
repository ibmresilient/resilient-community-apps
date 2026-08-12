# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974
"""Tests using pytest_resilient_circuits"""

import pytest
from tests import helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_watsonx_analyst"
FUNCTION_NAME = "fn_watsonx_analyst_text_generation"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watsonx_analyst_text_generation_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_watsonx_analyst_text_generation", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_watsonx_analyst_text_generation_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnWatsonxTextGeneration:
    """ Tests for the fn_watsonx_analyst_text_generation function"""

    cold_mem_limit = "2 MB"

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_system_prompt": "sample text",
        "fn_watsonx_analyst_arguments": "",
        "fn_watsonx_analyst_prompt": "sample text"
    }
    expected_results_3 = "Lorem ipsum"

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_3),
    ])
    @pytest.mark.limit_memory(cold_mem_limit)
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        results = call_fn_watsonx_analyst_text_generation_function(circuits_app, mock_inputs)
        assert(results["content"]["raw_output"] == expected_results)

"""Unit tests for substitute_prompt_arguments function"""

import pytest
from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_text_generation import substitute_prompt_arguments


class TestSubstitutePromptArgumentsPositional:
    """Test positional argument substitution"""

    def test_single_positional_argument(self):
        """Test substitution with a single positional argument"""
        prompt = "Hello {}"
        arguments = "World"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello World"

    def test_multiple_positional_arguments(self):
        """Test substitution with multiple positional arguments"""
        prompt = "Hello {}, you are {}"
        arguments = "Alice,awesome"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice, you are awesome"

    def test_three_positional_arguments(self):
        """Test substitution with three positional arguments"""
        prompt = "{} {} {}"
        arguments = "one,two,three"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "one two three"

    def test_positional_with_spaces(self):
        """Test positional arguments with leading/trailing spaces"""
        prompt = "Hello {}, you are {}"
        arguments = " Alice , awesome "
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice, you are awesome"

    def test_positional_with_numbers(self):
        """Test positional arguments with numbers"""
        prompt = "The answer is {}"
        arguments = "42"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "The answer is 42"

    def test_positional_with_special_characters(self):
        """Test positional arguments with special characters"""
        prompt = "Email: {}"
        arguments = "user@example.com"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Email: user@example.com"

    def test_positional_empty_argument(self):
        """Test positional with empty argument value"""
        prompt = "Hello {}"
        arguments = ""
        result = substitute_prompt_arguments(prompt, arguments)
        # Empty string after strip means no substitution
        assert result == "Hello {}"


class TestSubstitutePromptArgumentsNamed:
    """Test named argument substitution"""

    def test_single_named_argument(self):
        """Test substitution with a single named argument"""
        prompt = "Hello {name}"
        arguments = "name=World"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello World"

    def test_multiple_named_arguments(self):
        """Test substitution with multiple named arguments"""
        prompt = "Hello {name}, you are {adj}"
        arguments = "name=Alice,adj=awesome"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice, you are awesome"

    def test_named_with_spaces_around_equals(self):
        """Test named arguments with spaces around equals sign"""
        prompt = "Hello {name}"
        arguments = "name = World"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello World"

    def test_named_with_spaces_in_values(self):
        """Test named arguments with spaces in values"""
        prompt = "Hello {name}, you are {adj}"
        arguments = "name=Alice Smith,adj=very awesome"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice Smith, you are very awesome"

    def test_named_with_comma_in_value(self):
        """Test named arguments with comma in value (complex case)"""
        prompt = "Hello {name}, you live in {city}"
        arguments = "name=Bob,city=New York, NY"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Bob, you live in New York, NY"

    def test_named_three_arguments(self):
        """Test substitution with three named arguments"""
        prompt = "{greeting} {name}, you are {adj}"
        arguments = "greeting=Hi,name=Charlie,adj=great"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hi Charlie, you are great"

    def test_named_with_numbers(self):
        """Test named arguments with numeric values"""
        prompt = "The answer is {num}"
        arguments = "num=42"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "The answer is 42"

    def test_named_with_special_characters_in_value(self):
        """Test named arguments with special characters in values"""
        prompt = "Email: {email}"
        arguments = "email=user@example.com"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Email: user@example.com"

    def test_named_arguments_order_independent(self):
        """Test that named arguments work regardless of order"""
        prompt = "Hello {name}, you are {adj}"
        arguments = "adj=awesome,name=Alice"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice, you are awesome"

    def test_named_with_underscores_in_keys(self):
        """Test named arguments with underscores in key names"""
        prompt = "Hello {first_name} {last_name}"
        arguments = "first_name=John,last_name=Doe"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello John Doe"


class TestSubstitutePromptArgumentsEdgeCases:
    """Test edge cases and error conditions"""

    def test_none_arguments(self):
        """Test with None arguments"""
        prompt = "Hello {}"
        arguments = None
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello {}"

    def test_empty_prompt(self):
        """Test with empty prompt"""
        prompt = ""
        arguments = "test"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == ""

    def test_none_prompt_with_arguments(self):
        """Test with None prompt but valid arguments"""
        prompt = None
        arguments = "test"
        # Should handle gracefully
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "" or result is None

    def test_prompt_without_placeholders(self):
        """Test prompt without any placeholders"""
        prompt = "Hello World"
        arguments = "test"
        with pytest.raises(ValueError):
            substitute_prompt_arguments(prompt, arguments)


    def test_more_arguments_than_placeholders_positional(self):
        """Test with more positional arguments than placeholders"""
        prompt = "Hello {}"
        arguments = "World,Extra"
        # Python's format will ignore extra arguments
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello World"

    def test_fewer_arguments_than_placeholders_positional(self):
        """Test with fewer positional arguments than placeholders"""
        prompt = "Hello {} {}"
        arguments = "World"
        with pytest.raises(ValueError):
            substitute_prompt_arguments(prompt, arguments)

    def test_missing_named_argument(self):
        """Test with missing named argument"""
        prompt = "Hello {name} {title}"
        arguments = "name=Alice"
        # Should raise KeyError
        with pytest.raises(KeyError):
            substitute_prompt_arguments(prompt, arguments)

    def test_extra_named_arguments(self):
        """Test with extra named arguments (should be ignored)"""
        prompt = "Hello {name}"
        arguments = "name=Alice,extra=value"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice"

    def test_whitespace_only_arguments(self):
        """Test with whitespace-only arguments"""
        prompt = "Hello {}"
        arguments = "   "
        result = substitute_prompt_arguments(prompt, arguments)
        # After strip, empty string means no substitution
        assert result == "Hello {}"

    def test_numeric_string_arguments(self):
        """Test with numeric string arguments"""
        prompt = "Count: {}"
        arguments = "123"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Count: 123"


class TestSubstitutePromptArgumentsComplexScenarios:
    """Test complex real-world scenarios"""

    def test_incident_summary_positional(self):
        """Test incident summary with positional arguments"""
        prompt = "Analyze incident {} with severity {}"
        arguments = "INC-12345,High"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Analyze incident INC-12345 with severity High"

    def test_incident_summary_named(self):
        """Test incident summary with named arguments"""
        prompt = "Analyze incident {id} with severity {severity}"
        arguments = "id=INC-12345,severity=High"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Analyze incident INC-12345 with severity High"

    def test_artifact_analysis_with_comma(self):
        """Test artifact analysis with comma in value"""
        prompt = "Analyze artifact {type} with value {value}"
        arguments = "type=IP Address,value=192.168.1.1, 192.168.1.2"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Analyze artifact IP Address with value 192.168.1.1, 192.168.1.2"

    def test_long_text_substitution(self):
        """Test with long text values"""
        prompt = "Summarize: {text}"
        long_text = "This is a very long text " * 10
        arguments = f"text={long_text}"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == f"Summarize: {long_text}".strip()

    def test_multiple_placeholders_same_name(self):
        """Test with multiple placeholders using same name"""
        prompt = "Hello {name}, nice to meet you {name}"
        arguments = "name=Alice"
        result = substitute_prompt_arguments(prompt, arguments)
        assert result == "Hello Alice, nice to meet you Alice"

