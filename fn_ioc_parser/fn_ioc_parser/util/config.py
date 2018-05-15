# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ioc_parser"""
# Copyright IBM Corp. - Confidential Information

from __future__ import print_function


CONFIG_SECTION = "fn_ioc_parser"


def config_section_data():

    config_result = """
[fn_ioc_parser]
filepath=
    """
    return config_result