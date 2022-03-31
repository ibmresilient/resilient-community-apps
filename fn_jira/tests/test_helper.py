#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict, namedtuple
import mock
import pytest

from fn_jira.util.helper import (build_url_to_resilient, extract_images,
                                 format_dict, prepend_text, read_img,
                                 validate_app_configs,
                                 validate_task_id_for_jira_issue_id)
from resilient.co3 import SimpleClient


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


def test_prepend_text():
    assert prepend_text("mock text") == "mock text"
    assert prepend_text(u"mock Ü Ý Þ ß à á text", "abc") == u"mock Ü Ý Þ ß à á text\n\nabc"


def test_build_url_to_resilient():
    assert build_url_to_resilient("www.example.com", "443", 1000) == "https://www.example.com:443/#incidents/1000"
    assert build_url_to_resilient("www.example.com", "443", 1000, 123) == "https://www.example.com:443/#incidents/1000?task_id=123"


def test_format_dict():
    formatted_dict = format_dict(OrderedDict([("key1", "value Ü Ý Þ ß1"), ("key2", "value2")]))
    actual_result = """\n-----------------\nkey1: value Ü Ý Þ ß1\nkey2: value2\n-----------------\n"""

    assert formatted_dict == actual_result

def test_extract_images():
    mock_html = "<div>Text! <img src=\"https://img.com/img.jpg\" alt=\"img.jpg\" /> middle text! <img src=\"https://test.org/my_pic\" alt=\"my_pic\" /> </div>"
    expected_imgs = (("https://img.com/img.jpg", "img.jpg"), ("https://test.org/my_pic", "my_pic"))
    expected_formatted_html = "<div>Text! !img.jpg! middle text! !my_pic! </div>"

    assert extract_images(mock_html)[0] == expected_imgs
    assert extract_images(mock_html)[1] == expected_formatted_html

def test_read_img_external():
    mock_img_url = "https://example.com/some_img.jpg"
    mock_response = namedtuple("Response", "content")
    mock_ret_val = mock_response("fake_img_data")

    with mock.patch("fn_jira.util.helper.requests.get") as mock_req_get:
        mock_req_get.return_value = mock_ret_val

        img_content = read_img(None, mock_img_url)

        assert img_content == mock_ret_val.content

def test_read_img_from_soar_upload():
    mock_img_url = "/rest/images/some_img"
    mock_response = namedtuple("Response", "content")
    mock_ret_val = mock_response("fake_img_data")

    with mock.patch("resilient.co3.SimpleClient.get") as mock_req_get:
        mock_req_get.return_value = mock_ret_val

        img_content = read_img(SimpleClient(), mock_img_url)

        assert img_content == mock_ret_val.content

def test_read_img_exception():
    mock_img_url = "/rest/images/inaccessible"
    mock_response = namedtuple("Response", "content")
    mock_ret_val = mock_response("fake_img_data")

    with mock.patch("resilient.co3.SimpleClient.get") as mock_req_get:
        mock_req_get.side_effect = ConnectionError("url invalid")

        with pytest.raises(ConnectionError) as err:
            read_img(SimpleClient(), mock_img_url)

            assert "url invalid" in str(err.value)

def test_validate_task_id_for_jira_issue_id():
    mock_fn_inputs = {"jira_issue_id": "INT-9"}
    mock_app_config = {"jira_dt_name": "jira_task_references"}
    with mock.patch("fn_jira.util.helper._get_jira_issue_id") as mock_dt_call:
        mock_dt_call.return_value = ("INT-10", "https://jira.test/INT-10")

        valid = validate_task_id_for_jira_issue_id(None, mock_app_config, "100", "101", mock_fn_inputs)

        assert valid
        assert mock_fn_inputs["jira_issue_id"] == "INT-10"

def test_invalid_validate_task_id_for_jira_issue_id():
    mock_fn_inputs = {"jira_issue_id": "INT-9"}
    mock_app_config = {"jira_dt_name": "jira_task_references"}
    with mock.patch("fn_jira.util.helper._get_jira_issue_id") as mock_dt_call:
        mock_dt_call.return_value = (None, None)

        valid = validate_task_id_for_jira_issue_id(None, mock_app_config, "100", "101", mock_fn_inputs)

        assert not valid
