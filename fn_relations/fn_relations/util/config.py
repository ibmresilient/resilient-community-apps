# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

"""Generate a default configuration-file section for fn_relations"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_relations when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

#    config_data = u"""[fn_relations]
#setting=xxx
#"""
    return config_data
