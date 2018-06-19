# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from watson_developer_cloud import LanguageTranslatorV3
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_watson_translate"
FUNCTION_NAME = "fn_watson_translate"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watson_translate_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_watson_translate", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_watson_translate_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnWatsonTranslate:
    """ Tests for the fn_watson_translate function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch("watson_developer_cloud.LanguageTranslatorV3")
    @pytest.mark.parametrize("source_lang, target_lang, source_text, expected_results, translate_value, identify_value",
                             [
                                 ("us", "text", "text", {"value": "k", "confidence": 1}, {"translations":[{"translation":"k"}]}, "uk"),
                                 ("us", "text", "text", {"value": "k", "confidence": 1}, {"translations":[{"translation":"k"}]}, "uk"),
                             ])
    def test_success(self, translator, circuits_app, source_lang, target_lang, source_text, expected_results,
                     translate_value, identify_value):
        """ Test calling with sample values for the parameters """
        translator.return_value = translator
        translator.translate.return_value = translate_value
        translator.identify.return_value = identify_value
        print(translator)
        function_params = {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "source_text": source_text
        }
        results = call_fn_watson_translate_function(circuits_app, function_params)
        assert(expected_results == results)