# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""AppFunction implementation"""
import re

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting
from fn_watsonx_analyst.util.watsonx_client import WatsonxClient
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_text_generation"

log = create_logger(__name__)

def substitute_prompt_arguments(prompt: str, arguments: str | None) -> str:
    """
    Substitute arguments into a prompt template.
    
    Supports two formats:
    1. Positional: "arg1,arg2,arg3" -> prompt.format(arg1, arg2, arg3)
    2. Named: "key1=value1,key2=value2" -> prompt.format(key1=value1, key2=value2)
    
    Named format is detected by the presence of '=' in the arguments string.
    Named format handles commas within values correctly.
    
    Args:
        prompt: The prompt template with {} placeholders
        arguments: Comma-separated arguments (positional or named format), or None
        
    Returns:
        The prompt with arguments substituted, or original prompt if no arguments
        
    Examples:
        >>> substitute_prompt_arguments("Hello {}", "World")
        'Hello World'
        
        >>> substitute_prompt_arguments("Hello {name}", "name=World")
        'Hello World'
        
        >>> substitute_prompt_arguments("Hello {}, you are {}", "Alice,awesome")
        'Hello Alice, you are awesome'
        
        >>> substitute_prompt_arguments("Hello {name}, you are {adj}", "name=Alice,adj=awesome")
        'Hello Alice, you are awesome'
        
        >>> substitute_prompt_arguments("Hello {name}, you live in {city}", "name=Bob,city=New York, NY")
        'Hello Bob, you live in New York, NY'
    """
    if not arguments:
        return prompt
    
    if not prompt:
        return ""
    
    arguments = str(arguments).strip()
    
    # If arguments is empty after stripping, return original prompt
    if not arguments:
        return prompt
    
    try:
        # Check if it looks like named format (has key=value pattern)
        if re.search(r'\w+\s*=', arguments):
            # Named format: Parse "key1=value1,key2=value2"
            # Handles commas in values by looking for pattern: word=...until next word=
            kwargs = {}
            # Match pattern: word characters, optional spaces, =, then capture until next key= or end
            # This pattern captures everything after = until we hit ", word=" or end of string
            pattern = r'(\w+)\s*=\s*([^,]+(?:,(?!\s*\w+\s*=)[^,]+)*)'
            for match in re.finditer(pattern, arguments):
                key = match.group(1).strip()
                # Strip only leading whitespace from value, preserve trailing
                value = match.group(2).lstrip()
                kwargs[key] = value
            return prompt.format(**kwargs)
        else:
            # Positional format (backward compatibility)
            args_list = [arg.strip() for arg in arguments.split(",")]
            result = prompt.format(*args_list)
            
            # Check if any substitution actually happened
            # If prompt has no placeholders, format returns unchanged string
            if result == prompt and '{}' not in prompt:
                # No placeholders were found but arguments were provided
                raise ValueError("No placeholders found in prompt but arguments were provided")
            
            return result
    except KeyError as e:
        # Missing named argument - preserve KeyError
        raise
    except IndexError as e:
        # Wrong number of positional arguments - convert to ValueError
        raise ValueError(f"Error formatting prompt with positional arguments: {str(e)}") from e
    except Exception as e:
        # Other formatting errors
        raise ValueError(f"Error formatting prompt: {str(e)}") from e


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_text_generation'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Perform Text Generation against watsonx™. 
            Can replace '{}' in prompts with comma-separated strings in `fn_watsonx_analyst_arguments`.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_prompt
            -   fn_inputs.fn_watsonx_analyst_system_prompt
            -   fn_inputs.fn_watsonx_analyst_arguments
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_model_id_override
        """
        _ = generate_request_id()

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_state.get().reset()

        app_state.get().set_model(getattr(fn_inputs, "fn_watsonx_analyst_model_id", None))
        app_state.get().opts = self.opts
        app_state.get().res_client = self.rest_client()
        app_state.get().purpose = AiResponsePurpose.TEXT_GENERATION

        prompt = getattr(fn_inputs, "fn_watsonx_analyst_prompt", None) or ""
        system_prompt = getattr(fn_inputs, "fn_watsonx_analyst_system_prompt", None) or ""
        arguments = getattr(fn_inputs, "fn_watsonx_analyst_arguments", None) or ""

        try:
            # Build user message from prompt with argument substitution
            user_message = substitute_prompt_arguments(prompt if prompt else "", arguments)

            # Build chat messages using ChatPrompting
            chat_prompting = ChatPrompting()
            messages = chat_prompting.build_simple_chat(
                system_prompt=system_prompt,
                user_message=user_message
            )

            response = WatsonxClient().chat(messages)
            results = ResponseHelper().text_chat_to_ai_response(response)

            yield FunctionResult(results)

        # pylint: disable=broad-exception-caught
        except Exception as e:
            log.exception("Error in text generation function")
            yield FunctionResult({"error": str(e)}, success=False, reason=str(e))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

