# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import html2text

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
        try:
            language_translator = LanguageTranslatorV3(
                iam_api_key=self.options["fn_watson_translate_api"],
                version=self.options["fn_watson_translate_version"],
                url=self.options["fn_watson_translate_url"]
            )

            # Get the function parameters:
            source_lang = kwargs.get("source_lang", None)  # text
            target_lang = kwargs.get("target_lang", None)  # text
            source_text = kwargs.get("source_text", None)  # text

            if source_text is None or target_lang is None:
                raise FunctionError("Neither source_text nor target_lang can be unspecified.")

            # get rid of the HTML tags that notes can have.
            source_text = html2text.html2text(source_text)

            log = logging.getLogger(__name__)
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
                # log.error(str(e))
                print("I've been here for sure")
                raise FunctionError("First Watson error caught")
            if len(translation['translations']) == 0:
                raise FunctionError("Wasn't translated.")
            yield StatusMessage("Finished translating.")

            results = {
                "value": translation.get('translations')[0].get('translation')
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log = logging.getLogger(__name__)
            log.error(str(e))
            raise FunctionError("An error occurred, check out logs for details.")

    def _identify_language(self, text, language_translator):
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
            raise FunctionError("The language wasn't identified.")
        return source_lang, confidence
