# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from bs4 import BeautifulSoup

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud.watson_service import WatsonApiException


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

            # Get the function parameters:
            source_lang = kwargs.get("fn_watson_translate_source_lang", None)  # text
            target_lang = kwargs.get("fn_watson_translate_target_lang", None)  # text
            source_text = kwargs.get("fn_watson_translate_source_text", None)  # text

            if source_text is None or target_lang is None:
                raise ValueError("Neither source_text nor target_lang can be unspecified.")

            # get rid of the HTML tags that notes can have.
            source_text = self._get_text_from_html(source_text)

            log.info("source_lang: %s", source_lang)
            log.info("target_lang: %s", target_lang)
            log.info("source_text: %s", source_text)

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
            except WatsonApiException as e:
                # if it couldn't be translated, return this message
                log.error(str(e))
                yield FunctionResult({"value": "Couldn't translate from {} to {}".format(source_lang, target_lang),
                                      "confidence": confidence, "language": target_lang})
                return

            # if the translation went through, but nothing was returned
            if len(translation['translations']) == 0:
                raise ValueError("Wasn't translated.")

            yield StatusMessage("Finished translating.")
            results = {
                "value": translation["translations"][0]["translation"],
                "confidence": confidence,
                "language": target_lang
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(e)
            yield FunctionError("An error occurred."+str(e))

    def _get_text_from_html(self, input):
        """
        Strips input from html.
        :param input: String
            Text from resilient's input field to be cleared of html.
        :return: String
            Stripped of html tags
        """
        return BeautifulSoup(input).get_text()

    def _get_translator(self):
        """
        Uses provided value in the config value to authenticate to Watson Translate API
        :return:  LanguageTranslatorV3
        """
        if not self.options["fn_watson_translate_api"] or not self.options["fn_watson_translate_version"] or \
                not self.options["fn_watson_translate_api"]:
            raise ValueError("Options do not have necessary information")
        return LanguageTranslatorV3(
                iam_api_key=self.options["fn_watson_translate_api"],
                version=self.options["fn_watson_translate_version"],
                url=self.options["fn_watson_translate_url"]
            )

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
        source_lang = source_lang_query['languages']
        if len(source_lang) > 0:
            confidence = source_lang[0]['confidence']
            source_lang = source_lang[0]['language']
        else:
            raise ValueError("The language wasn't identified.")
        return source_lang, confidence
