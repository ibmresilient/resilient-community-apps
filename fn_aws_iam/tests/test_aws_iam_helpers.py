# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_aws_iam.lib.helpers import *
"""
Suites of tests to test the AWS IAM Helper functions
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def convert_value_to_none(v):
    # Convert "None" string value to None value.
    if type(v) == str and v.lower() == 'none':
        v = None
    return v

class Func(object):
    def __init__(self, options={}):
        self.options = options

class TestAwsIamHelpersTransformKwargs:
    """Test transform_kwargs function"""

    @pytest.mark.parametrize("aws_iam_access_keys, aws_iam_password, aws_iam_password_reset_required, aws_iam_user_name, "
                             "", [
        ("AKAABBCCDDEEFFGGHH12", "MyNewPass", True, "Test_user"),
        (None, None, None, None),
        ('none', 'None', 'NoNe', "nonE"),
        ("noNe", "", "nOne", '')
    ])
    def test_transform_kwargs(self, aws_iam_access_keys, aws_iam_password, aws_iam_password_reset_required,
                              aws_iam_user_name):
        new_kwargs = {
            "AccessKeys": convert_value_to_none(aws_iam_access_keys),
            "Password": convert_value_to_none(aws_iam_password),
            "PasswordResetRequired": convert_value_to_none(aws_iam_password_reset_required),
            "UserName": convert_value_to_none(aws_iam_user_name),

        }
        kwargs = {
            "aws_iam_access_keys": aws_iam_access_keys,
            "aws_iam_password": aws_iam_password,
            "aws_iam_password_reset_required": aws_iam_password_reset_required,
            "aws_iam_user_name": aws_iam_user_name
        }
        params = transform_kwargs(kwargs)
        for key in new_kwargs:
            assert (key in params)

class TestAwsIamSnakeCaseToPascal:
    """Test snake_to_pascal function"""

    @pytest.mark.parametrize("snake_string, expected_result", [
        ("snake_case", "SnakeCase"),
        ("snake_snake_case", "SnakeSnakeCase"),
        ('a__snake_case', 'A_SnakeCase'),
        ('_a__snake_case', '_A_SnakeCase'),
        ('_a__snake_case_', '_A_SnakeCase_'),
        ('a_snake_case', 'ASnakeCase'),
        ('a__snake__case', 'A_Snake_Case')
    ])
    def test_snake_to_pascal(self, snake_string, expected_result):

        result = snake_to_pascal(snake_string)

        assert expected_result == result

class TestAwsIamValidateOptsGood:
    """Test validate_opts function"""

    @pytest.mark.parametrize("aws_iam_access_key_id, aws_iam_secret_access_key, expected_results", [
                                 ('AKAABBCCDDEEFFGGHH12', "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss", None),
                             ])
    def test_validate_opts_Not_set(self, aws_iam_access_key_id, aws_iam_secret_access_key, expected_results):
        opt = {
            "aws_iam_access_key_id": aws_iam_access_key_id,
            "aws_iam_secret_access_key": aws_iam_secret_access_key
        }

        func = Func(opt)

        result = validate_opts(func)
        assert expected_results == result


class TestAwsIamValidateOptsErr:
    """Test validate_opts function"""

    @pytest.mark.parametrize("aws_iam_access_key_id, aws_iam_secret_access_key, expected_results", [
        (None, None, "Mandatory config setting 'aws_iam_access_key_id' not set."),
        (None, "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss", "Mandatory config setting 'aws_iam_access_key_id' not set."),
        ("AKAABBCCDDEEFFGGHH12", None, "Mandatory config setting 'aws_iam_secret_access_key' not set.")
    ])
    def test_validate_opts_Not_set(self, aws_iam_access_key_id, aws_iam_secret_access_key, expected_results):
        opt = {
            "aws_iam_access_key_id": aws_iam_access_key_id,
            "aws_iam_secret_access_key": aws_iam_secret_access_key
        }

        func = Func(opt)

        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)
        pass

    @pytest.mark.parametrize("aws_iam_access_key_id, aws_iam_secret_access_key, expected_results", [
        ("", None, "Invalid value for config setting 'aws_iam_access_key_id'."),
        ("\'\'", None, "Invalid value for config setting 'aws_iam_access_key_id'."),
        ("AKAABBCCDDEEFFGGHH12", "", "Invalid value for config setting 'aws_iam_secret_access_key'."),
        ("AKAABBCCDDEEFFGGHH12", "\'\'", "Invalid value for config setting 'aws_iam_secret_access_key'."),
      ])
    def test_validate_opts_Invalid(self, aws_iam_access_key_id, aws_iam_secret_access_key, expected_results):
        opt = {
            "aws_iam_access_key_id": aws_iam_access_key_id,
            "aws_iam_secret_access_key": aws_iam_secret_access_key
        }
        func = Func(opt)
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)