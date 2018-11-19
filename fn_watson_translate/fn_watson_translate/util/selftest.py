# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_watson_translate
"""

import logging
from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud.watson_service import WatsonApiException

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_watson_translate", {})

    language_translator = LanguageTranslatorV3(
        version=options["fn_watson_translate_version"],
        iam_apikey=options["fn_watson_translate_api"],
        url=options["fn_watson_translate_url"]
    )

    try:
        source_lang_query = language_translator.identify("hello world")

        if source_lang_query.status_code == 200:
            return {"state": "success", "status_code": source_lang_query.status_code }
        else:
            return {"state": "failure", "status_code": source_lang_query.status_code }
    except WatsonApiException as e:
        return {"state": "failure", "status_code": e}
