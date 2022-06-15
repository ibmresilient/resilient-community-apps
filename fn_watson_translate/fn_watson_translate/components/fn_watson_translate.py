# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from bs4 import BeautifulSoup
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields

OK = 200

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_watson_translate"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_watson_translate", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_watson_translate", {})

    @function("fn_watson_translate")
    def _fn_watson_translate_function(self, event, *args, **kwargs):
        """Function: translates input text to a target language"""
        log = logging.getLogger(__name__)
        self.should_except = False
        try:
            language_translator = self._get_translator()

            validate_fields(['fn_watson_translate_api', 'fn_watson_translate_version', 'fn_watson_translate_url'],
                           self.options)
            validate_fields(['fn_watson_translate_source_text', 'fn_watson_translate_target_lang'],
                           kwargs)

            # Get the function parameters:
            source_lang = kwargs.get("fn_watson_translate_source_lang", None)  # text
            target_lang = kwargs.get("fn_watson_translate_target_lang", None)  # text
            source_text = kwargs.get("fn_watson_translate_source_text", None)  # text

            # get rid of the HTML tags that notes can have.
            source_text = self._get_text_from_html(source_text)

            log.info("fn_watson_translate_source_lang: %s", source_lang)
            log.info("fn_watson_translate_target_lang: %s", target_lang)
            log.info("fn_watson_translate_source_text: %s", source_text)

            if source_lang is None:
                # get the source language and confidence it is the right language
                source_lang, confidence = self._identify_language(source_text, language_translator)
                yield StatusMessage("Identified language as {}".format(source_lang))
            else:
                # if language is specified we are confident it is the right language.
                confidence = 1
            try:
                translation = language_translator.translate(
                    text=source_text,
                    source=source_lang,
                    target=target_lang
                )
            except ApiException as e:
                # if it couldn't be translated, return this message
                log.error(str(e))
                yield FunctionResult({"value": "Couldn't translate from {} to {}".format(source_lang, target_lang),
                                      "confidence": confidence, "language": target_lang})
                return

            # if the translation went through, but nothing was returned
            if translation.get_status_code() != OK:
                raise ValueError("Wasn't translated.")

            yield StatusMessage("Finished translating.")
            results = {
                "value": translation.get_result()["translations"][0]["translation"],
                "confidence": confidence,
                "language": target_lang,
                "source_lang": source_lang
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(e)
            yield FunctionError("An error occurred. {}".format(str(e)))

    def _get_text_from_html(self, input):
        """
        Strips input from html.
        :param input: String
            Text from resilient's input field to be cleared of html.
        :return: String
            Stripped of html tags
        """
        return BeautifulSoup(input, "html.parser").get_text()

    def _get_translator(self):
        """
        Uses provided value in the config value to authenticate to Watson Translate API
        :return:  LanguageTranslatorV3
        """
        authenticator = IAMAuthenticator(self.options["fn_watson_translate_api"])
        language_translator = LanguageTranslatorV3(
                                    version=self.options["fn_watson_translate_version"],
                                    authenticator=authenticator)
        language_translator.set_service_url(self.options["fn_watson_translate_url"])

        return language_translator
        #'https://gateway.watsonplatform.net/language-translator/api')

    @staticmethod
    def _identify_language(text, language_translator):
        """

        :param text: String
            text that needs to be identified
        :return:
            source language : String, confidence : Number
            Returns source language name, and confidence it is correct
        """
        source_lang_query = language_translator.identify(text)

        if source_lang_query.get_status_code() == OK:
            query_result = source_lang_query.get_result()['languages'][0]
            confidence = query_result['confidence']
            source_lang = query_result['language']
            return source_lang, confidence
        else:
            raise ValueError(u"The language wasn't identified for text '{}'. Rerun and specify source language".format(text))
