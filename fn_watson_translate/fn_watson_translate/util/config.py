# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_watson_translate"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_watson_translate]
fn_watson_translate_api=xxx
fn_watson_translate_version=xxxx-xx-xx
fn_watson_translate_url=xxx
    """
    return config_data
