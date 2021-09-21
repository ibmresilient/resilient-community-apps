# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_watson_translate
"""

import logging
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_watson_translate", {})

    authenticator = IAMAuthenticator(options["fn_watson_translate_api"])
    language_translator = LanguageTranslatorV3(version=options["fn_watson_translate_version"],
                                               authenticator=authenticator)
    language_translator.set_service_url(options["fn_watson_translate_url"])

    try:
        source_lang_query = language_translator.identify("hello world")

        if source_lang_query.get_status_code() == 200:
            return {"state": "success", "status_code": source_lang_query.status_code }
        else:
            return {"state": "failure", "status_code": source_lang_query.status_code }
    except ApiException as e:
        return {"state": "failure", "status_code": str(e)}
