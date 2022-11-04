#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
from fn_jira.util.helper import validate_app_configs

def test_validate_app_configs():
    mock_app_configs = {
        "url": "www.example.com",
        "auth_method": "BASIC",
        "user": "exampleuser",
        "password": "examplepassword",
        "verify_cert": "true"
    }

    valid_app_configs = validate_app_configs(mock_app_configs)

    assert valid_app_configs.get("url") == "www.example.com"
    assert valid_app_configs.get("user") == "exampleuser"
    assert valid_app_configs.get("auth_method") == "BASIC"
    assert valid_app_configs.get("password") == "examplepassword"
    assert valid_app_configs.get("verify_cert") is True
