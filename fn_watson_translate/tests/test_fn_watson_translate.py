# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

from resilient_circuits.action_message import FunctionException_, FunctionError_
import logging

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
    print("Asserting event:")
    print(evt)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnWatsonTranslateE2E:
    """ Tests for the fn_watson_translate function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch("fn_watson_translate.components.fn_watson_translate.LanguageTranslatorV3")
    @pytest.mark.parametrize("source_lang, target_lang, source_text, expected_results, translate_value, identify_value",
                             [
                                 # source language is given, expected confidence - 1
                                 ("us", "su", "text", {"value": "txet", "confidence": 1, "language": "su"},
                                  {"translations": [{"translation": "txet"}]},
                                  {"languages": [{"language": "wrong", "confidence": 0}]}),
                                 # source language not given, has to be identified
                                 (None, "su", "text", {"value": "txet", "confidence": 0.7, "language": "su"},
                                  {"translations": [{"translation": "txet"}]},
                                  {"languages": [{"language": "su", "confidence": 0.7}]}),
                             ])
    def test_e2e_success(self, translator, circuits_app, source_lang, target_lang, source_text, expected_results,
                     translate_value, identify_value):
        """ Test calling with sample values for the parameters """
        translator = translator.return_value
        translator.translate.return_value = translate_value
        translator.identify.return_value = identify_value

        function_params = {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "source_text": source_text
        }
        results = call_fn_watson_translate_function(circuits_app, function_params)
        assert(expected_results == results)

    @patch("fn_watson_translate.components.fn_watson_translate.LanguageTranslatorV3")
    @pytest.mark.parametrize("source_lang, target_lang, source_text, expected_results, translate_value, identify_value",
                             [
                                 # target language not given
                                 ("us", None, "text", {"value": "txet", "confidence": 1, "language": "su"},
                                  {"translations": [{"translation": "txet"}]},
                                  {"languages": [{"language": "wrong", "confidence": 0}]}),
                                 # text not given
                                 ("us", "su", None, {"value": "txet", "confidence": 0.7, "language": "su"},
                                  {"translations": [{"translation": "txet"}]},
                                  {"languages": [{"language": "su", "confidence": 0.7}]}),
                                 # # Source not given, no correct results
                                 ("us", "su", None, {"value": "txet", "confidence": 0.7, "language": "su"},
                                  {"translations": [{"translation": "txet"}]},
                                  {"languages": []}),
                             ])
    def test_e2e_fail_bad_parameters(self, translator, source_lang, target_lang, source_text, expected_results,
                         translate_value, identify_value, caplog, circuits_app):
        """ Test calling with sample values for the parameters """
        # caplog.set_level(logging.DEBUG)
        translator = translator.return_value
        translator.translate.return_value = translate_value
        translator.identify.return_value = identify_value

        function_params = {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "source_text": source_text
        }
        with pytest.raises(AssertionError):
            results = call_fn_watson_translate_function(circuits_app, function_params)