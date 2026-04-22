# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_network_utilities.util.utils_common import *

class TestNetworkUtilsCommonSeparateParams:
    """ Test Network Utilities utils_common separate params """
    @pytest.mark.parametrize("shell_params, expected_results", [
        ('안녕하세요 세상', {'shell_param1': '안녕하세요 세상'}),
        ('안녕하세요 $ 세상', {'shell_param1': '안녕하세요 \\$ 세상'}),
        ('恶意软件,坏的', {'shell_param1': '恶意软件', 'shell_param2': '坏的'}),
        ('something# ^bad', {'shell_param1': 'something\\# ^bad'})
    ])
    def test_separate_params(self, shell_params, expected_results):
        results = separate_params(shell_params)
        assert (expected_results == results)
