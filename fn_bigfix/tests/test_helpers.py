# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Test helper functions"""

from __future__ import print_function
import pytest
from fn_bigfix.util.helpers import create_attachment
from mock_artifacts import mocked_res_client

"""Suite of tests to test Helper functions"""

class Func(object):
    def __init__(self, options=object):
        self.options = options

class TestHelpersCreateAttachment:
    """ Tests for the create_attachment function"""

    @pytest.mark.parametrize("file_name, file_content, params", [
        ("test_file.xml", 'My test data', {"incident_id": 12345})
    ])
    def test_create_attachment(self, file_name, file_content, params):
        """ Test create_attachment using mocked data. """

        results = create_attachment(mocked_res_client("post_attachment", file_name, params["incident_id"]), file_name, file_content, params)
        assert results["name"] == file_name
        assert results["inc_id"] == params["incident_id"]
