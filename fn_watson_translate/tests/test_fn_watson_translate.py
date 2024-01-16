# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function

from bs4.element import ResultSet
import pytest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_watson_translate.components.fn_watson_translate import FunctionComponent

_identify_language = FunctionComponent._identify_language

import logging

PACKAGE_NAME = "fn_watson_translate"
FUNCTION_NAME = "fn_watson_translate"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

class MockBase():
    def __init__(self, result, rc=None):
        self.result = result
        self.rc = rc

    def get_status_code(self):
        return self.rc

    def get_result(self):
        return self.result

class MockTranslate(MockBase):
    def set_service_url(self, url):
        pass

class MockIdentify(MockBase):
    pass

class MockLanguageTranslator():
    def __init__(self, identify_results, translate_results, irc=200, trc=200):
        self.identify_results = MockIdentify(identify_results, rc=irc)
        self.translate_results = MockTranslate(translate_results, rc=trc)

    def identify(self, text):
        return self.identify_results

    def translate(self, **kwargs):
        return self.translate_results

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

    @patch("fn_watson_translate.components.fn_watson_translate.FunctionComponent._get_translator")
    @pytest.mark.parametrize("source_lang, target_lang, source_text, expected_results, translate_value, identify_value",
                             [
                                 # source language is given, expected confidence - 1
                                 ("en", "su", "1.1 text", {"value": "1.1 txet", "confidence": 1, "language": "su", "source_lang": "en"},
                                  {"translations": [{"translation": "1.1 txet"}]},
                                  {"languages": [{"language": "wrong", "confidence": 0}]}),
                                 # source language not given, has to be identified
                                 (None, "su", "1.2 text", {"value": "1.2 txet", "confidence": 0.7, "language": "su", "source_lang": "su"},
                                  {"translations": [{"translation": "1.2 txet"}]},
                                  {"languages": [{"language": "su", "confidence": 0.7}]}),
                                 # check that html is stripped
                                 ("en", "su", "<div>1.3 text</div>", {"value": "1.3 txet", "confidence": 1, "language": "su", "source_lang": "en"},
                                  {"translations": [{"translation": "1.3 txet"}]},
                                  {"languages": [{"language": "su", "confidence": 0.7}]}),
                             ])
    def test_e2e_success(self, translator, circuits_app, source_lang, target_lang, source_text, expected_results,
                     translate_value, identify_value):
        """ Test calling with sample values for the parameters """
        translator.return_value = MockLanguageTranslator(identify_value, translate_value)

        function_params = {
            "fn_watson_translate_source_lang": source_lang,
            "fn_watson_translate_target_lang": target_lang,
            "fn_watson_translate_source_text": source_text
        }
        results = call_fn_watson_translate_function(circuits_app, function_params)
        assert expected_results == results

    @patch("fn_watson_translate.components.fn_watson_translate.FunctionComponent._get_translator")
    @pytest.mark.parametrize("text", [("2.2 text")] )
    def test_identify_language(self, translator, text):
        """ Test calling with sample values for the parameters """
        translator.return_value = MockLanguageTranslator(None, None, irc=303)

        with pytest.raises(ValueError):
            results = _identify_language(None, translator)

    @patch("fn_watson_translate.components.fn_watson_translate.FunctionComponent._get_translator")
    @pytest.mark.parametrize("source_lang, target_lang, source_text, expected_results, translate_value, identify_value",
                             [
                                 # Target language not given
                                 ("en", None, "3.1  text", {"value": "3.1 txet", "confidence": 1, "language": "su"},
                                  {"translations": [{"translation": "3.1 txet"}]},
                                  {"languages": [{"language": "wrong", "confidence": 0}]}),
                                 # Text not given
                                 ("en", "su", None, {"value": "3.2 txet", "confidence": 0.7, "language": "su"},
                                  {"translations": [{"translation": "3.2 txet"}]},
                                  {"languages": [{"language": "su", "confidence": 0.7}]}),
                                 # Source not given, no correct results
                                 ("en", "su", None, {"value": "3.3 txet", "confidence": 0.7, "language": "su"},
                                  {"translations": [{"translation": "3.3 txet"}]},
                                  {"languages": []}),
                                 # No source, and no guesses on language
                                 (None, "su", "3.4 text", {"value": "3.4 txet", "confidence": 0.7, "language": "su"},
                                  {"translations": []},
                                  {"languages": []}),
                                 # No translation
                                 ("en", "su", "3.5 text", {"value": "3.5 txet", "confidence": 0.7, "language": "su"},
                                  {"translations": []},
                                  {"languages": []}),

                             ])
    def test_e2e_fail_bad_parameters(self, translator, source_lang, target_lang, source_text, expected_results,
                         translate_value, identify_value, caplog, circuits_app):
        """ Test calling with sample values for the parameters """
        translator.return_value = MockLanguageTranslator(identify_value, translate_value)

        function_params = {
            "fn_watson_translate_source_lang": source_lang,
            "fn_watson_translate_target_lang": target_lang,
            "fn_watson_translate_source_text": source_text
        }
        with pytest.raises(AssertionError):
            results = call_fn_watson_translate_function(circuits_app, function_params)
