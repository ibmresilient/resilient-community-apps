# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Test helper functions"""

import pytest
from fn_proofpoint_trap.lib.helpers import *
"""
Suites of tests to test the Proofpoint TRAP Helper functions
"""
class Func(object):
    def __init__(self, options={}):
        self.options = options

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def convert_value_to_none(v):
    # Convert "None" string value to None value.
    if type(v) == str and v.lower() == 'none':
        v = None
    return v

class TestTrapHelpersTransformKwargs:
    """Test transform_kwargs function"""

    @pytest.mark.parametrize("trap_list_id, trap_member_id, trap_member, trap_description, trap_expiration, "
                             "trap_duration, trap_members_type", [
        (1, 8, "192.168.1.2", "Test", 1569798000000, 10, "members.json"),
        (None, None, None, None, None, None, None),
        ('none', 'None', 'NoNe', "nonE", "noNe", "", '')
    ])
    def test_transform_kwargs(self, trap_list_id, trap_member_id, trap_member, trap_description, trap_expiration,
                              trap_duration, trap_members_type):
        new_kwargs = {
            "list_id": convert_value_to_none(trap_list_id),
            "member_id": convert_value_to_none(trap_member_id),
            "member": convert_value_to_none(trap_member),
            "description": convert_value_to_none(trap_description),
            "expiration": convert_value_to_none(trap_expiration),
            "duration": convert_value_to_none(trap_duration),
            "members_type": convert_value_to_none(trap_members_type)
        }
        kwargs = {
            "trap_list_id": trap_list_id,
            "trap_member_id": trap_member_id,
            "trap_member": trap_member,
            "trap_description": trap_description,
            "trap_expiration": trap_expiration,
            "trap_duration": trap_duration,
            "trap_members_type": "trap_members_type"
        }
        params = transform_kwargs(kwargs)
        for key in new_kwargs:
            assert (key in params)

class TestTrapHelpersValidateAllSet:
    """Test validate_opts function"""

    @pytest.mark.parametrize("base_url, api_key, polling_interval, startup_interval, state, host_categories, expected_result", [
        ("https://127.0.0.1:5555", "abcd1234-a123-123a-123a-123456abcdef", "2", 60, "open", "forensics",
         None),
    ])
    def test_validate_opts_all_set(self, base_url, api_key, polling_interval, startup_interval, state, host_categories,
                                   expected_result):
        opt = {
            "base_url": base_url,
            "api_key": api_key,
            "polling_interval": polling_interval,
            "startup_interval": startup_interval,
            "state": state,
            "host_categories": host_categories,
        }
        for (k, v) in opt.copy().items():
            if v == '':
                opt.pop(k)

        func = Func(opt)

        result = validate_opts(func)
        assert expected_result == result